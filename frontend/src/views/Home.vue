<template>
  <div class="home">
    <navbar></navbar>
    udalo ci sie zalogowac, gratulacje {{username}} !
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import Navbar from "@/components/ui/Navbar.vue";
export default {
  data() {
    return {
      username: '',
    }
  },
  name: "Home",
  components: {
    HelloWorld,
    Navbar,
  },
  mounted() {
    document.title = 'strona glowna'
    
  },
  beforeMount(){
    this.username = this.getUsername;
  },
  computed: {
    getUsername(){
      return this.$store.state.user.username;
    }
  }
};
</script>
