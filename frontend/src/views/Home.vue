<template>
  <div style="background: url(../assets/background_food.jpg);  height: 100vh;">
  <img src = "../assets/background_food.jpg" style=" position: absolute; " class="img-fluid">
  <div class="home">
    <navbar></navbar>
    udalo ci sie zalogowac, gratulacje {{username}} !
  </div>

  <MDBContainer class="text-center">
    <MDBCard class="mb-4 mt-4 bg-light">
      <MDBCardHeader><h4>Stwórz zamówienie</h4></MDBCardHeader>
      <MDBCardBody>
        <div class="row">
          <div class="col-4">
            <form @submit.prevent="searchForm">
              <MDBInput v-model="query" inputGroup :formOutline="false" wrapperClass="mb-3" placeholder="Wyszukaj danie" aria-label="Search">
                  <MDBBtn color="primary" type="submit">
                      <MDBIcon icon="search" />
                  </MDBBtn>
              </MDBInput>
            </form>
            <MDBListGroup light data-bs-spy="scroll" data-bs-target="#list-example" id="list-example" data-bs-offset="0">
              <MDBListGroupItem tag="label">
                <input class="form-check-input me-1" type="checkbox" value="" />
                Cras justo odio
              </MDBListGroupItem>
              <MDBListGroupItem tag="label">
                <input class="form-check-input me-1" type="checkbox" value="" />
                Dapibus ac facilisis in
              </MDBListGroupItem>
              <MDBListGroupItem tag="label">
                <input class="form-check-input me-1" type="checkbox" value="" />
                Morbi leo risus
              </MDBListGroupItem>
              <MDBListGroupItem tag="label">
                <input class="form-check-input me-1" type="checkbox" value="" />
                Porta ac consectetur ac
              </MDBListGroupItem>
              <MDBListGroupItem tag="label">
                <input class="form-check-input me-1" type="checkbox" value="" />
                Vestibulum at eros
              </MDBListGroupItem>
            </MDBListGroup>
          </div>
          <div class="col-5">
            opis dania
            <hr>
          </div>
          <div class="col-3">
            wybrane
            <hr>
          </div>
        </div>
        <div class="row mt-4">
          <div class="col-4">
            <select class="form-select" aria-label="Default select example">
              <option selected>Wybierz stolik</option>
              <option value="1">Stolik 1</option>
              <option value="2">Stolik 2</option>
            </select>
          </div>
          <div class="col-6"><MDBBtn color="primary">złóż zamówienie</MDBBtn></div>
          <div class="col-2"><b>do zapłaty: 12 zł</b></div>
        </div>
      </MDBCardBody>
    </MDBCard>

    <MDBCard  class="bg-light mt-5">
      <MDBCardHeader>Stoliki</MDBCardHeader>
      <MDBCardBody>
        <div class="row">
        <MDBCard class="col-md-2 bg-info me-3">
          <MDBCardBody>
            <MDBCardTitle>Stolik 1</MDBCardTitle>
            <MDBCardText>
              2 ludzi
            </MDBCardText>
          </MDBCardBody>
        </MDBCard>
        <MDBCard class="col-lg-2">
          <MDBCardBody>
            <MDBCardTitle>Stolik 2</MDBCardTitle>
            <MDBCardText>
              2 ludzi
            </MDBCardText>
          </MDBCardBody>
        </MDBCard>
      </div>
      
      </MDBCardBody>
    </MDBCard>
  </MDBContainer>
</div>
</template>

<script>

import HelloWorld from "@/components/HelloWorld.vue";
import Navbar from "@/components/ui/Navbar.vue";
import { MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardImg, MDBBtn, mdbRipple, MDBCol, MDBRow,MDBContainer,MDBCardHeader,MDBListGroup,MDBListGroupItem,MDBInput,MDBIcon } from "mdb-vue-ui-kit";

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
      MDBListGroup,
      MDBListGroupItem,
      MDBInput,
      MDBIcon,
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
