<template>
    <navbar></navbar>


    <MDBContainer fluid>


        <section style="background-color: #eee;">
            <div class="text-center container-fluid py-5">
                <h4 class="mt-4 mb-5"><strong>Zamówienia</strong></h4>

                <div class="row">
                    
                        <div class="col-lg-2 mb-4"  v-for="order in tablica" v-show="order.status!='gotowe'">
                            <MDBCard>
                                <MDBCardHeader class="mt-2">{{ order.name }}</MDBCardHeader>
                                <MDBCardBody>
                                    <MDBCardTitle>
                                        <ol>
                                            <li>fryty</li>
                                        </ol>
                                    </MDBCardTitle>
                                    <MDBCardText>
                                        {{ order.description }}
                                    </MDBCardText>
                                    <MDBBtn type="button" color="primary" @Click="UpdateStatus(order.id)">
                                        Zrobione !
                                    </MDBBtn>
                                </MDBCardBody>
                            </MDBCard>
                        </div>
                    
                </div>

            </div>
        </section>

    </MDBContainer>
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
    name: "Home",
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
    data() {
        return {
            tablica: [],
            tablica2: [],
            orderId: 0,
            actualId: "",
        }
    },
    directives: {
    },
    mounted() {
        document.title = 'Kuchnia'
        // this.getOrderRecipe()
    },
    beforeMount() {
        this.ViewAllProducts()
    },
    computed: {
    },
    methods: {
        setId(id) {
            this.actualId = id;
            console.log(this.actualId, "dd");
        },

        UpdateStatus(id) {
            console.log(id, "change status id");
            let formData = new FormData();
            //const update_id = id;
            formData.append('status', 'gotowe');
            axios
                .put(`/api/v1/order/${id}/`, formData, {
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
        ViewAllProducts() {
            axios
                .get('/api/v1/orders/all/')
                .then((response) => {

                    this.tablica = response.data.orders;
                    //console.log(this.tablica[2].id,'zawartosc tablicy wczesniej');
                    console.log(this.tablica, 'orders');
                })
                .catch((error) => {
                    console.log(error);
                })
        },

        getOrderRecipe() {
            //console.log(this.tablica[2].id,'zawartosc tablicy wczesniej');
            // for(let i = 0; i < this.tablica.length; i++){
            // console.log(this.tablica[2].id,'zawartosc tablicy wczesniej');
            //console.log(this.tablica[1].id);
            const order_id = 8;
            let formData = new FormData();
            //formData.append('id', product_id);
            axios
                .get(`/api/v1/order_recipes/${order_id}/`, {
                    headers: {
                        Authorization: `Token ${this.$store.state.user.token}`
                    }
                })
                .then((response) => {
                    //this.recipe = response.data;
                    console.log(response.data, "powinny byc wszystkie rzeczy git");
                    /*
                    for(let i = 0; i < response.data.length; i++){
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
*/

                })
                .catch((error) => {
                    console.log(error);
                })
        }
    },
    //}


};

</script>