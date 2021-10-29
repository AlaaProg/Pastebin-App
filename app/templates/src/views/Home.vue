<template>
  <div class="home">
      <b-container>
        <b-row class="justify-content-center">
          <b-col cols=12 sm=10 class="mb-2 d-flex justify-content-end">
            <b-button  variant="primary" squared size="sm" @click="textModal=true">Create New</b-button>
          </b-col>
          <b-modal @hidden="current={}" v-model="textModal" id="text-modal" size="xl" hide-footer>
            <template #modal-title v-if='!current.id'>
              Create New Text
            </template>
            <template #modal-title v-else>
              Edit {{ current.id }} Text
            </template>
            <p> link: <a href="#">{{ current.link }}</a> </p>
            <text-form @close="textModal=false" @update='current=$event' :data="current"></text-form>
          </b-modal>
          
          <b-col cols=12 sm=10 class="mb-5">
            <b-list-group class="text-start">
              <b-list-group-item v-for="text in $store.state.texts" :key="text.id">
                <small class="text-muted">{{ text.created_at }}</small>
                <p class="text-truncate">
                  {{ text.value }}
                </p>
                <a href="#" class="text-danger text-decoration-none" @click="deleteText(text.id)">delete</a>
                |
                <a href="#" class="text-primary text-decoration-none" @click="editText(text)">edit</a>
              </b-list-group-item>
            </b-list-group>
          </b-col>
        </b-row>
      </b-container>
  </div>
</template>

<script>

// @ is an alias to /src
const TextForm = () => import("../components/TextForm.vue")
export default {
  name: 'Home',
  components:{
    TextForm
  },
  data(){
    return {
      current: {},
      textModal: false
    }
  },
  methods: {
    deleteText(id) {
      this.$store.dispatch("deleteText", {id: id})
    },
    editText(data) {
      this.current = data
      this.textModal = true
    }
  },
  created() {
    this.$store.dispatch("getAllText")
  }
}
</script>
