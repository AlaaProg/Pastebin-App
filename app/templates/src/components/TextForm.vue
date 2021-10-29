<template>
    <b-form @submit.prevent="onSubmit" ref='form' >

        <b-form-group
            id="username"
            label=" "
        >
            <b-form-textarea
                id="value"
                name="value"
                v-model="value"
                placeholder="Enter something..."
                rows="10"
                max-rows="8"
            ></b-form-textarea>
        </b-form-group>
        
        <b-button squared variant="outline-success"  type="submit" class="block mt-4" :disabled='isloading'>
            <b-spinner small v-show="isloading"></b-spinner>
            Save
        </b-button>
    </b-form>

</template>

<script>

export default {
    name: 'login-form',
    props: ["data"],
    data() {
        return {
            showAlert: false,
            isloading: false,
            value: this.data.value
        }
    },

    methods: {
        onSubmit() {
            
            this.isloading = true
            if (this.data.id) {
                this.$store.dispatch("saveText", {value: this.value, id: this.data.id})
                .then((data) => {
                    
                    alert("successfuly update text")
                })
                .finally( ()=> this.isloading = false)
            } else{ 
                this.$store.dispatch("createText", {value: this.value})
                .then(() => {
                    this.$refs.form.reset()
                    this.$emit("close")
                })
                .finally( ()=> this.isloading = false)
            }
            
                
        }
    },
}
</script>