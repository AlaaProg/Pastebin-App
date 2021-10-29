<template>
  <div id="app">
    <div id="nav">
      <template v-if="$store.state.isLogin">
        <router-link to="/" >Home</router-link> |
        <a @click="logout" href="#">logout</a>
      </template>
      <template v-else>
        <router-link to="/login" >Login</router-link> |
        <router-link to="/register" v>Register</router-link> 
      </template>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  methods: {
    logout() {

      this.$store.dispatch("logout")
      this.$router.push("login")
    }
  },
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
