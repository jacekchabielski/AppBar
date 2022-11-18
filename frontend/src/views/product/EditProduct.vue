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
                                    <MDBFile class="form-control d-none" label="zmien"
                                        @change="handleFileUpload($event)" id="image" accept=".jpg,.jpeg,.png"></MDBFile>
                                </div>

                            </div>
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
            image: "",
            imagePreview: "",
            imageChanged: false,
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
        getProduct(){
            const product_id = this.$route.params.id;   //? pobranie id produktu z parametru - URL
            let formData = new FormData();
            //formData.append('id', product_id);
            axios
                .get(`/api/v1/product/${product_id}/`, {
                    //params: {id: product_id},
                    headers: {
                        Authorization: `Token ${this.$store.state.user.token}`
                    }
                })
                .then((response) => {
                    this.alert = true;
                    this.name = response.data.name;
                    this.description = response.data.description;
                    this.product_quantity = response.data.product_quantity;
                    this.imagePreview = response.data.get_image;
                    console.log(response.data);
                })
                .catch((error) => {
                    console.log(error);
                })
        },
        submitForm() {
            let formData = new FormData();
            const product_id = this.$route.params.id;   //? pobranie id produktu z parametru - URL              
            formData.append('name', this.name);
            formData.append('product_quantity', this.product_quantity);
            formData.append('description', this.description);
            if(this.imageChanged){
                formData.append('image', this.image);
            }else{
                formData.append('image', this.imagePreview.replace('http://127.0.0.1:8000/media/',''));
            }
            
            axios
                .put(`/api/v1/product/${product_id}/`, formData, {
                    headers: {
                        Authorization: `Token ${this.$store.state.user.token}`
                    }
                })
                .then((response) => {
                    //this.alert = true;
                    this.notification = "pomyslnie edytowano produkt " +this.name;
                    this.$store.commit('setAlert',this.notification);
                    this.$router.push({ name: 'ViewProduct'});
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
            this.imageChanged = true ;
        }
        
    }
};
</script>