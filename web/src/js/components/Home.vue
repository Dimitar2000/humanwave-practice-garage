<template>
    <div>
        <h1>Home</h1>
        <h2>{{ msg }}</h2>
        <router-link to="/garages">Garages</router-link>
        <button @click="redirectRequest">Redirect to Worker</button>
    </div>
</template>

<script>
    export default {
        name: "Home",
        data () {
            return {
                msg: 'Welcome to Your Appengine/Vue app the garage'
            }
        },
        
        methods: {
            redirectRequest() {
                $.ajax({
                    type: 'GET',
                    contentType: 'application/json',
                    url: `/garages/worker`
                }).then((data) => {
                    console.log(data);
                })
            }
        }
    }
</script>

<style scoped>

</style>