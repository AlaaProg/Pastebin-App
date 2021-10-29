<template>

    <b-form @submit.prevent="onSubmit" ref='form' class="text-start">
        
        <b-form-group
            id="username"
            label="  "
        >
            <b-form-input
                id="#username"
                name="username"
                placeholder="Enter username"
                required
                :state="errors.username != null ? false : null"
            ></b-form-input>

            <b-form-invalid-feedback id="input-1-live-feedback" :state="!errors.username">
                <ul>
                    <li v-for="(err,i) in errors.username" :key="i">
                        {{ err }}
                    </li>
                </ul>
            </b-form-invalid-feedback>
        </b-form-group>

        <b-form-group
            id="firstname"
            label="  "
        >
            <b-form-input
                id="#first_name"
                name="first_name"
                placeholder="Enter first name"
                required
            ></b-form-input>
        
        </b-form-group>

        <b-form-group
            id="lastname"
            label="  "
        >
            <b-form-input
                id="#last_name"
                name="last_name"
                placeholder="Enter last name"
                required
            ></b-form-input>
        
        </b-form-group>

        <b-form-group
            id="email"
            label="  "
        >
            <b-form-input
                id="#email"
                name="email"
                type="email"
                :state="errors.email != null ? false : null"
                placeholder="Enter email"
                required
            ></b-form-input>

            <b-form-invalid-feedback id="input-1-live-feedback" :state="!errors.email" >
                <ul>
                    <li v-for="(err,i) in errors.email" :key="i">
                        {{ err }}
                    </li>
                </ul>
            </b-form-invalid-feedback>
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
                :state="errors.password != null ? false : null"
                required
            ></b-form-input>

            <b-form-invalid-feedback id="input-1-live-feedback" :state="!errors.password" >
                <ul>
                    <li v-for="(err,i) in errors.password" :key="i">
                        {{ err }}
                    </li>
                </ul>
            </b-form-invalid-feedback>
        </b-form-group>

        <b-form-group
            id="password2"
            label="  "
        >
            <b-form-input
                id="#password2"
                type="password"
                name="password2"
                :state="errors.password2 != null ? false : null"
                placeholder="Confirm password"
                required
            ></b-form-input>

            <b-form-invalid-feedback id="input-1-live-feedback" :state="!errors.password2" >
                <ul>
                    <li v-for="(err,i) in errors.password2" :key="i">
                        {{ err }}
                    </li>
                </ul>
            </b-form-invalid-feedback>
        </b-form-group>

        <b-button squared variant="outline-success" type="submit" class="block mt-4" :disabled='isloading'>
            <b-spinner small v-show="isloading"></b-spinner>
            Create Acount 
        </b-button>
    </b-form>

</template>

<script>

export default {
    name: 'register-form',
    data() {
        return {
            errors: {},
            showAlert: false,
            isloading: false
        }
    },
    methods: {
        onSubmit() {
            let fd = new FormData(this.$refs.form)

            this.showAlert = false
            this.isloading = true
            this.$store.dispatch("register", fd)
                .then( ()=> {
                    this.$router.push("login")
                    alert("Succsulfly Create Account Go To Login")
                } )
                .catch( (err)=> {
                    this.errors = err.response.data
                    this.showAlert = true
                })
                .finally( ()=> this.isloading = false)
        }
    },
}
</script>