<template>
    <navbar></navbar>
    <div v-if="alertMessage" class="alert alert-success alert-dismissible fade show" role="alert">
        {{ alertMessage }}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close" @click="close()"></button>
    </div>
    <MDBTable class="align-middle mb-0 bg-white">
        <thead class="bg-light">
            <tr>
                <th>Name</th>
                <th>Description</th>
                <th>quantity</th>
                <th colspan="2">Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="product in products" v-bind:key="product.id">
                <td>
                    <div class="d-flex align-items-center">
                        <img v-bind:src="product.get_thumbnail" style="width: 81px; height: 81px"
                            class="rounded-circle" />
                        <div class="ms-3">
                            <p class="fw-bold mb-1">{{ product.name }}</p>
                        </div>
                    </div>
                </td>
                <td>
                    <p class="fw-normal mb-1">{{ product.description }}</p>
                </td>
                <td>{{ product.product_quantity }}</td>
                <td>
                    <MDBBtn color="link" size="sm" rounded>
                        <router-link v-bind:to="'EditProduct' + product.get_absolute_url">Edytuj</router-link>
                    </MDBBtn>

                </td>
                <td>
                    <MDBBtn type="button" color="danger" size="sm" rounded data-bs-toggle="modal"
                        @click="deleteProduct(product.id)" data-bs-target="#myModal">
                        usuń
                    </MDBBtn>
                </td>
            </tr>

        </tbody>
    </MDBTable>
</template>


<script>
import axios from "axios";
import Navbar from "@/components/ui/Navbar.vue";
import { ref } from 'vue';
import {
    MDBTable,
    MDBBtn,
    MDBBadge,
    MDBModal,
    MDBModalHeader,
    MDBModalTitle,
    MDBModalBody,
    MDBModalFooter,
} from 'mdb-vue-ui-kit';

export default {
    components: {
        MDBTable,
        MDBBtn,
        MDBBadge,
        Navbar,
        MDBModal,
        MDBModalHeader,
        MDBModalTitle,
        MDBModalBody,
        MDBModalFooter,
    },
    props: {
        alert: Boolean
    },
    computed: {
        showAlert() {
            return this.$store.getters.getAlertStatus
        }
    },
    data() {
        return {
            products: {},
            alertMessage: null

        }
    },
    mounted() {             //~ wywołanie metody przy zmontowaniu strony
        this.getProducts();
        console.log(this.$store.getters);
        console.log(this.showAlert);
        this.statusAlert();



    },
    methods: {
        async getProducts() {
            axios
                .get('/api/v1/products/') //* get pobierający wszystkie produkty (które nie są usunięte)
                .then((response) => {
                    this.products = response.data;

                })
                .catch((error) => {
                    console.log(error);
                })
        },
        deleteProduct(id) {
            //let formData = new FormData();
            //formData.append('id', id);
            // console.log(id, 'to jest to id do usuwania')
            axios
                .delete(`/api/v1/product/${id}/`, {
                    headers: {
                        Authorization: `Token ${this.$store.state.user.token}`
                    }
                })
                .then((response) => {
                    console.log(response);
                    location.reload()
                })
                .catch((error) => {
                    console.log(error);
                })
        },

        statusAlert() {
            if (this.showAlert) {
                this.alertMessage = this.$store.getters.getMessage;
                this.$store.commit('consumeAlert');
                console.log(this.alertMessage);

            }
        },
        close() {
            alertMessage = "";
        }
    }

};
</script>