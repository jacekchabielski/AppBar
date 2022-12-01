<template>
    <navbar></navbar>
    <div v-if="alertMessage" class="alert alert-success alert-dismissible fade show" role="alert">
        {{ alertMessage }}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close" @click="close()"></button>
    </div>
    <MDBContainer fluid>
        <MDBRow class="mb-4">
            <MDBCol>
                <h2>Nazwa</h2>
            </MDBCol>
            <MDBCol>
                <MDBDropdown class="nav-item" v-model="dropdown1">
                    <div>
                    <MDBDropdownToggle tag="a" @click="dropdown1 = !dropdown1" class="h2 link-dark "> Kategorie </MDBDropdownToggle>
                        
                    <MDBDropdownMenu dark aria-labelledby="dropdownMenuButton" class="mt-2">
                    <MDBDropdownItem tag="button"  @click="getProductsByCategory('Wszystkie kategorie')">Wszystkie Kategorie</MDBDropdownItem>
                    <MDBDropdownItem divider />
                    <MDBDropdownItem tag="button" v-for="category in productCategories" @click="getProductsByCategory(category)">{{category}}</MDBDropdownItem>
                    </MDBDropdownMenu>
                    </div>
                </MDBDropdown>
            </MDBCol>
            <MDBCol>
                <h2>Opis</h2>
            </MDBCol>
            <MDBCol>
                <h2>Ilość</h2>
            </MDBCol>
            <MDBCol>
                <h2>Akcje</h2>
            </MDBCol>
            
        </MDBRow>

        <template v-for="(product, index) in products.products" v-bind:key="product.id">
            <MDBRow @click="collapseList[index] = !collapseList[index]" class="border-bottom pb-3">
                <MDBCol>
                    <div class="d-flex align-items-center">
                        <img v-bind:src="product.get_thumbnail" class="rounded-circle image"
                            :class="{ 'image-large': collapseList[index] }" />
                        <div class="ms-3">
                            <p class="fw-bold mb-1">{{ product.name }}</p>
                        </div>
                    </div>
                </MDBCol>
                <MDBCol class="d-flex align-items-center justify-content-center"> {{ product.Product_category_name}}</MDBCol>
                <MDBCol class="d-flex align-items-center justify-content-center" >
                    <p style="max-width: 250px;" class="fw-normal mb-1" :class="{ 'text-truncate': !collapseList[index]  }" >
                        {{ product.description }}
                    </p>
                </MDBCol>
                
                <MDBCol class=" d-flex align-items-center justify-content-center">{{ product.product_quantity }}
                </MDBCol>
                <MDBCol class=" d-flex align-items-center justify-content-center gap-1"
                    :class="{ 'align-items-start': !collapseList[index] }">
                    <MDBBtn color="link" size="sm" rounded>
                        <router-link v-bind:to="'/EditProduct' + product.get_absolute_url">Edytuj</router-link>
                    </MDBBtn>
                    <MDBBtn type="button" color="danger" size="sm" rounded @Click="setId(product.id)">
                        usuń
                    </MDBBtn>
                </MDBCol>
            </MDBRow>
        </template>
    </MDBContainer>

    <div class="modal" id="myModal" :class="{ 'show-modal': actualId }" v-show="actualId">
        <div class="modal-dialog">
            <div class="modal-content">
                <!-- Modal Header -->
                <div class="modal-header">
                    <h4 class="modal-title">Czy na pewno chcesz usunąć ?</h4>
                    <button type="button" class="btn-close" v-on:click="actualId = null"></button>
                </div>

                <!-- Modal body -->
                <div class="modal-body">usuniesz element</div>

                <!-- Modal footer -->
                <div class="modal-footer">
                    <button type="button" class="btn btn-danger" v-on:click="deleteProduct(actualId)">
                        Usuń
                    </button>
                    <button type="button" class="btn margin-left" v-on:click="actualId = null">
                        powrót
                    </button>
                </div>
            </div>
        </div>
    </div>
    

    <!--~~~~~~~~~~PAGINACJA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
    <nav v-if="products.products!=''" aria-label="pagination"  class="pagination justify-content-center" style="margin: 20px 0">
        <ul class="pagination">
            <li class="page-item" v-if="parseInt(this.$route.params.page_number) > 1">
            <a class="page-link" :href="'/ViewProduct/' + (parseInt(this.$route.params.page_number) - 1) + '/'">Poprzednia</a>
            </li>
            <li v-for="page in products.page_numbers" v-bind:class="[pageItemClass, page === parseInt(this.$route.params.page_number) ? activeClass : '',]">
            <a class="page-link" :href="'/ViewProduct/' + page + '/'">{{ page }}</a>
            </li>
            <li class="page-item" v-if="products.next_page">
            <a class="page-link" :href="'/ViewProduct/' + (parseInt(this.$route.params.page_number) + 1) + '/'">Następna</a>
            </li>
        </ul>
    </nav>
<!--~~~~~~~~~~PAGINACJA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->


  
</template>

