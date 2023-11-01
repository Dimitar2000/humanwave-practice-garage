<template>
    <div class="garage-item-grid">
        <div>
            <div class="garage-name">
                <span class="name">{{ garage.name }}</span>
                <button @click="refresh">Refresh</button>
                <button @click="toggleDisplayCarForm">{{ addCarButtonLabel }}</button>
                <template v-if="!editing">
                    <button type="button" class="btn btn-primary" @click="editing=!editing">Edit</button>
                    <button type="button" class="btn btn-danger" @click="deleteGarage">Delete</button>
                </template>
                <template v-else>
                    <!--<button type="button" class="btn btn-primary" @click="save">Save</button>-->
                    <button type="button" class="btn btn-default" @click="editing=!editing; Object.assign(garage, updated_garage)">Cancel</button>
                </template>
            </div>
            <div v-if="editing" class="edit-garage">
                <garage-form :garage="garage" @change="editing = false; Object.assign(updated_garage, garage)"></garage-form>
            </div>
        </div>
        <div class="garage-cars">
            <div v-if="displayCarForm">
                <car-form @submit-data="addCarToGarage"></car-form>
            </div>
            <div>
                <div class="car-list">
                    <div v-for="car in cars" :key="car.id">
                        <button @click="removeCarFromGarage(car.id)">Delete</button>
                        <car-list-item 
                            :name="car.name" 
                            :owner="car.owner" 
                            :price="car.price"
                            
                            @edit-car="updateCar($event, car.id)">
                        </car-list-item>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import GarageForm from "./garage-form";
    import CarForm from './car/car-form.vue';
    import carListItem from './car/car-list-item.vue'

    export default {
        name: "garage-list-item",
        components: {GarageForm, CarForm, carListItem},
        props: {
            garage: {
                type: Object,
                required: true
            }
        },
        data() {
            return {
                updated_garage: {},
                editing: false,
                displayCarForm: false,
                cars: []
            }
        },
        mounted() {
            this.updated_garage = Object.assign({}, this.garage)
            this.load_cars()
        },
        computed: {
            addCarButtonLabel() {
                return this.displayCarForm ? "Hide Car Form" : "Add Car";
            }
        },
        methods: {
            toggleDisplayCarForm() {
                this.displayCarForm = !this.displayCarForm;
            },

            // Add car when form is submitted
            addCarToGarage(carData) {
                console.log("Car to be sent: ", JSON.stringify(carData));

                $.ajax({
                    type: 'POST',
                    contentType: 'application/json',
                    url: `/garages/car`,
                    data: JSON.stringify({carData: carData, garage_id: this.garage.id})
                }).then((resp_data) => {
                    console.log("Car was added to garage: ", resp_data);
                    this.cars.push(resp_data)
                }).always(() => {
                })
            },
            removeCarFromGarage(car_id) {
                $.ajax({
                    type: 'DELETE',
                    contentType: 'application/json',
                    url: `/garages/car`,
                    data: JSON.stringify({car_id: car_id})
                }).then((data) => {
                    console.log("Car was removed from garage: ", data);
                    this.refresh();
                }).always(() => {
                })
            },
            updateCar(newCarData, id) {
                newCarData["car_id"] = id

                console.info("GarageListItem:updateCar - ", newCarData);
                
                // Send a PUT request to update the car data
                $.ajax({
                    type: 'PUT',
                    contentType: 'application/json',
                    url: `/garages/car`,
                    data: JSON.stringify(newCarData)
                }).then((data) => {
                    console.log("--- Car was updated");

                    this.load_cars();

                }).always(() => {
                })
            },
            deleteGarage() {
                $.ajax({
                    type: 'DELETE',
                    contentType: 'application/json',
                    url: `/garages/`,
                    data: JSON.stringify({'garage': this.garage.id})
                }).then((data) => {
                    this.$emit('change-delete', this.garage.id)
                }).always(() => {
                })
            },
            refresh() {
                $.ajax({
                    type: 'GET',
                    contentType: 'application/json',
                    url: `/garages/?garage=${this.garage.id}`,
                }).then((data) => {
                    console.log("Garage fetched: ", data)
                    Object.assign(this.garage, data) // watch does not work this way then we need to use deep watch
                    Object.assign(this.updated_garage, this.garage)

                    this.load_cars();

                }).always(() => {
                })

            },

            load_cars() {
                $.ajax({
                    type: 'GET',
                    contentType: 'application/json',
                    url: `/garages/car?garage_id=${this.garage.id}`
                }).then((resp) => {
                    console.log("Cars fetched: ", resp)
                    this.cars = resp
                }).always(() => {})
            } 
        },
        watch: {
            garage(g) {
                console.log('garage update:' + g)
                Object.assign(this.updated_garage, g)
            }
        }
    }
</script>

<style scoped>

    .car-list {
        width: fit-content;
    }
    .garage-item-grid {
		display: grid;
		grid-template-columns: 1fr 3fr;
		grid-gap: 10px;
		grid-auto-rows: min-content;
		grid-template-areas:
			"garage-name edit-garage garage-cars";
	}

    .garage-name {
        grid-area: garage-name;
        display: grid;
        grid-gap: 10px;
        grid-template-columns: 3fr 1fr;
        grid-auto-rows: min-content;
        grid-template-areas:
            "name btn-top"
            ". btn-bottom";
    }

    .btn-primary { grid-area: btn-top }
    .btn-default { grid-area: btn-bottom }
    .btn-danger { grid-area: btn-bottom }

    .edit-garage {
        grid-area: edit-garage;
        display: grid;
        grid-gap: 10px;
        grid-template-columns: 6fr 1fr;
        grid-template-areas:
            "name v-model-name"
            "brand v-model-brand"
            "country v-model-country";
        /* for some reason justify-items isn't working properly yet... */
        justify-items: end | start;
    }

    .name { grid-area: name; }
    .v-model-name { grid-area: v-model-name; }
    .brand { grid-area: brand; }
    .v-model-brand { grid-area: v-model-brand; }
    .country { grid-area: country; }
    .v-model-country {grid-area: v-model-country; }

</style>