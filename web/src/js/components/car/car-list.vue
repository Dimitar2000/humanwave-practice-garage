<template>
    <div>
        <div v-for="car in cars" :key="car.id">
            <car-list-item :name="car.name" :owner="car.owner" :price="car.price"></car-list-item>
            <button @click="deleteCarFromList(car.id)">Delete</button>
        </div>
    </div>
</template>

<script>
import carListItem from './car-list-item.vue'
export default {
  emits: [ 'remove-car'],
  props: [ 'cars' ],
  components: { carListItem },

  methods: {
    deleteCarFromList(id) {
        console.log("Car has to be deleted ");

        this.$emit("remove-car", id)
    }
  }
}
</script>

<style>

</style>