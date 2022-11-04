<template>
    <navbar></navbar>
    <MDBTable class="align-middle mb-0 bg-white">
        <thead class="bg-light">
            <tr>
                <th>Name</th>
                <th>Description</th>
                <th>quantity</th>
                <th>Actions</th>
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
                    <MDBBtn color="link" size="sm" rounded > <router-link v-bind:to="'EditProduct'+product.get_absolute_url">Edytuj</router-link> </MDBBtn>

                </td>
            </tr>

        </tbody>
    </MDBTable>
</template>


<script>
import axios from "axios";
import Navbar from "@/components/ui/Navbar.vue";
import {
    MDBTable,
    MDBBtn,
    MDBBadge,
} from 'mdb-vue-ui-kit';

export default {
    components: {
        MDBTable,
        MDBBtn,
        MDBBadge,
        Navbar,
    },
    data() {
        return {
            products: {}
        }
    },
    mounted() {             //~ wywołanie metody przy zmontowaniu strony
        this.getProducts();
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
    }
};
</script>