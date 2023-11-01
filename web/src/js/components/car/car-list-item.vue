<template>
  <div class="card">
    <button @click="toggleEditForm">Edit</button>
    <p class="car-data">
        <ul class="list-group">
            <li class="list-group-item">
                Name: <label>{{ name }}</label>
            </li>
            <li class="list-group-item">
                Owner: <label>{{ owner }}</label>
            </li>
            <li class="list-group-item">
                Price: <label>{{ price }}</label>
            </li>
        </ul>
        <car-form v-if="editing"></car-form>
    </p>
  </div>
</template>

<script>
import carForm from './car-form.vue'
export default {
    components: { carForm },
    emits: ['edit-car'],
    props: {
        name: {
            required: true
        },
        owner: {
            required: true
        },
        price: {
            required: true,
            type: Number
        }
    },
    
    data() {
        return {
            editing: false,
            updatedCar: {
                name: null,
                owner: null,
                price: null
            }
        }
    },

    created() {
        // Copy props to updated car
        this.updatedCar = {
            name: this.name,
            owner: this.owner,
            price: this.price
        }
    },
    
    methods: {
        toggleEditForm() {
            this.editing = !this.editing
        }
    },
}
</script>

<style scoped>



</style>