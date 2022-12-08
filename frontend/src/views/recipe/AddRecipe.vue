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
                                        <MDBTabItem :wrap="false" v-for="category in productCategories" :tabId="category" >{{category}}</MDBTabItem>
                                    </MDBTabNav>
                                    <MDBTabContent>
                                        
                                        <MDBTabPane v-for="product in products.products" v-bind:key="product.id" :tabId="product.Product_category_name">
                                            <MDBListGroup light >
                                                <MDBListGroupItem tag="label" class="col-lg-6 mx-auto mb-2 text-center">
                                                    <input class="form-check-input " type="checkbox" id="mySelect" name="checkbox" :value="product.id" @change="myFunction(product.id)" />
                                                        {{ product.name }}
                                                        {{product.id}}
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
import { MDBInput, MDBBtn, MDBCard, MDBCardBody, MDBTextarea, MDBFile, MDBTabs, MDBTabNav, MDBTabContent, MDBTabItem, MDBTabPane, MDBListGroup, MDBListGroupItem } from "mdb-vue-ui-kit";

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
    },
    setup() {
        const activeTabId4 = ref('ex4-1');

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
            products: {},
            collapseList: [],
            selectedProducts: []

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
            const storedCategory = localStorage.getItem('category');
                this.activeCategory = 'Wszystkie kategorie';
            axios
                .get(`/api/v1/products/?page_number=${this.page_number}&page_size=${this.page_size}&category=${this.activeCategory}`) //* get pobierający wszystkie produkty (które nie są usunięte)
                .then((response) => {
                    console.log(response, "respons wszystkiego");
                    this.products = response.data;
                    this.collapseList = [];
                    console.log(this.collapseList, 'collapselist');
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
        myFunction(id){
            var dupa = id ;
            let uniqueChars

            var checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
            this.selectedProducts = [];
            for (var checkbox of checkboxes) {
                console.log(checkbox.value + ' ');
                this.selectedProducts.push(checkbox.value);
            }
                    console.log(this.selectedProducts, "wszystkiee checkboxy");
                    console.log(uniqueChars, "bez duplikatow");
                
                }

        },
}



</script>