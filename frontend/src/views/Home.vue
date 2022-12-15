<template>
  <div class="home">
    <navbar></navbar>
    udalo ci sie zalogowac, gratulacje {{username}} !
  </div>

  <MDBContainer>
    <MDBRow :cols="['1','md-2']" class="mt-2">
            <MDBCol>
                <MDBCard text="dark" bg-silver style="width: 20rem;" id="card">
                    <a v-mdb-ripple="{ color: 'light' }">
                        <MDBCardImg src="https://mdbootstrap.com/img/new/standard/nature/184.webp" style="width: 100%; height: 12vw; object-fit: cover;"  class="img-fluid zoom" top alt="..." />
                    </a>
                    <MDBCardBody>
                        <MDBCardTitle>test</MDBCardTitle>
                        <MDBCardText>
                            test opisu
                        </MDBCardText>
                        <MDBBtn tag="a" color="primary">Więcej..</MDBBtn>
                    </MDBCardBody>
                </MDBCard>
            </MDBCol>
            <MDBCol>
              <MDBCard text="dark" bg-silver style="width: 20rem;" id="card">
                  <a v-mdb-ripple="{ color: 'light' }">
                      <MDBCardImg src="https://mdbootstrap.com/img/new/standard/nature/184.webp" style="width: 100%; height: 12vw; object-fit: cover;"  class="img-fluid zoom" top alt="..." />
                  </a>
                  <MDBCardBody>
                      <MDBCardTitle>test</MDBCardTitle>
                      <MDBCardText>
                          test opisu
                      </MDBCardText>
                      <MDBBtn tag="a" color="primary">Więcej..</MDBBtn>
                  </MDBCardBody>
              </MDBCard>
          </MDBCol>
          <MDBCol>
            <MDBCard text="dark" bg-silver style="width: 20rem;" id="card">
                <a v-mdb-ripple="{ color: 'light' }">
                    <MDBCardImg src="https://mdbootstrap.com/img/new/standard/nature/184.webp" style="width: 100%; height: 12vw; object-fit: cover;"  class="img-fluid zoom" top alt="..." />
                </a>
                <MDBCardBody>
                    <MDBCardTitle>test</MDBCardTitle>
                    <MDBCardText>
                        test opisu
                    </MDBCardText>
                    <MDBBtn tag="a" color="primary">Więcej..</MDBBtn>
                </MDBCardBody>
            </MDBCard>
        </MDBCol>
        <MDBCol>
          <MDBCard text="dark" bg-silver style="width: 20rem;" id="card">
              <a v-mdb-ripple="{ color: 'light' }">
                  <MDBCardImg src="https://mdbootstrap.com/img/new/standard/nature/184.webp" style="width: 100%; height: 12vw; object-fit: cover;"  class="img-fluid zoom" top alt="..." />
              </a>
              <MDBCardBody>
                  <MDBCardTitle>test</MDBCardTitle>
                  <MDBCardText>
                      test opisu
                  </MDBCardText>
                  <MDBBtn tag="a" color="primary">Więcej..</MDBBtn>
              </MDBCardBody>
          </MDBCard>
      </MDBCol>
    </MDBRow>
</MDBContainer>

</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import Navbar from "@/components/ui/Navbar.vue";
import { MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardImg, MDBBtn, mdbRipple, MDBCol, MDBRow,MDBContainer } from "mdb-vue-ui-kit";

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
