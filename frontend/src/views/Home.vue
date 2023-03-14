<template>
  <div style="background: url(../assets/background_food.jpg);  height: 100vh;">
    <img src="../assets/background_food.jpg" style=" position: absolute; " class="img-fluid">
    <div class="home">
      <navbar></navbar>
      udalo ci sie zalogowac, gratulacje {{ username }} !
    </div>

    <MDBContainer class="text-center">
      <MDBCard class="mb-4 mt-4 bg-light">
        <MDBCardHeader>
          <h4>Stwórz zamówienie</h4>
        </MDBCardHeader>
        <MDBCardBody>
          <div class="row">
            <div class="col-4">
              <form @submit.prevent="searchForm">
                <MDBInput v-model="query" inputGroup :formOutline="false" wrapperClass="mb-3" placeholder="Wyszukaj danie"
                  aria-label="Search">
                  <MDBBtn color="primary" type="submit">
                    <MDBIcon icon="search" />
                  </MDBBtn>
                </MDBInput>
              </form>
              <MDBListGroup light data-bs-spy="scroll" data-bs-target="#list-example" id="list-example"
                data-bs-offset="0">
                <MDBListGroupItem tag="label" v-for="(recipe, index) in recipes.recipes" v-bind:key="recipe.id">
                  <div class="col-md-8">
                    <MDBCheckbox class="form-check-input" :label="recipe.name" type="checkbox" id="mySelect"
                      name="checkbox" :value="recipe.id" :alt='recipe.name'
                      @change="myFunction(recipe.name, recipe.id)" />
                  </div>
                  <div class="col-md-4">
                    <MDBInput label="ilosc" for="typeNumber" type="number" name="Input" class="active" :id="recipe.id"
                      v-model="recipe.quantity" />
                  </div>
                </MDBListGroupItem>
              </MDBListGroup>
            </div>
            <div class="col-5">
              opis dania
              <hr>
            </div>
            <div class="col-3">
              Wybrane dania
              <hr>
              <MDBCard class="border pt-2 mt-3">
                <MDBCardBody>
                  <MDBCardText>
                    <li v-for="recipe in ProductsSelectedObject">
                      {{ recipe.name }} - {{ recipe.quantity }} szt. - {{recipe.price}} zł/szt
                    </li>
                  </MDBCardText>
                </MDBCardBody>
              </MDBCard>
            </div>
          </div>
          <div class="row mt-4">
            <div class="col-4">
              <select class="form-select" aria-label="Default select example" id="idCategory">
                <option selected>Brak stolika</option>
                <option value="1">Stolik 1</option>
                <option value="2">Stolik 2</option>
              </select>
            </div>
            <div class="col-6">
              <MDBBtn color="primary">złóż zamówienie</MDBBtn>
            </div>
            <div class="col-2"><b>do zapłaty: {{ doZaplaty }} zł</b></div>
          </div>
        </MDBCardBody>
      </MDBCard>

      <MDBCard class="bg-light mt-5">
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
import axios from 'axios'
import HelloWorld from "@/components/HelloWorld.vue";
import Navbar from "@/components/ui/Navbar.vue";
import { MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardImg, MDBBtn, mdbRipple, MDBCol, MDBRow, MDBContainer, MDBCardHeader, MDBListGroup, MDBListGroupItem, MDBInput, MDBIcon, MDBCheckbox } from "mdb-vue-ui-kit";

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
    MDBCheckbox,
    HelloWorld,
    Navbar,
  },
  data() {
    return {
      table: '',
      name: "",
      username: '',
      recipes: {},
      doZaplaty: 0,
      selectedProducts: [],       //zaznaczone produkty - id
      selectedProductsNames: [], //nazwy zaaznaczonych produktów
      ProductsSelectedObject: [],
    }
  },
  directives: {
    mdbRipple
  },
  mounted() {
    document.title = 'strona glowna'

  },
  methods: {
    async getRecipes() {
      axios
        .get('/api/v1/recipes/')
        .then((response) => {
          console.log(response, "przepisy wszystkie");
          this.recipes = response.data;
          for (let i = 0; i < response.data.recipes.length; i++) {
            this.recipe_quantity.push(0);
          }
          console.log(this.recipe_quantity, "to jest tablica z zerami");
        })
        .catch((error) => {
          console.log(error);
        })
    },

    myFunction(name) {
      let uniqueChars;
      var checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
      this.selectedProducts = [];
      this.selectedProductsNames = [];
      for (var checkbox of checkboxes) {
        console.log(checkbox.value + ' ');
        this.selectedProducts.push(parseInt(checkbox.value));
      }
      this.doZaplaty = 0;
      console.log(this.recipes, 'AUUUUUUU');
      this.ProductsSelectedObject = [];
      for (var number in this.recipes.recipes) {
        if (this.selectedProducts.includes(this.recipes.recipes[number].id)) {
          if (!this.recipes.recipes[number].quantity) {
            this.recipes.recipes[number].quantity = 1;
          }
          //console.log(this.products.products[number], 'dupa');
          let objectToPush = {
            'id': this.recipes.recipes[number].id,
            'name': this.recipes.recipes[number].name,
            'quantity': this.recipes.recipes[number].quantity,
            'price': this.recipes.recipes[number].price,
            'fullPrice': this.recipes.recipes[number].price * this.recipes.recipes[number].quantity,
          }
          this.ProductsSelectedObject.push(objectToPush);
          
          this.doZaplaty += this.ProductsSelectedObject[number].fullPrice;
          
          console.log(this.ProductsSelectedObject[number].price, "price");
          //ProductsSelectedObject.push(this.products.products[number].id, this.products.products[number].name );

        } else {
          this.recipes.recipes[number].quantity = 0;
        }
      }



      console.log(this.selectedProducts, "wszystkiee checkboxy");
      console.log(this.ProductsSelectedObject, 'obiekt zaznaczonych rzeczy');

    },

    submitForm() {
      let formData = new FormData();
      var select = document.getElementById('idCategory');
      axios
        .post("/api/v1/add_recipe/", formData, {
          headers: {
            Authorization: `Token ${this.$store.state.user.token}`,
          }
        })
        .then((response) => {
          console.log(response);
          //this.ProductsSelectedObject;
          for (let i = 0; i < this.ProductsSelectedObject.length; i++) {
            let formData = new FormData();
            console.log(this.ProductsSelectedObject[i].id, 'recipe_id');
            formData.append('id', this.ProductsSelectedObject[i].id);
            formData.append('quantity', this.ProductsSelectedObject[i].quantity);
            //console.table(formData, 'jedno_do_wysłania');
            axios
              .post("/api/v1/add_product_to_recipe/", formData, {
                headers: {
                  Authorization: `Token ${this.$store.state.user.token}`,

                }
              })
              .then((response) => {
                console.log(response, 'produkt_dodany do przepisu');
                this.$router.push({ path: '/ViewRecipe/1/' });
              })
              .catch((error) => {
                console.log(error);
              })
            formData.forEach((value, key) => { console.log(key + " " + value) });
          }

        })
        .catch((error) => {
          console.log(error);
        })
    },
  },
  beforeMount() {
    this.username = this.getUsername;
    this.getRecipes();
  },
  computed: {
    getUsername() {
      return this.$store.state.user.username;
    }
  }
};
</script>
