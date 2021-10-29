<template>

    <b-form @submit.prevent="onSubmit" ref='form' >
        <b-alert 
            variant="danger" 
            :show="showAlert"
            class="text-start">
                Incorrect username or password
        </b-alert>

        <b-form-group
            id="username"
            label="  "
        >
            <b-form-input
                id="#username"
                name="username"
                placeholder="Enter username"
                required
            ></b-form-input>
        
        </b-form-group>

        <b-form-group
            id="password"
            label="  "
        >
            <b-form-input
                id="#password"
                type="password"
                name="password"
                placeholder="Enter password"
                required
            ></b-form-input>
        </b-form-group>

        <b-button squared variant="outline-success" type="submit" class="block mt-4" :disabled='isloading'>
            <b-spinner small v-show="isloading"></b-spinner>
            Log In
        </b-button>
    </b-form>

</template>

<script>

export default {
    name: 'login-form',

    data() {
        return {
            showAlert: false,
            isloading: false
        }
    },

    methods: {
        onSubmit() {
            let fd = new FormData(this.$refs.form)

            this.showAlert = false
            this.isloading = true
            this.$store.dispatch("login", fd)
                .then( () => {
                    this.$router.push("/")
                })
                .catch( ()=> this.showAlert = true)
                .finally( ()=> this.isloading = false)
                
        }
    },
}
</script>