<template>
  <div>
    <h3>Name: {{ name }}</h3>
    <h3>Owner: {{ owner }}</h3>
    <h3>Price: {{ price }}</h3>
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

<style>

</style>