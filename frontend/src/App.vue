<template>

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
@import '~@/../mdb/scss/index.free.scss';

@import '~mdb-ui-kit/css/mdb.min.css';
#app {
  font-family: Roboto, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  //text-align: center;
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
