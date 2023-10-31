<template>
  <div class="card">
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
  </div>
</template>

<script>
export default {
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
    }
}
</script>

<style scoped>



</style>