<template>
    <div>
        <div v-for="car in cars" :key="car.id">
            <car-list-item :name="car.name" :owner="car.owner" :price="car.price"></car-list-item>
            <button @click="deleteCarFromList">Delete</button>
        </div>
    </div>
</template>

<script>
import carListItem from './car-list-item.vue'
export default {
  props: [ 'cars' ],
  components: { carListItem },

  methods: {
    deleteCarFromList() {
        console.log("Car has to be deleted ");
    }
  }
}
</script>

<style>

</style>