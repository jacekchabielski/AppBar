<template>
  <div class="home">
    udalo ci sie zalogowac, gratulacje !

    <router-link to="/Logout" class="btn btn-primary">wyloguj</router-link>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
</script>
