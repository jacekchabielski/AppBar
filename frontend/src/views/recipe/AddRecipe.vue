<template>
    <navbar></navbar>
    <div class="container">


        <MDBCard class="center-block">

            <MDBCardBody>
                <form @submit.prevent="submitForm">
                    <div class="row">
                        <div class="col-md-8">
                            <MDBInput type="text" label="nazwa" id="name" wrapperClass="mb-4" v-model="name" required />

                            <MDBTextarea label="opis" id="description" wrapperClass="mb-4" v-model="description"
                                rows="4" required />

                            <MDBRow class="card border mx-auto ">
                                wybierz produkty
                                <hr>
                                <MDBTabs v-model="activeTabId4" vertical>
                                    <MDBTabNav tabsClasses="mb-3 text-center">
                                        <MDBTabItem :wrap="false" v-for="category in productCategories"
                                            :tabId="category">{{ category }}</MDBTabItem>
                                    </MDBTabNav>
                                    <MDBTabContent>

                                        <MDBTabPane v-for="product in products.products" v-bind:key="product.id"
                                            :tabId="product.Product_category_name">
                                            <MDBListGroup light>
                                                <MDBListGroupItem tag="label" class="col-lg-7 mx-auto mb-2 text-center">
                                                    <div class="row">
                                                        <div class="col-md-8">
                                                            <MDBCheckbox class="form-check-input" :label="product.name"
                                                                type="checkbox" id="mySelect" name="checkbox"
                                                                :value="product.id" :alt='product.name' @change="myFunction(product.name, product.id)" />
                                                        </div>
                                                        <div class="col-md-4">
                                                            <MDBInput label="ilosc" for="typeNumber" type="number" name="Input" class="active" :id="product.id"
                                                            v-model="product.quantity"/>
                                                        </div>
                                                    </div>


                                                </MDBListGroupItem>
                                            </MDBListGroup>
                                        </MDBTabPane>
                                    </MDBTabContent>

                                </MDBTabs>
                            </MDBRow>

                            <p>wybierz kategorie dania</p>

                            <select class="form-select mb-4" id="idCategory" aria-label="Default select example"
                                required>
                                <option v-for="recipeCategory in recipeCategories" v-bind:key="recipeCategory.id"
                                    :value="recipeCategory.id">{{ recipeCategory }}</option>
                            </select>


                            <div class="col-md-4">
                                <MDBInput type="number" label="cena" id="price" wrapperClass="mb-4" v-model="price"
                                    required />
                            </div>
                        </div>




                        <div class="col-md-4">
                            <div v-if="imagePreview.length === 0">
                                <img src="https://mdbootstrap.com/img/Photos/Others/placeholder-avatar.jpg"
                                    class="rounded-circle" alt="example placeholder" style="width: 200px;" />
                            </div>
                            <div v-if="imagePreview.length > 0">
                                <img :src="imagePreview" alt="zdjecie" class="rounded-circle" style="width:200px;">
                            </div>
                            <div>
                                <div class="btn btn-primary btn-rounded">
                                    <MDBFile class="form-control d-none" label="zdjecie"
                                        @change="handleFileUpload($event)" id="image" accept=".jpg,.jpeg,.png" />
                                </div>
                            </div>

                            <MDBCard class="border pt-2 mt-3">
                                <MDBCardBody>
                                    <MDBCardTitle>Wybrane Produkty:
                                        <hr>
                                    </MDBCardTitle>
                                    <MDBCardText>
                                        <li v-for="product in ProductsSelectedObject">
                                            {{ product.name }} - {{ product.quantity }} szt.
                                          </li>
                                          
                                    </MDBCardText>
                                </MDBCardBody>
                            </MDBCard>
                        </div>

                    </div>
                    <div class="row justify-content-center">
                        <div class="col-md-2 center mt-2">
                            <p id="demo"></p>
                            <MDBBtn color="primary" block type="submit"> Dodaj </MDBBtn>
                        </div>


                    </div>

                </form>
            </MDBCardBody>
        </MDBCard>
    </div>
</template>

<script>
import axios from "axios";
import Navbar from "@/components/ui/Navbar.vue";
import { ref } from "vue";
import { MDBInput, MDBBtn, MDBCard, MDBCardBody, MDBTextarea, MDBFile, MDBTabs, MDBTabNav, MDBTabContent, MDBTabItem, MDBTabPane, MDBListGroup, MDBListGroupItem, MDBCheckbox, MDBTable, MDBCardTitle } from "mdb-vue-ui-kit";

