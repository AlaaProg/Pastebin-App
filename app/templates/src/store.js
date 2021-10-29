import Vue from "vue";
import Vuex from "vuex";
import axios from "./axios"
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: null,
    isLogin: null,
    texts: []
  },
  mutations: {
    setData(state, data) {

        state.texts = data.results
    },
    addToData(state, data) {

        state.texts.push(data)
    },
    removeData(state, id) {

        state.texts = state.texts.filter( it => it.id != id)
    },
    updateData(state, data) {
        
        state.texts = state.texts.map(it => it.id == data.id ? data : it)
    },
    setUser(state, user) {
        state.user = user;
        state.isLogin = true
    },
    setToken(state, token) {

        localStorage.setItem("auth_token", token)
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    },
    destroyToken(state) {

        localStorage.removeItem("auth_token")
        axios.defaults.headers.common['Authorization'] = null;
        state.isLogin = false
    }
  },
  actions: {
    logout({commit}) {
        commit("destroyToken")
    },
    user({commit}) {
        return axios.get("me/")
            .then( ({data}) => {

                commit("setUser", data)
                return data
            }) 
    },
    login({commit}, formData)  {
        return axios.post("login/", formData)
            .then( ({data}) => {

                commit("setToken", data.access)
            }) 
    },
    register({commit}, formData)  {

        return axios.post("register/", formData)
    },
    getAllText({commit}) {
        return axios.get("text/")
            .then( ({data}) => {

                commit("setData", data)
                return data
            }) 
    },
    createText({commit}, data) {

        return axios.post("text/", data)
            .then(({data})=>{

                commit("addToData", data)
            })
    },
    deleteText({commit}, data) {

        return axios.delete("text/"+data.id, data)
            .then( () => {

                commit("removeData", data.id)
            })
    },
    saveText({commit}, data) {

        return axios.put(`text/${data.id}/`, data)
            .then( ({data}) => {

                commit("updateData", data)
                return data
            })
    },

    getText({commit}, hash) {

        return axios.get(`text/link/${hash}`)
    },
  },
});