<template>
    <navbar></navbar>
    <div class="container">


        <MDBCard class="center-block">

            <MDBCardBody>
                <form @submit.prevent="submitForm">
                    <div class="row">
                        <div class="col-md-6">
                            <MDBInput type="text" label="name" id="name" wrapperClass="mb-4" v-model="name"  required />
                            
                            <MDBTextarea label="description" id="description" wrapperClass="mb-4" v-model="description"
                                rows="4" required />
                            <MDBInput type="number" label="product_quantity" id="product_quantity" wrapperClass="mb-4"
                            v-model="product_quantity" required />
                        </div>

                        
                        <div class="row justify-content-center">
                            <div class="col-md-4">
                                <MDBBtn color="warning" block type="submit"> zapisz edycje </MDBBtn>
                            </div>
    
                            <div v-if="alert">
                                <p>Zapisz zmiany !</p>
                            </div>
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
    import FormData from "form-data";
    import {
        MDBFile,
        MDBTextarea,
        MDBCard,
        MDBCardBody,
        MDBInput,
        MDBBtn
    } from 'mdb-vue-ui-kit';

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
            product_quantity: "",
            description: "",
            token: "",
        }
    },

    computed: {
        getToken() {
            return this.$store.state.token;
        }
    
    },
    mounted(){
        const product_id = this.$route.params.id;   //? pobranie id produktu z parametru - URL
        this.getProduct();
    },
    methods: {
        submitForm() {
            let formData = new FormData();
            const product_id = this.$route.params.id;   //? pobranie id produktu z parametru - URL
            formData.append('id', product_id);              //? nowe dane 
            formData.append('name', this.name);
            formData.append('product_quantity', this.product_quantity);
            formData.append('description', this.description);
            axios
                .put('/api/v1/product/', formData, {
                    headers: {
                        Authorization: `Token ${this.$store.state.user.token}`
                    }
                })
                .then((response) => {
                    console.log(response);
                    this.alert = true;
                })
                .catch((error) => {
                    console.log(error);
                })
        },
        getProduct(){
            const product_id = this.$route.params.id;   //? pobranie id produktu z parametru - URL
            console.log(product_id);
            let formData = new FormData();
            formData.append('id', product_id);
            axios
                .get('/api/v1/product/', {
                    params: {id: product_id},
                    headers: {
                        Authorization: `Token ${this.$store.state.user.token}`
                    }
                })
                .then((response) => {
                    console.log(response);
                    this.alert = true;
                    this.name = response.data.name;
                    this.description = response.data.description;
                    this.product_quantity = response.data.product_quantity;
                })
                .catch((error) => {
                    console.log(error);
                })
        }
    }
};
</script>