<template>
    <navbar></navbar>
    <div v-if="alertMessage" class="alert alert-success alert-dismissible fade show" role="alert">
        {{ alertMessage }}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close" @click="close()"></button>
    </div>
    
    <MDBContainer fluid style="font-family: 'Molle', cursive;" >
        <MDBRow  class="mb-4 mt-2 col-md-12">
            <MDBCol class="col-md-10">
                <MDBDropdown class="nav-item" v-model="dropdown1">
                    <div>
                        <MDBDropdownToggle tag="a" @click="dropdown1 = !dropdown1" class="h2 link-dark "> Kategorie
                        </MDBDropdownToggle>

                        <MDBDropdownMenu dark aria-labelledby="dropdownMenuButton" class="mt-2">
                            <MDBDropdownItem tag="button" @click="getRecipesByCategory('Wszystkie kategorie')">Wszystkie Kategorie</MDBDropdownItem>
                            <MDBDropdownItem divider />
                            <MDBDropdownItem tag="button" v-for="category in recipeCategories"
                                @click="getRecipesByCategory(category)">{{ category }}</MDBDropdownItem>
                        </MDBDropdownMenu>
                    </div>
                </MDBDropdown>
            </MDBCol>
            <MDBCol class="col-md-2">
                <form @submit.prevent="searchForm">
                    <MDBInput v-model="query" inputGroup :formOutline="false" wrapperClass="mb-3" placeholder="Wyszukaj produkt" aria-label="Search">
                        <MDBBtn color="primary" type="submit">
                            <MDBIcon icon="search" />
                        </MDBBtn>
                    </MDBInput>
                </form>
            </MDBCol>
        </MDBRow>
        <MDBContainer>
            <h2 v-if="empty" class="text-danger">nie znaleziono szukanych przepisów</h2>
            <MDBRow :cols="['1','md-3']" class="g-4">
                
                <template v-for="(recipe, index) in recipes.recipes" v-bind:key="recipe.id">
                    
                
                
                    <!--  KARTA  -->
                
                    <MDBCol>
                        <MDBCard text="dark" bg-silver style="width: 20rem;" id="card">
                            <a v-mdb-ripple="{ color: 'light' }">
                                <MDBCardImg v-bind:src="recipe.get_thumbnail" style="width: 100%; height: 12vw; object-fit: cover;"  class="img-fluid zoom" top alt="..." />
                            </a>
                            <MDBCardBody>
                                <MDBCardTitle>{{ recipe.name }}</MDBCardTitle>
                                <MDBCardText>
                                    {{ recipe.description }}
                                </MDBCardText>
                                <MDBBtn tag="a" :href="'/ViewRecipeDetails' + recipe.get_absolute_url" color="primary">Więcej..</MDBBtn>
                            </MDBCardBody>
                        </MDBCard>
                    </MDBCol>
                
                </template>
            </MDBRow>
        </MDBContainer>
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
                    <button type="button" class="btn btn-danger">
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
    <nav v-if="recipes.recipes != ''" aria-label="pagination" class="pagination justify-content-center"
        style="margin: 20px 0; font-family: 'Molle', cursive;" >
        <ul class="pagination">
            <li class="page-item" v-if="parseInt(this.$route.params.page_number) > 1">
                <a class="page-link"
                    :href="'/ViewRecipe/' + (parseInt(this.$route.params.page_number) - 1) + '/'">Poprzednia</a>
            </li>
            <li v-for="page in recipes.page_numbers"
                v-bind:class="[pageItemClass, page === parseInt(this.$route.params.page_number) ? activeClass : '',]">
                <a class="page-link" :href="'/ViewRecipe/' + page + '/'">{{ page }}</a>
            </li>
            <li class="page-item" v-if="recipes.next_page">
                <a class="page-link"
                    :href="'/ViewRecipe/' + (parseInt(this.$route.params.page_number) + 1) + '/'">Następna</a>
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
    MDBCard,
    MDBCardBody,
    MDBCardTitle,
    MDBCardText,
    MDBCardImg,
    mdbRipple,
    MDBInput,
    MDBIcon,

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
        MDBCard,
        MDBCardBody,
        MDBCardTitle,
        MDBCardText,
        MDBCardImg,
        MDBInput,
        MDBIcon

    },
    directives: {
        mdbRipple
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
            recipes: {},
            alertMessage: null,
            actualId: "",
            collapseList: [],
            recipeCategories: [],
            page_size: 6,
            activeClass: "active",
            activeCategory: '',
            empty: false, //sprawdzanie czy pole do wyszukiwania jest puste
        };
    },
    mounted() {
        //~ wywołanie metody przy zmontowaniu strony
        this.getRecipes();
        this.statusAlert();
        this.getRecipeCategory();

    },
    methods: {


        setId(id) {
            this.actualId = id;
            console.log(this.actualId, "dd");
        },
        async searchForm() {                    //POLE DO WYSZUKIWANIA PRODUKTOW
            //console.log(this.query);
            axios
                .post(`/api/v1/recipes/search/?page_number=${this.$route.params.page_number}&page_size=${this.page_size}`,
                {
                    query: this.query
                })
                .then((response) => {
                    this.recipes = response.data;
                    console.log(this.recipes.recipes.length, 'długość');
                    if(this.recipes.recipes.length==0){this.empty = true;}
                    else{this.empty = false;}

                })
                .catch((error) => {
                    console.log(error);
                });
        },

        ///////////////////////////////////// POBIERANIE WSZYSTKICH PRZEPISOW /////////////////////////////////////////////////////////////
        async getRecipes() {
            const storedCategory = localStorage.getItem('category');
            if (storedCategory) {
                this.activeCategory = storedCategory;
            } else {
                this.activeCategory = '';
            }
            axios
                .get(`/api/v1/recipes/?page_number=${this.$route.params.page_number}&page_size=${this.page_size}&category=${this.activeCategory}`) //* get pobierający wszystkie produkty (które nie są usunięte)
                .then((response) => {
                    console.log(response, "respons wszystkiego");
                    this.recipes = response.data;
                    this.collapseList = [];
                    for (recipe in this.recipes) {
                        this.collapseList.push(false);
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        /////////////////////////////////////////// POBIERANIE PRZEPISU PO WYBRANEJ KATEGORII /////////////////////////////////////////////////////////////
        async getRecipesByCategory(category) {
            localStorage.setItem('category', category);
            this.activeCategory = category;
            axios
                // .get(`/api/v1/products/${activeCategory}/`)
                .get(`/api/v1/recipes/?category=${this.activeCategory}&page_number=${this.$route.params.page_number}&page_size=${this.page_size}`)
                .then((response) => {
                    console.log(response, "respons po kategorii");
                    this.recipes = response.data;
                    this.$router.push({ path: '/ViewRecipe/1/' });
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        ///////////////////////////////////// USUWANIE PRZEPISU /////////////////////////////////////////////////////////////
        /*
                async deleteRecipe(id) {
                    console.log(id, "delete recipe id");
                    axios
                        .delete(`/api/v1/recipe/${id}/`, {
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
        */
        ///////////////////////////////////// POBIERANIE SAMEJ KATEGORII PRODUKTU /////////////////////////////////////////////////////////////
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
.zoom {
    transition: transform .2s; /* Animation */
    margin: 0 auto;
}

.zoom:hover{
    transform: scale(1.5); /* (150% zoom - Note: if the zoom is too large, it will go outside of the viewport) */
}
.show-modal{
    display: block !important;
}

#card:hover{
    transform: scale(1.05);
    box-shadow: 0 10px 20px rgba(0,0,0,.12), 0 4px 8px rgba(0,0,0,.06);
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

.pagination>.active>a {
    color: white;
    background-color: #2b9788 !Important;
    border: solid 1px #2b9788 !Important;
}

.pagination>.active>a:hover {
    background-color: #1a5f56 !Important;
    border: solid 1px #1a5f56;
}
</style>
