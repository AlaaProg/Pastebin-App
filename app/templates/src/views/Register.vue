<template>
    <b-aspect :aspect="3">
        <b-container style="height: 100%">
            <b-row class="justify-content-center " style="height:100%" align-v="center">
                <b-col cols="12" sm="8" md="6" lg="4">
                    <h1> Create New Account  </h1>
                    <register-form></register-form>
                    <p class="text-start mt-3">
                        Have account ? go to <b-link to="login">login</b-link>
                    </p>
                </b-col>
            </b-row>
        </b-container>
    </b-aspect>
</template>

<script>

const RegisterForm = ()=> import("../components/RegisterForm.vue")

export default {
    components: { RegisterForm },
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
