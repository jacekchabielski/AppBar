<template>
  <div class="home">
    <navbar></navbar>
    udalo ci sie zalogowac, gratulacje {{username}} !
  </div>

  <MDBContainer fluid>
    <MDBCard>
      <MDBCardHeader>Stoliki</MDBCardHeader>
      <MDBCardBody>
        <div class="row">
        <MDBCard class="col-lg-2 bg-info">
          <MDBCardBody>
            <MDBCardTitle>Stolik 1</MDBCardTitle>
            <MDBCardText>
              2 ludzi
            </MDBCardText>
          </MDBCardBody>
        </MDBCard>
        <MDBCard class="col-lg-2">
          <MDBCardBody>
            <MDBCardTitle>Stolik 1</MDBCardTitle>
            <MDBCardText>
              2 ludzi
            </MDBCardText>
          </MDBCardBody>
        </MDBCard>
      </div>
      </MDBCardBody>
    </MDBCard>
  </MDBContainer>

</template>

<script>

import HelloWorld from "@/components/HelloWorld.vue";
import Navbar from "@/components/ui/Navbar.vue";
import { MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardImg, MDBBtn, mdbRipple, MDBCol, MDBRow,MDBContainer,MDBCardHeader } from "mdb-vue-ui-kit";

export default {
  name: "Home",
  components: {
      MDBCard,
      MDBCardBody,
      MDBCardTitle,
      MDBCardText,
      MDBCardImg,
      MDBBtn,
      MDBCol,
      MDBRow,
      MDBContainer,
      MDBCardHeader,
      HelloWorld,
      Navbar,
    },
  data() {
    return {
      username: '',
    }
  },
  directives: {
      mdbRipple
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
