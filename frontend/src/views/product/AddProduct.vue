<template>
    <navbar></navbar>
    <div class="container text-center">


        <MDBCard class="center-block">

            <MDBCardBody>
                <form @submit.prevent="submitForm">
                    <div class="row">
                        <div class="col-md-6">
                            <MDBInput type="text" label="name" id="name" wrapperClass="mb-4" v-model="name" required />
                            <MDBTextarea label="description" id="description" wrapperClass="mb-4" v-model="description"
                                rows="4" required />
                            <MDBInput type="number" label="product_quantity" id="product_quantity" wrapperClass="mb-4"
                                v-model="product_quantity" required />
                                <p>wybierz kategorie</p>
                                <select class="form-select" id="idCategory" aria-label="Default select example" required>
                                    <option v-for="productCategory in productCategories" v-bind:key="productCategory.id" :value="productCategory.id">{{productCategory}}</option>
                                </select>
                        </div>


                        <div class="col-md-6">
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
                        <div class="col-md-4 mt-2">
                            <MDBBtn color="primary" block type="submit"> Dodaj </MDBBtn>
                        </div>

                    
                    </div>

                </form>
            </MDBCardBody>
        </MDBCard>
    </div>
</template>

<script>

import { MDBInput, MDBBtn, MDBCard, MDBCardBody, MDBTextarea, MDBFile } from "mdb-vue-ui-kit";
import { ref } from "vue";
import axios from "axios";
import FormData from "form-data";
import Navbar from "@/components/ui/Navbar.vue";
export default {
    components: {
        MDBFile,
        MDBTextarea,
        MDBCard,
        MDBCardBody,
        MDBInput,
        MDBBtn,
        Navbar,
    },
    data() {
        return {
            name: "",
            description: "",
            product_quantity: "",
            token: "",
            image: "",
            imagePreview: "",
            alert: false,
            product_id: 0,
            notification: "",
            productCategories: [],

        }
    },
    computed: {
        getToken() {
            return this.$store.state.token;
        }
    },
    mounted() {
        this.getProductCategory();
    },
    methods: {
        submitForm() {
            let formData = new FormData();
            formData.append('name', this.name);
            formData.append('product_quantity', this.product_quantity);
            formData.append('description', this.description);
            formData.append('image', this.image);
            //console.log(this.image, "consol log zdjecia")
            var select = document.getElementById('idCategory');
            var selectCategoryValue = select.options[select.selectedIndex].value ;
            console.log(selectCategoryValue, 'select category value');
            formData.append('Product_category', selectCategoryValue);
            axios
                .post(`/api/v1/product/${this.product_id}/`, formData, {
                    headers: {
                        Authorization: `Token ${this.$store.state.user.token}`,
                        
                    }
                })
                .then((response) => {
                    console.log(response);
                    this.notification = "pomyslnie dodano produkt " +this.name;
                    this.$store.commit('setAlert',this.notification);
                    this.$router.push({ path: '/ViewProduct/1/'});

                })
                .catch((error) => {
                    console.log(error);
                })
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

        async getProductCategory(){
            axios
                .get("/api/v1/productCategory/")
                .then((response) => { 
                    this.productCategories = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },
    

};
</script>