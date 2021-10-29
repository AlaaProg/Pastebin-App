<template>
    <b-aspect :aspect="4">
        <b-container style="height: 100%">
            <b-row class="justify-content-center " style="height:100%" align-v="center">
                <b-col cols="12" sm="8" md="6" lg="4">
                    <h1> Login </h1>
                    <login-form></login-form>
                    <p class="text-start mt-3">
                        Create new Account <b-link to="register">Register</b-link>
                    </p>
                </b-col>
            </b-row>
        </b-container>
    </b-aspect>
</template>

<script>

const LoginForm = ()=> import("../components/LoginForm.vue")

export default {
    components: { LoginForm },
    name: 'Login',

    data() {
        return {
        }
    }
}
</script>

<style>
    .block{
        width: 100% !important
    }
</style>
