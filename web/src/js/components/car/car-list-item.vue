<template>
  <div class="card body">
    <label>Name: {{ name }}</label>
    <label>Owner: {{ owner }}</label>
    <label>Price: {{ price }}</label>
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

.card {
    border: black 18rem;
}

</style>