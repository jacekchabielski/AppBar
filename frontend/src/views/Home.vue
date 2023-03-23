<template>
  <div style="background-color: #eee;">
    <div class="home">
      <navbar></navbar>
    </div>

    <MDBContainer class="text-center">
      
      <MDBCard class="mb-4 mt-4 bg-light">
        
        <MDBCardHeader>
          <h4>Stwórz zamówienie</h4>
        </MDBCardHeader>
        <MDBCardBody>
        <form @submit.prevent="submitForm">
          <div class="row">
            <div class="col-4">
                
              
              <MDBListGroup light data-bs-spy="scroll" data-bs-target="#list-example" id="list-example"
                data-bs-offset="0">
                <MDBListGroupItem tag="label" v-for="(recipe, index) in recipes.recipes" v-bind:key="recipe.id">
                  <div class="row">
                  <div class="col-md-8">
                    <MDBCheckbox class="form-check-input" :label="recipe.name" type="checkbox" id="mySelect"
                      name="checkbox" :value="recipe.id" :alt='recipe.name'
                      @change="myFunction(recipe.name, recipe.description)" />
                  </div>
                  <div class="col-md-4">
                    <MDBInput label="ilosc" for="typeNumber" type="number" name="Input" class="active" :id="recipe.id"
                      v-model="recipe.quantity"  />
                  </div>
                </div>
                </MDBListGroupItem>
              </MDBListGroup>
            </div>
            <div class="col-5">
              <MDBTextarea label="Uwagi do zamówienia" rows="4" v-model="textareaValue" />
              <p class="mt-4">opis dania</p> 
              <hr>
              {{description}}
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
                    <li v-for="data in selectedProducts">
                      {{ data.name }} - {{ data.quantity }} szt. - {{data.price}} zł/szt

                    </li>
                    
                  </MDBCardText>
                </MDBCardBody>
              </MDBCard>
            </div>
          </div>
          <div class="row mt-4">
            <div class="col-4">
              <select class="form-select" aria-label="Default select example" id="idStolik">
                <option selected>Brak stolika</option>
                <option value="1">Stolik 1</option>
                <option value="2">Stolik 2</option>
                <option value="3">Stolik 3</option>
                <option value="4">Stolik 4</option>
                <option value="5">Stolik 5</option>
              </select>
            </div>
            <div class="col-6">
              <MDBBtn color="primary" type="submit">złóż zamówienie</MDBBtn>
            </div>
            <div class="col-2"><b>do zapłaty: {{ doZaplaty }} zł</b></div>
          </div>
        </form>
        </MDBCardBody>
      
      </MDBCard>
   
      <MDBCard class="bg-light mt-5">
        <MDBCardHeader>Stoliki</MDBCardHeader>
        <MDBCardBody>
          <div class="row">
            <MDBCard class="col-md-2 bg-info me-3">
              <MDBCardBody>
                <MDBCardTitle>Stolik 1</MDBCardTitle>
                
              </MDBCardBody>
            </MDBCard>
            <MDBCard class="col-lg-2">
              <MDBCardBody>
                <MDBCardTitle>Stolik 2</MDBCardTitle>
                
              </MDBCardBody>
            </MDBCard>
            <MDBCard class="col-lg-2">
              <MDBCardBody>
                <MDBCardTitle>Stolik 3</MDBCardTitle>
              
              </MDBCardBody>
            </MDBCard>
            <MDBCard class="col-lg-2">
              <MDBCardBody>
                <MDBCardTitle>Stolik 4</MDBCardTitle>
                
              </MDBCardBody>
            </MDBCard>
            <MDBCard class="col-lg-2">
              <MDBCardBody>
                <MDBCardTitle>Stolik 5</MDBCardTitle>
                
              </MDBCardBody>
            </MDBCard>
            
          </div>

        </MDBCardBody>
      </MDBCard>
      
    </MDBContainer>
  </div>
</template>