export default {
    components: {
        MDBFile,
        MDBTextarea,
        MDBCard,
        MDBCardBody,
        MDBInput,
        MDBBtn,
        Navbar,
        MDBTabs,
        MDBTabNav,
        MDBTabContent,
        MDBTabItem,
        MDBTabPane,
        MDBListGroup,
        MDBListGroupItem,
        MDBCheckbox,
        MDBTable,
        MDBCardTitle
    },
    setup() {
        const activeTabId4 = ref('Produkty zbożowe');

        return {
            activeTabId4,
        };
    },
    data() {
        return {
            name: "",
            description: "",
            token: "",
            image: "",
            price: "",
            imagePreview: "",
            alert: false,
            recipe_id: 0,
            notification: "",
            recipeCategories: [],
            productCategories: [],
            page_number: 1,
            page_size: 12,
            empty_category: '',
            products: {},       //wszystkie produkty object
            collapseList: [],
            selectedProducts: [],       //zaznaczone produkty - id
            selectedProductsNames: [], //nazwy zaaznaczonych produktów
            ProductsSelectedObject : [],
            default_number: 0

        }
    },
    mounted() {
        this.getProducts();
        this.getProductCategory();
        this.getRecipeCategory();



    },
    computed: {
        getToken() {
            return this.$store.state.token;

        },

    },
    methods: {                                                                          //POBIERANIE WSZYSTKICH PRODUKTOW
        async getProducts() {


            axios
                .get(`/api/v1/products/all/`) //* get pobierający wszystkie produkty (które nie są usunięte)
                .then((response) => {
                    console.log(response, "respons wszystkiego");
                    this.products = response.data;
                    this.products.products.forEach((product) => {
                        product.quantity = 0;
                    })
                    console.log(this.products.products, "response wszystkiego z quantity");

                    //this.collapseList = [];
                    //console.log(this.collapseList, 'collapselist');
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        // POBIERANIE KATEGORII PRODUKTU
        async getProductCategory() {
            axios
                .get("/api/v1/productCategory/")
                .then((response) => {
                    this.productCategories = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        // POBIERANIE KATEGORII PRZEPISU
        async getRecipeCategory() {
            axios
                .get("/api/v1/recipeCategory/")
                .then((response) => {
                    console.log(response, 'response z getrecipecategory');
                    this.recipeCategories = response.data;
                    console.log(this.recipeCategories);
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        //FUNKCJA SPRAWDZANIE CO JEST ZAZNACZONE I WRZUCA DO TABLICY
        myFunction(name) {
            let uniqueChars ;
            var checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
            this.selectedProducts = [];
            this.selectedProductsNames = [];
            for (var checkbox of checkboxes) {
                console.log(checkbox.value + ' ');
                this.selectedProducts.push(parseInt(checkbox.value));         
            }
            console.log(this.products, 'AUUUUUUU'); 
            this.ProductsSelectedObject = [];
            for(var number in this.products.products){
                if (this.selectedProducts.includes(this.products.products[number].id)) {
                    if (!this.products.products[number].quantity) {
                        this.products.products[number].quantity = 1;
                    }
                    console.log(this.products.products[number], 'dupa');
                    let objectToPush = {
                        'id': this.products.products[number].id,
                        'name': this.products.products[number].name,
                        'quantity': this.products.products[number].quantity
                    }
                    this.ProductsSelectedObject.push(objectToPush);
                    //ProductsSelectedObject.push(this.products.products[number].id, this.products.products[number].name );
                
                } else {
                    this.products.products[number].quantity = 0;
                }
                }
                
            
        
            console.log(this.selectedProducts, "wszystkiee checkboxy");
            console.log(this.ProductsSelectedObject, 'obiekt zaznaczonych rzeczy');

        },


        handleFileUpload(event) {
            var input = event.target;
            if (input.files && input.files[0]) { //! jesli mamy plik
                var reader = new FileReader();
                reader.onload = (e) => {
                    this.imagePreview = e.target.result;
                };
                reader.readAsDataURL(input.files[0]); //base 64

            }
            this.image = event.target.files[0];
        },

    },
}



</script>