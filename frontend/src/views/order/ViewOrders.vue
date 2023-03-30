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
                <th scope="col">Status</th>
                <th scope="col" class="text-center">Akcje</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(item, index) in tablica">
                
                <th scope="row">{{ index + 1 }}</th>
                <td>{{item.name}}</td>
                <td>{{item.price}} PLN</td>
                <td>{{item.created}}</td>
                <td>{{item.status}}</td>
                <td class="text-center">
                    <MDBBtn type="button" color="info" data-mdb-toggle="modal" :value="item.id" :data-mdb-target="'#modal'+ item.id">Szczegóły</MDBBtn>
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
            
                                <div class="d-flex justify-content-between">
                                    <p class="small mb-0">Cheeseburger</p>
                                    <p class="small mb-0">25 PLN</p>
                                </div>
            
                                <div class="d-flex justify-content-between pb-1">
                                    <p class="small">Frytki</p>
                                    <p class="small">10 PLN</p>
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
        }
    },
    directives: {
    },
    mounted() {
        document.title = 'Zamówienia'
        // this.getOrderRecipe()
        this.ViewAllOrders()
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
                    this.tablica = response.data.orders;
                    //console.log(this.tablica[2].id,'zawartosc tablicy wczesniej');
                    console.log(this.tablica, 'orders');

                })
                .catch((error) => {
                    console.log(error);
                })
        },
    }

};

</script>