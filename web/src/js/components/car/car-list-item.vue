<template>
  <div>
    <h2>Name: {{ name }}</h2>
    <h2>Owner: {{ owner }}</h2>
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
            required: true
        }
    }
}
</script>

<style>

</style>