<script>
import axios from "axios";
import Navbar from "@/components/ui/Navbar.vue";
import { ref } from "vue";
import {
    MDBPagination,
    MDBPageNav,
    MDBPageItem,
    MDBDropdown, 
    MDBDropdownToggle, 
    MDBDropdownMenu, 
    MDBDropdownItem,
    MDBCol,
    MDBRow,
    MDBContainer,
    MDBCollapse,
    MDBTable,
    MDBBtn,
    MDBBadge,
    MDBModal,
    MDBModalHeader,
    MDBModalTitle,
    MDBModalBody,
    MDBModalFooter,
    MDBAccordion,
    MDBAccordionItem,
} from "mdb-vue-ui-kit";

export default {
    components: {
        MDBPagination,
        MDBPageNav,
        MDBPageItem,
        MDBDropdown, 
        MDBDropdownToggle, 
        MDBDropdownMenu, 
        MDBDropdownItem,
        MDBCol,
        MDBRow,
        MDBContainer,
        MDBCollapse,
        MDBTable,
        MDBBtn,
        MDBBadge,
        Navbar,
        MDBModal,
        MDBModalHeader,
        MDBModalTitle,
        MDBModalBody,
        MDBModalFooter,
        MDBAccordion,
        MDBAccordionItem,
    },
    
    setup() {
        const collapse1 = ref(false);
        const dropdown1 = ref(false);
        const dropdown2 = ref(false);
        return {
            collapse1,
            dropdown1,
            dropdown2,
        };
    },
    props: {
        alert: Boolean,
    },
    computed: {
        showAlert() {
            return this.$store.getters.getAlertStatus;
        },
    },
    data() {
        return {
            products: {},
            alertMessage: null,
            actualId: "",
            collapseList: [],
            productCategories: [],
            page_size: 6,
            activeClass: "active",
            activeCategory: ''
        };
    },
    mounted() {
        //~ wywołanie metody przy zmontowaniu strony
        this.getProducts();
        console.log(this.$store.getters);
        console.log(this.showAlert);
        this.statusAlert();
        this.getProductCategory();
        
    },
    methods: {


        setId(id) {
            this.actualId = id;
            console.log(this.actualId, "dd");
        },


///////////////////////////////////// POBIERANIE WSZYSTKICH PRODUKTÓW /////////////////////////////////////////////////////////////
        async getProducts() {
            const storedCategory = localStorage.getItem('category');
            if(storedCategory) {
                this.activeCategory = storedCategory;
            } else {
                this.activeCategory = '';                
            }
            axios
                .get(`/api/v1/products/?page_number=${this.$route.params.page_number}&page_size=${this.page_size}&category=${this.activeCategory}`) //* get pobierający wszystkie produkty (które nie są usunięte)
                .then((response) => {
                    console.log(response,"respons wszystkiego");
                    this.products = response.data;
                    this.collapseList = [];
                    for (product in this.products) {
                        this.collapseList.push(false);
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
        },
/////////////////////////////////////////// POBIERANIE PRODUKTU PO WYBRANEJ KATEGORII /////////////////////////////////////////////////////////////
        async getProductsByCategory(category){
            localStorage.setItem('category', category);
            this.activeCategory = category;
            axios
                // .get(`/api/v1/products/${activeCategory}/`)
                .get(`/api/v1/products/?category=${this.activeCategory}&page_number=${this.$route.params.page_number}&page_size=${this.page_size}`)
                .then((response) => {
                    console.log(response, "respons po kategorii");
                    this.products = response.data;
                    this.$router.push({ path: '/ViewProduct/1/'});
                })
                .catch((error) => {
                    console.log(error);
                });
        },
///////////////////////////////////// USUWANIE PRODUKTU /////////////////////////////////////////////////////////////
        async deleteProduct(id) {
            console.log(id, "delete product id");
            axios
                .delete(`/api/v1/product/${id}/`, {
                    headers: {
                        Authorization: `Token ${this.$store.state.user.token}`,
                    },
                })
                .then((response) => {
                    console.log(response);
                    this.actualId = null;
                    location.reload();
                })
                .catch((error) => {
                    console.log(error);
                });
        },
///////////////////////////////////// POBIERANIE SAMEJ KATEGORII PRODUKTU /////////////////////////////////////////////////////////////
        async getProductCategory(){
            axios
                .get("/api/v1/productCategory/")
                .then((response) => {
                    console.log(response,'response z getproductcategory');
                    this.productCategories = response.data;
                    console.log(this.productCategories);
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        statusAlert() {
            if (this.showAlert) {
                this.alertMessage = this.$store.getters.getMessage;
                this.$store.commit("consumeAlert");
                console.log(this.alertMessage);
                setTimeout(() => { this.alertMessage = ""; }, 4300);
                
            }
        },
        close() {

            this.alertMessage = "";
        },
    },
};
</script>
<style>
.show-modal {
    display: block !important;
}

.image {
    width: 81px;
    height: 81px;
    transition: 0.3s all;
}

.image-large {
    width: 140px !important;
    height: 140px !important;
}
.pagination > .active > a
{
    color: white;
    background-color: #2b9788 !Important;
    border: solid 1px #2b9788 !Important;
}

.pagination > .active > a:hover
{
    background-color: #1a5f56 !Important;
    border: solid 1px #1a5f56;
}
</style>
