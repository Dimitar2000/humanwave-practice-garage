<template>
    <div>
        <h3>Add a new car to garage</h3>
        <div class="row">
            <label class="col-sm-4">Name</label>
            <input type="text" class="col-sm-8" v-model="newCar.name"/>
        </div>
        <div class="row">
            <label class="col-sm-4">Price</label>
            <input type="number" class="col-sm-8" v-model.number="newCar.price"/>
        </div>
        <div class="row">
            <label class="col-sm-4">Owner</label>
            <input type="text" class="col-sm-8" v-model="newCar.owner"/>
        </div>
        <div class="row">
            <button class="pull-right btn btn-success" @click="save">Save</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "car-form",
        emits: ["submit-data"],
        props: {
            name: {
                required: false,
                default: ""
            },
            owner: {
                required: false,
                default: ""
            },
            price: {
                required: false,
                default: null
            },
            resetOnSave: {
                required: false,
                default: true
            }
        },
        data() {
            return {
                newCar: null
            }
        },

        created() {
            this.newCar = {
                name: this.name,
                owner: this.owner,
                price: this.price
            }
        },

        methods:{
            save() {
                this.$emit("submit-data", this.newCar);
                
                if (this.resetOnSave)
                {
                    this.resetForm();
                }
            },
            resetForm() {
                this.newCar = {
                    name: '',
                    owner: '',
                    price: null
                }
            },

        },
        watch: {
        }
    }
</script>

<style scoped>

</style>