<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> | 
    <router-link to="/SignUp">rejestracja</router-link>
  </div>
  <router-view/>
</template>
<script>
import axios from 'axios'

  export default {
    data (){
      return {
        authenticated: false
      }
    },
    beforeCreate(){
      this.$store.commit('initializeStore') // commit uruchamia mutations tworzymy local storage
      const token = this.$store.state.user.token 
      if (token){
        axios.defaults.headers.common.Authorization = 'Token' + token 
      } else {
        axios.defaults.headers.common.Authorization = ''
      }
    }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
