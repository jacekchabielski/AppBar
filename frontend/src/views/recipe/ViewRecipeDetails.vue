<template>
    <navbar></navbar>
    <section style="background-color: #eee;">
        <div class="container py-5">
            <div class="row">
                <div class="col">
                    <nav aria-label="breadcrumb" class="bg-light rounded-3 p-3 mb-4">
                        <ol class="breadcrumb mb-0">
                            <h2>Szczegóły {{ recipe.name }}</h2>
                        </ol>
                    </nav>
                </div>
            </div>

            <div class="row">
                <div class="col-lg-4">
                    <div class="card mb-4">
                        <div class="card-body text-center">
                            <div v-if="imagePreview.length === 0">
                                <div v-if="recipe.get_image == '' ">
                                    <img  src="https://mdbootstrap.com/img/Photos/Others/placeholder-avatar.jpg" alt="" loading="lazy" class="img-fluid mt-5 mb-2 rounded" style="width: 120px; height: 120px" />
                                </div>
                                <div v-if="recipe.get_image != '' ">
                                    <img  :src="recipe.get_image" alt="" loading="lazy" class="img-fluid mt-5 mb-2 rounded" style="width: 120px; height: 120px" />
                                </div>
                            </div>
                            <div v-if="imagePreview.length > 0">
                                <img :src="imagePreview" alt="zdjecie" class="img-fluid my-5 rounded" style="width: 120px;height: 120px" />
                            </div>
                            <h5 class="my-3">{{ recipe.name }}</h5>
                            
                            <div class="d-flex justify-content-center mb-2">
                                <button type="button" class="btn btn-outline-primary">Edytuj przepis</button>
                                <button type="button" class="btn btn-danger ms-1">Usuń przepis</button>
                            </div>
                        </div>
                    </div>
                    <div class="card mb-4 mb-lg-0">
                        <div class="card-body p-0">
                            <ul class="list-group list-group-flush rounded-3">
                                <li class="list-group-item d-flex justify-content-between align-items-center p-3">
                                    <p class="mb-0">{{recipe.description}}</p>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6 mx-auto">
                    <div class="card mb-4">
                        <div class="card-body" v-for="test in product_list">
                            <div class="row">
                                <div class="col-sm-5">
                                    <p class="mb-0">{{test.name}}</p>
                                </div>
                                <div class="col-sm-7">
                                    <p class="text-muted mb-0 text-end me-2">{{test.quantity}} g</p>
                                </div>
                            </div>
                            <hr>
                            
                            
                        </div>
                    </div>

                    <div class="card mb-4 w-25 float-end">
                        <div class="card-body p-0">
                            <ul class="list-group list-group-flush rounded-3">
                                <li class="list-group-item d-flex  text-end p-3">
                                    <p class="mb-0"><b>Cena: </b> {{ recipe.price}} pln</p>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>


<script>
import HelloWorld from "@/components/HelloWorld.vue";
import axios from "axios";
import Navbar from "@/components/ui/Navbar.vue";
import FormData from "form-data";

import {
    MDBCard,
    MDBCardHeader,
    MDBCardBody,
    MDBCardTitle,
    MDBCardText,
    MDBBtn,
    MDBRow,
    MDBCol,
} from "mdb-vue-ui-kit";

export default {
    components: {
        Navbar,
        MDBCard,
        MDBCardHeader,
        MDBCardBody,
        MDBCardTitle,
        MDBCardText,
        MDBBtn,
        MDBRow,
        MDBCol,
    },
    data() {
        return {
            recipe: {},
            name: "",
            price: "",
            description: "",
            token: "",
            image: "",
            imagePreview: "",
            recipe: "",
            product_list: [],

        }
    },
    computed: {
        getToken() {
            return this.$store.state.token;
        }
    },
    mounted() {
        const recipe_id = this.$route.params.id;   //? pobranie id przepisu z parametru - URL
        this.getRecipe();
        this.getRecipeProducts();
    },
    methods: {
        getRecipe() {
            const recipe_id = this.$route.params.id;   //? pobranie id przepisu z parametru - URL
            let formData = new FormData();
            //formData.append('id', product_id);
            axios
                .get(`/api/v1/recipe/${recipe_id}/`, {
                    headers: {
                        Authorization: `Token ${this.$store.state.user.token}`
                    }
                })
                .then((response) => {
                    this.recipe = response.data;
                    console.log(response.data,"opis co tu jest");
                })
                .catch((error) => {
                    console.log(error);
                })
        },
        getRecipeProducts() {
            const recipe_id = this.$route.params.id;   //? pobranie id przepisu z parametru - URL
            let formData = new FormData();
            //formData.append('id', product_id);
            axios
                .get(`/api/v1/recipe_products/${recipe_id}/`, {
                    headers: {
                        Authorization: `Token ${this.$store.state.user.token}`
                    }
                })
                .then((response) => {
                    //this.recipe = response.data;
                    console.log(response.data,"produkty");
                    for(let i = 0; i < response.data.length; i++){
                        //this.product_list = response.data[i].product_quantity;
                        //console.log(response.data[i].quantity, "ilosci produktow");
                        //this.product_list.push(response.data[i].quantity);
                        axios
                            .get(`/api/v1/product/${response.data[i].product_id}/`, {
                        headers: {
                            Authorization: `Token ${this.$store.state.user.token}`
                        }
                        })
                        .then((response2) => {
                            let objectToPush = {
                                'quantity': response.data[i].quantity,
                                'name': response2.data.name,
                            }
                            this.product_list.push(objectToPush);
                            //console.log(response.data.name,"nazwa produktu");
                            //this.product_list.push(response.data.name);
                        })
                        .catch((error) => {
                            console.log(error);
                        })
                        
                    }
                    console.log(this.product_list, "ilosc oraz nazwa");

                    //this.product_list = response.data;

                })
                .catch((error) => {
                    console.log(error);
                })
        },
    }
}
</script>