<script>
import axios from "axios";
import HelloWorld from "@/components/HelloWorld.vue";
import Navbar from "@/components/ui/Navbar.vue";
import FormData from "form-data";
import { ref } from "vue";
import { MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardImg, MDBBtn, mdbRipple, MDBCol, MDBRow, MDBContainer, MDBCardHeader, MDBListGroup, MDBListGroupItem, MDBInput, MDBIcon, MDBTextarea, MDBCheckbox } from "mdb-vue-ui-kit";

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
    MDBTextarea,
    HelloWorld,
    Navbar,
  },
  data() {
    return {
      description: '',
      table: '',
      name: "",
      username: '',
      recipes: {},
      doZaplaty: 0,
      selectedCheckboxes: [],       //zaznaczone produkty - id
      selectedProducts: [], //ZAWIERA WSZYSTKIE INFO O ZAZNACZONYCH RZECZACH
      selectedProductsQuantity: [],
      selectedProductsPrice: [],
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

    myFunction(name, descrip) {
      var nazwa = name;
      var descr = descrip;
      console.log(descr, 'descr');
      this.description = descr;
      //console.log(description, "opis");
      this.doZaplaty = 0;
      var checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
      this.selectedProducts = [];
      for (var checkbox of checkboxes) {
        console.log(checkbox.value, 'wartosc checkboxa');              //tu sa idki zaznaczanych rzeczy
        this.selectedCheckboxes.push(checkbox.value);            //tablica z id zaznaczonych rzeczy
        for(let i = 0; i < this.recipes.recipes.length; i++){
          
          if(this.recipes.recipes[i].id == checkbox.value){
            console.log(this.recipes.recipes[i].name, "nazwa zaznaczonej rzeczy");
            let objectToPush = {
            'id': this.recipes.recipes[i].id,
            'name': this.recipes.recipes[i].name,
            'quantity': this.recipes.recipes[i].quantity,
            'price': this.recipes.recipes[i].price,
          }
          this.doZaplaty += this.recipes.recipes[i].price * this.recipes.recipes[i].quantity;
          this.selectedProducts.push(objectToPush);
          }
        }
        
      }
      //console.log(this.selectedProductsNames, "nazwy zaznaczonych");

    },
                                                                  //wysylanie zamowienia
    submitForm() {
      //console.log('DZIALA ????');
      //name/table/price/status
            let formData = new FormData();
            //formData.append('name', 'cosnasztywno1');
            formData.append('price', this.doZaplaty);
            formData.append('status', 'Oczekuje');
            var select = document.getElementById('idStolik');
            var selectTableValue = select.options[select.selectedIndex].value ;
            formData.append('table', selectTableValue);
            axios
              .post("/api/v1/add_order/", formData, {
                    headers: {
                        Authorization: `Token ${this.$store.state.user.token}`,
                        
                    }
                })
                .then((response) => {
                  console.log(response, 'DODANO ZAMÓWIENIE');
                  
                  //TU PISZEMY WYSYLANIE TEGO DALEJ LEEETS GOO

                  for (let i = 0; i < this.selectedProducts.length; i++){
                        let formData = new FormData();
                        console.log(this.selectedProducts[i].id ,'product_id');
                        formData.append('id', this.selectedProducts[i].id);
                        formData.append('name',this.selectedProducts[i].name)
                        formData.append('quantity',this.selectedProducts[i].quantity);
                        //console.table(formData, 'jedno_do_wysłania');
                        axios
                            .post("/api/v1/add_recipe_to_order/", formData, {
                    headers: {
                        Authorization: `Token ${this.$store.state.user.token}`,
                        
                    }
                            })
                            .then((response) => {
                                console.log(response, 'Przepisy dodane do zamowienia');
                                //this.$router.push({ path: '/ViewRecipe/1/'});
                            })
                            .catch((error) => {
                                console.log(error);
                            })
                        formData.forEach((value,key) => { console.log(key+" "+value)});
                    }

                    //KONIEC KOPIOWANIA

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
