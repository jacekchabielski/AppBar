<template>
    <navbar></navbar>

    <!-- Modal -->
    

    <div class="modal fade" id="DetailsModal" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Szczegóły zamówienia</h5>
                    <button type="button" class="btn-close" data-mdb-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">

                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-mdb-dismiss="modal">Zamknij</button>
                </div>
            </div>
        </div>
    </div>
    <MDBTable>
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Zamówienie</th>
                <th scope="col">Cena</th>
                <th scope="col">Data</th>
                <th scope="col">Nr stolika</th>
                <th scope="col">Status</th>
                <th scope="col" class="text-center">Akcje</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(item, index) in tablicainna">
                
                <th scope="row">{{ index + 1 }}</th>
                <td>{{item.name}}</td>
                <td>{{item.price}} PLN</td>
                <td>{{item.created}}</td>
                <td>{{item.table}}</td>
                <td>{{item.status}}</td>
                <td class="text-center">
                    <MDBBtn type="button" color="info" data-mdb-toggle="modal" :value="item.id" :data-mdb-target="'#modal'+ item.id" @click="ViewProducts(index)">Szczegóły</MDBBtn>
                </td>
                <div class="modal fade" :id="'modal'+item.id" tabindex="-1" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header border-bottom-0">
                                <button type="button" class="btn-close" data-mdb-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body text-start text-black p-4">
                                <h5 class="modal-title text-uppercase mb-5" id="exampleModalLabel">{{ item.name }}</h5>
                                <p class="mb-0" style="color: #35558a;">Podsumowanie zamówienia</p>
                                <hr class="mt-2 mb-4"
                                    style="height: 0; background-color: transparent; opacity: .75; border-top: 2px dashed #9e9e9e;">
            
                                
            
                                <div class="d-flex justify-content-between pb-2" v-for="przepisy in gotowe">
                                    <p class="small">{{przepisy.ilosc_przepisu}}x {{ przepisy.nazwa_przepisu }}</p>
                                    <p class="small">{{przepisy.cena}} PLN</p>
                                </div>
            
                                <div class="d-flex justify-content-between">
                                    <p class="fw-bold">Razem</p>
                                    <p class="fw-bold" style="color: #35558a;">{{item.price}} PLN</p>
                                </div>
                            </div>
                            <div class="modal-footer d-flex justify-content-center border-top-0 py-4">
                                <button type="button" class="btn btn-danger" data-mdb-dismiss="modal">Zamknij</button>
                            </div>
                        </div>
                    </div>
                </div>
            </tr>
        </tbody>
    </MDBTable>
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
        MDBIcon,
    },
    data() {
        return {
            tablica: [],
            tablicainna: [],
            tablicadwa: [],
            gotowe: [],
        }
    },
    directives: {
    },
    mounted() {
        document.title = 'Zamówienia'
        this.ViewAllOrders();
        
    },
    beforeMount() {
        
    },
    computed: {
    },
    methods: {
        


        ViewAllOrders() {
            axios
                .get('/api/v1/orders/all/')
                .then((response) => {
                    this.tablicainna = response.data.orders;
                    //console.log(this.tablica[2].id,'zawartosc tablicy wczesniej');
                    //console.log(this.tablicainna, 'orders');

                })
                .catch((error) => {
                    console.log(error);
                })

            
        },
        ViewProducts(id) {
            this.gotowe = [];
            let idd = id;
            axios
                .get("/api/v1/orders/all/")
                .then((response) => {
                    this.tablica = response.data.orders;

                    console.log(this.tablica, 'co tu jet ?');       // informacje o zamówieniach

                    axios
                        .get(`/api/v1/order/${this.tablica[idd].id}/order_recipes/`, {
                            headers: {
                                Authorization: `Token ${this.$store.state.user.token}`,
                            },
                        })
                        .then((response2) => {
                            // console.log(response2, "resp dwa");

                            this.tablicadwa = response2.data;
                            //console.log(this.tablicadwa, 'zawartosc tablicy');
                            //console.log(this.tablica[0], 'zawartosc tablicy');

                            axios
                                .get('/api/v1/recipes/all')
                                .then((response) => {
                                    console.log(response.data, 'informacje o przepisach');
                                    console.log(this.tablicadwa, 'zawartosc tablicy');

                                    //console.log(response.data.recipes[0].id, 'id przepisu  tlyko');
                                    //console.log(this.tablica2, 'zawartosc tablicy');
                                    //console.log(this.tablica[0], 'id z tablicy 0');

                                    // for(let i = 0; i< response.data.recipes.length; i++){
                                    // console.log(i, 'i');
                                    // }

                                    for (let i = 0; i < this.tablicadwa.length; i++) {
                                        for (let b = 0; b < response.data.recipes.length; b++) {
                                            if (this.tablicadwa[i].recipe_id == response.data.recipes[b].id) {
                                                console.log(response.data.recipes[b].name, "nazwa przepisu");
                                                console.log(this.tablicadwa[i].quantity, 'ilosc przepisow quantity');
                                                let objectToPush = {
                                                    'nazwa_przepisu': response.data.recipes[b].name,
                                                    'ilosc_przepisu': this.tablicadwa[i].quantity,
                                                    'cena':response.data.recipes[b].price * this.tablicadwa[i].quantity,
                                                }
                                                this.gotowe.push(objectToPush);
                                            }
                                        }
                                    }
                                    console.log(this.gotowe,'co magotowe ??');

                                })
                                .catch((error) => {
                                    console.log(error);
                                })

                        })
                        .catch((error) => {
                            console.log(error);
                        })

                })

                .catch((error) => {
                    console.log(error);
                });
        },
    }

};

</script>