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
            <!--MODAL-->
            <div class="modal fade" id="modalid" tabindex="-1" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header border-bottom-0">
                            <button type="button" class="btn-close" data-mdb-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body text-start text-black p-4">
                            <h5 class="modal-title text-uppercase mb-5" id="exampleModalLabel">Edycja {{ recipe.name }}</h5>

                            <form @submit.prevent="submitForm">
                                <div class="row">
                                    <div class="col-lg-8">
                                        <MDBInput type="text" label="Nazwa" id="name" wrapperClass="mb-4" v-model="name"
                                            required />

                                        <MDBTextarea label="Opis" id="description" wrapperClass="mb-4" v-model="description"
                                            rows="4" required />
                                        <MDBInput type="number" label="cena" id="cena" wrapperClass="mb-4" v-model="price"
                                            required />

                                    </div>
                                    <div class="col-lg-4">
                                        <div v-if="imagePreview.length === 0">
                                            <div v-if="recipe.get_image == ''">
                                                <img src="https://mdbootstrap.com/img/Photos/Others/placeholder-avatar.jpg"
                                                    alt="" loading="lazy" class="img-fluid mt-5 mb-2 rounded"
                                                    style="width: 120px; height: 120px" />
                                            </div>
                                            <div v-if="recipe.get_image != ''">
                                                <img :src="recipe.get_image" alt="" loading="lazy"
                                                    class="img-fluid mt-5 mb-2 rounded"
                                                    style="width: 120px; height: 120px" />
                                            </div>
                                        </div>
                                        <div v-if="imagePreview.length > 0">
                                            <img :src="imagePreview" alt="zdjecie" class="img-fluid my-5 rounded"
                                                style="width: 120px;height: 120px" />
                                        </div>
                                        <div class="ms-3">
                                            <div class="btn btn-primary btn-rounded">
                                                <MDBFile class="form-control d-none" label="zmien"
                                                    @change="handleFileUpload($event)" id="image" accept=".jpg,.jpeg,.png">
                                                </MDBFile>
                                            </div>

                                        </div>
                                    </div>

                                    <div class="row justify-content-center">
                                        <div class="col-md-4 mt-3">
                                            <MDBBtn color="warning" block type="submit"> zapisz edycje </MDBBtn>
                                        </div>


                                    </div>
                                </div>

                            </form>
                        </div>
                        <div class="modal-footer d-flex justify-content-center border-top-0 py-4">
                            <button type="button" class="btn btn-danger" data-mdb-dismiss="modal">Zamknij</button>
                        </div>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col-lg-4">
                    <div class="card mb-4">
                        <div class="card-body text-center">
                            <div v-if="imagePreview.length === 0">
                                <div v-if="recipe.get_image == ''">
                                    <img src="https://mdbootstrap.com/img/Photos/Others/placeholder-avatar.jpg" alt=""
                                        loading="lazy" class="img-fluid mt-5 mb-2 rounded"
                                        style="width: 120px; height: 120px" />
                                </div>
                                <div v-if="recipe.get_image != ''">
                                    <img :src="recipe.get_image" alt="" loading="lazy" class="img-fluid mt-5 mb-2 rounded"
                                        style="width: 120px; height: 120px" />
                                </div>
                            </div>
                            <div v-if="imagePreview.length > 0">
                                <img :src="imagePreview" alt="zdjecie" class="img-fluid my-5 rounded"
                                    style="width: 120px;height: 120px" />
                            </div>
                            <h5 class="my-3">{{ recipe.name }}</h5>

                            <div class="d-flex justify-content-center mb-2">
                                <button type="button" v-if="user.role === 'Kucharz'" class="btn btn-outline-primary" data-mdb-toggle="modal" value="1"
                                    data-mdb-target="#modalid">Edytuj przepis</button>
                                <MDBBtn v-if="user.role === 'Kucharz'" type="button" color="danger" size="sm" rounded @Click="setId(recipe.id)">
                                    usuń
                                </MDBBtn>
                            </div>
                        </div>
                    </div>
                    <div class="card mb-4 mb-lg-0">
                        <div class="card-body p-0">
                            <ul class="list-group list-group-flush rounded-3">
                                <li class="list-group-item d-flex justify-content-between align-items-center p-3">
                                    <p class="mb-0">{{ recipe.description }}</p>
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
                                    <p class="mb-0">{{ test.name }}</p>
                                </div>
                                <div class="col-sm-7">
                                    <p class="text-muted mb-0 text-end me-2">{{ test.quantity }} g</p>
                                </div>
                            </div>
                            <hr>


                        </div>
                    </div>

                    <div class="card mb-4 w-25 float-end">
                        <div class="card-body p-0">
                            <ul class="list-group list-group-flush rounded-3">
                                <li class="list-group-item d-flex  text-end p-3">
                                    <p class="mb-0"><b>Cena: </b> {{ recipe.price }} pln</p>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
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
    MDBInput,
    MDBTextarea,
    MDBFile
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
        MDBInput,
        MDBTextarea,
        MDBFile
    },
    data() {
        return {
            recipe: {},
            name: "",
            id: "",
            price: "",
            description: "",
            token: "",
            actualId: "",
            image: "",
            imagePreview: "",
            imageChanged: false,
            recipe: "",
            product_list: [],
            user: {},
        }
    },
    computed: {
        getToken() {
            return this.$store.state.token;
        },
        getId() {
            return this.$store.state.user.id;
        }
    },
    mounted() {
        this.id = this.getId;
        const recipe_id = this.$route.params.id;   //? pobranie id przepisu z parametru - URL
        this.getRecipe();
        this.getRecipeProducts();
        this.getUser();
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
                })
                .catch((error) => {
                    console.log(error);
                })
        },
        setId(id) {
            this.actualId = id;
            console.log(this.actualId, "dd");
        },
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
                    this.name = response.data.name;
                    this.description = response.data.description;
                    this.imagePreview = response.data.get_image;
                    this.price = response.data.price;
                    console.log(response.data, "opis co tu jest");
                })
                .catch((error) => {
                    console.log(error);
                })
        },
        submitForm() {
            let formData = new FormData();
            const recipe_id = this.$route.params.id;   //? pobranie id produktu z parametru - URL              
            formData.append('name', this.name);
            formData.append('description', this.description);
            formData.append('price', this.price);
            if (this.imageChanged) {
                formData.append('image', this.image);
            } else {
                formData.append('image', this.imagePreview.replace('http://127.0.0.1:8000/media/', ''));
            }

            axios
                .put(`/api/v1/recipe/${recipe_id}/`, formData, {
                    headers: {
                        Authorization: `Token ${this.$store.state.user.token}`
                    }
                })
                .then((response) => {
                    //this.alert = true;
                    //this.notification = "pomyslnie edytowano przepis " +this.name;
                    //this.$store.commit('setAlert',this.notification);
                    location.reload();
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
                    console.log(response.data, "produkty");
                    for (let i = 0; i < response.data.length; i++) {
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
                            })
                            .catch((error) => {
                                console.log(error);
                            })

                    }
                    console.log(this.product_list, "ilosc oraz nazwa");


                })
                .catch((error) => {
                    console.log(error);
                })
        },
        async deleteProduct(id) {
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
                    this.$router.push({ path: '/ViewRecipe/1/' });
                })
                .catch((error) => {
                    console.log(error);
                });
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
            this.imageChanged = true;
        },
    }
}
</script>

