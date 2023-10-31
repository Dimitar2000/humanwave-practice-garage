<template>
    <div>
        <h3>Add a new car to garage</h3>
        <div class="row">
            <label class="col-sm-4">Name</label>
            <input type="text" class="col-sm-8" v-model="newCar.name"/>
        </div>
        <div class="row">
            <label class="col-sm-4">Price</label>
            <input type="number" class="col-sm-8" v-model="newCar.price"/>
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
        data() {
            return {
                newCar: {
                    name: '',
                    owner: '',
                    price: ''
                }
            }
        },
        methods:{
            save() {
                this.$emit("submit-data", this.newCar);
                this.resetForm();
            },
            resetForm() {
                this.newCar = {
                    name: '',
                    owner: '',
                    price: ''
                }
            },

        },
        watch: {
        }
    }
</script>

<style scoped>

</style>