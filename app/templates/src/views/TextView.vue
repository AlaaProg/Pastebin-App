<template>
    <b-row class="justify-content-center mt-5">
        <b-col cols=8>
            <h5 class="text-break">
                {{ value }}
            </h5>
        </b-col>
    </b-row>
</template>


<script>
export default {
    

    data() {
        return {
            value: ""
        }
    },
    created() {
        console.log(this.$route.params)
        this.$store.dispatch("getText", this.$route.params.hash)
            .then( ({data})=>{
                this.value = data.text
            })
    },
}
</script>