<template>
    <div class="card">
        <div v-for="car in cars" :key="car.id">
            <button @click="deleteCarFromList(car.id)">Delete</button>
            <car-list-item 
                :name="car.name" 
                :owner="car.owner" 
                :price="car.price"
                
                @edit-car="updateCar($event, car.id)">
            </car-list-item>
        </div>
    </div>
</template>

<script>
import carListItem from './car-list-item.vue'
export default {
  emits: [ 'remove-car', 'update-car'],
  props: [ 'cars' ],
  components: { carListItem },

  methods: {
    deleteCarFromList(id) {
        console.log("Car has to be deleted ");

        this.$emit("remove-car", id)
    },

    updateCar(event, id) {
        console.log("Car has to be updated ");

        // Get the new car details from the event object
        const newCarData = {
            name: event.name,
            owner: event.owner,
            price: event.price
        };

        this.$emit("update-car", id, newCarData);
    }
  }
}
</script>

<style>
.card {
    width: fit-content;
}
</style>