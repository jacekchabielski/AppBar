<template>

  <MDBNavbar expand="lg" dark container style="background-color: #2b9788;">
    <MDBNavbarBrand href="/" id="Logo">barApp</MDBNavbarBrand>

    <MDBNavbarToggler @click="collapse1 = !collapse1" target="#navbarSupportedContent">
    </MDBNavbarToggler>
    <MDBCollapse v-model="collapse1" id="navbarSupportedContent">
      <MDBNavbarNav center class="mb-2 mb-lg-0">

        <MDBNavbarItem>
          <!-- Navbar dropdown produkty -->
          <MDBDropdown class="nav-item" v-model="dropdown3">
            <MDBDropdownToggle tag="a" class="nav-link" @click="dropdown3 = !dropdown3">
              <i class="fas fa-carrot"></i> Produkty
            </MDBDropdownToggle>
            <MDBDropdownMenu aria-labelledby="dropdownMenuButton">
              <MDBDropdownItem href="/addProduct"><i class="fas fa-plus"></i> Dodaj produkt</MDBDropdownItem>

              <MDBDropdownItem href="/ViewProduct/1/"><i class="fas fa-eye"></i> Wyswietl produkty</MDBDropdownItem>
            </MDBDropdownMenu>
          </MDBDropdown>
        </MDBNavbarItem>
        <MDBNavbarItem>
          <!-- Navbar dropdown przepis -->
          <MDBDropdown class="nav-item" v-model="dropdown2">
            <MDBDropdownToggle tag="a" class="nav-link" @click="dropdown2 = !dropdown2">
              <i class="fas fa-book"></i> Przepisy
            </MDBDropdownToggle>
            <MDBDropdownMenu aria-labelledby="dropdownMenuButton">
              <MDBDropdownItem href="/AddRecipe"><i class="fas fa-plus"></i> Dodaj przepis</MDBDropdownItem>
              <MDBDropdownItem href="/ViewRecipe/1/"><i class="fas fa-eye"></i> Wyświetl przepisy</MDBDropdownItem>
            </MDBDropdownMenu>
          </MDBDropdown>
        </MDBNavbarItem>
        <MDBNavbarItem href="/ViewUser">pracownicy</MDBNavbarItem>
        <MDBNavbarNav right>
          <MDBNavbarItem>
            <!-- Navbar dropdown -->
            <MDBDropdown class="nav-item" v-model="dropdown1">
              <MDBDropdownToggle tag="a" class="nav-link" @click="dropdown1 = !dropdown1">
                <i v-if="user.get_image == '' " class="fas fa-user-alt fa-2xl"></i>
                <img  :src="user.get_image" class="rounded-circle" height="26"
                  alt="" loading="lazy" />
                <strong class="ms-2"></strong>
              </MDBDropdownToggle>

              <MDBDropdownMenu aria-labelledby="dropdownMenuButton">
                <MDBDropdownItem header href="#">Witaj, {{ username }}</MDBDropdownItem>
                <hr>
                <MDBDropdownItem href="/UserProfile"><i class="fas fa-user-alt"></i> Mój profil</MDBDropdownItem>

                <MDBDropdownItem href="/Logout"><i class="fas fa-sign-out-alt"></i> wyloguj się</MDBDropdownItem>
              </MDBDropdownMenu>
            </MDBDropdown>
          </MDBNavbarItem>
        </MDBNavbarNav>

      </MDBNavbarNav>

    </MDBCollapse>
  </MDBNavbar>
</template>

<script>
import axios from "axios";
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
  data() {
    return {
      user: {},
      id: "",
      username: "",
      user_slug: ""
    }
  },

  setup() {

    const collapse1 = ref(false);   //metody aby animacje działały
    const dropdown1 = ref(false);
    const dropdown2 = ref(false);
    const dropdown3 = ref(false);

    return {
      collapse1,
      dropdown1,
      dropdown2,
      dropdown3,
    }

  },
  beforeMount() {
    this.username = this.getUsername;

  },
  mounted() {
    this.id = this.getId;
    this.getUser();
  },
  computed: {
    getUsername() {
      return this.$store.state.user.username;
    },
    getId() {
      return this.$store.state.user.id;
    }
  },
  methods: {
    getUser() {
      axios
        .get(`/api/v1/single_profile/${this.id}/`, {
          //params: {id: product_id},
          headers: {
            Authorization: `Token ${this.$store.state.user.token}`
          }
        })
        .then((response) => {
                    this.user = response.data;
                    console.log(response.data, 'respons wszystiego od usera');
                })
                .catch((error) => {
                    console.log(error);
                })
    },
  }


}

</script>

<style>
#Logo {
  font-family: 'Molle', cursive;
  font-weight: bold;
}

#ikona {
  transition: transform 0.5s ease-in-out;

}

#ikona:hover {
  transform: translate(0px, 5px) rotateZ(180deg);


}
</style>