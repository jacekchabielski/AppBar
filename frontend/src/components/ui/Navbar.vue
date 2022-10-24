<template>

  <MDBNavbar expand="lg" dark container style="background-color: #2b9788;">
  <MDBNavbarBrand href="/" id="Logo">barApp</MDBNavbarBrand>
  
  <MDBNavbarToggler @click="collapse1 = !collapse1" target="#navbarSupportedContent">
  </MDBNavbarToggler>
  <MDBCollapse v-model="collapse1" id="navbarSupportedContent">
    <MDBNavbarNav center class="mb-2 mb-lg-0">
      <MDBNavbarItem to="#" >
   
      </MDBNavbarItem>
      <MDBNavbarItem to="#" >
    
      </MDBNavbarItem>
      <MDBNavbarItem to="#" >
 
      </MDBNavbarItem>
      <MDBNavbarNav right>
      <MDBNavbarItem>
        <!-- Navbar dropdown -->
        <MDBDropdown class="nav-item" v-model="dropdown1">
          <MDBDropdownToggle tag="a" class="nav-link" @click="dropdown1 = !dropdown1">
            <img
            src="https://mdbootstrap.com/img/Photos/Avatars/img (31).webp"
            class="rounded-circle"
            height="22"
            alt=""
            loading="lazy"
          />
            </MDBDropdownToggle>
          <MDBDropdownMenu aria-labelledby="dropdownMenuButton">
            <MDBDropdownItem href="#">Mój profil</MDBDropdownItem>
            <MDBDropdownItem href="/Logout">wyloguj</MDBDropdownItem>
          </MDBDropdownMenu>
        </MDBDropdown>
      </MDBNavbarItem>
      </MDBNavbarNav>

    </MDBNavbarNav>
    
  </MDBCollapse>
</MDBNavbar>
</template>

<script>
import {
  MDBBtn,
  MDBIcon,
  MDBNavbar,
  MDBNavbarToggler,
  MDBNavbarBrand,
  MDBNavbarNav,
  MDBNavbarItem,
  MDBCollapse,
  MDBDropdown,
  MDBDropdownToggle,
  MDBDropdownMenu,
  MDBDropdownItem
} from 'mdb-vue-ui-kit';
import { ref } from 'vue';

export default {
name: 'Navbar',
components: {
  MDBBtn,
  MDBIcon,
  MDBNavbar,
  MDBNavbarToggler,
  MDBNavbarBrand,
  MDBNavbarNav,
  MDBNavbarItem,
  MDBCollapse,
  MDBDropdown,
  MDBDropdownToggle,
  MDBDropdownMenu,
  MDBDropdownItem,

},
data(){
  return {
    user_slug: ""
  }
},

  setup() {

    const collapse1 = ref(false);   //metody aby animacje działały
    const dropdown1 = ref(false);

    return {
      collapse1,
      dropdown1
    }
    
  },
  



  
  
}

</script>

<style>
#Logo{
font-family: 'Molle', cursive;
font-weight: bold;
}
#ikona{
 transition: transform 0.5s ease-in-out;
 
}
#ikona:hover{
transform: translate(0px,5px) rotateZ(180deg);


}
</style>