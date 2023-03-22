<template>
    <navbar></navbar>
    <div class="container">


        <MDBCard class="center-block">

            <MDBCardBody>
                <form @submit.prevent="submitForm">
                    <div class="row">
                        <div class="col-md-6">
                            <MDBInput type="text" label="Nazwa" id="name" wrapperClass="mb-4" v-model="name"  required />
                            
                            <MDBTextarea label="Opis" id="description" wrapperClass="mb-4" v-model="description"
                                rows="4" required />
                            <MDBInput type="number" label="Ilość" id="product_quantity" wrapperClass="mb-4"
                            v-model="product_quantity" required />

                            <p>wybierz kategorie</p>
                                <select class="form-select" id="idCategory" aria-label="Default select example" required>
                                    <template v-for="productCategory in productCategories" v-bind:key="productCategory.id">
                                        <option :value="productCategory.id" :selected="productCategory === selectedCategory">{{productCategory}}</option>
                                    </template>
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
                                    <MDBFile class="form-control d-none" label="zmien"
                                        @change="handleFileUpload($event)" id="image" accept=".jpg,.jpeg,.png"></MDBFile>
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
            productCategories: [],
            selectedCategory: "",
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
        this.getProductCategory();
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
                    this.selectedCategory = response.data.Product_category_name;
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
            var select = document.getElementById('idCategory');
            var selectCategoryValue = select.options[select.selectedIndex].value ;
            console.log(selectCategoryValue, 'select category value');
            formData.append('Product_category', selectCategoryValue);
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
            this.imageChanged = true ;
        },
        async getProductCategory(){
            axios
                .get("/api/v1/productCategory/")
                .then((response) => {
                    console.log(response,'response z getproductcategory');
                    this.productCategories = response.data;
                    console.log(this.productCategories, 'nazwy kategorii');
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        
    }
};
</script>