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
                fetch('/garages/worker')
                .then(res => res.json())
                .then(res => console.log(res));

                // $.ajax({
                //     type: 'GET',
                //     contentType: 'application/json',
                //     url: `/garages/worker`,
                //     success: function (data, textStatus) {
                //         if (data.redirect) {
                //         // data.redirect contains the string URL to redirect to
                //         window.location.replace(data.redirect);
                //         } else {
                //         // data.form contains the HTML for the replacement form
                //             console.log("No redirect");
                //         }
                //     }
                // });
            }
        }
    }
</script>

<style scoped>

</style>