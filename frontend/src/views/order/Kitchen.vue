<template>
    <navbar></navbar>

    <MDBContainer fluid>
        <section style="background-color: #eee">
            <div class="text-center container-fluid py-5">
                <h4 class="mt-4 mb-5"><strong>Zamówienia</strong></h4>

                <div class="row">
                    <div class="col-lg-2 mb-4" v-for="(order, index) in tablica" v-show="order.status != 'gotowe'">

                        <MDBCard>
                            <MDBCardHeader class="mt-2">{{ order.name }} {{ order.email }}</MDBCardHeader>
                            <MDBCardBody>
                                <MDBCardTitle>
                                    <div v-for="(przepis, index) in costam">
                                        <ol>
                                            <li v-if="przepis.idZamowienia == order.id"> {{ przepis.ilosc }}x {{przepis.nazwaPrzepisu}}
                                            </li>
                                        </ol>
                                    </div>
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
        MDBIcon,
    },
    data() {
        return {
            tablica_recipes: [],
            super_array: [],
            order_recipes: [],
            tablica: [],
            tablicadwa: [],
            gotowe: [],
            costam: [],
            recipeList: [],
            tablicachwilowa: [],
            array_przepisy: [],
            orderId: 0,
            actualId: "",
        };
    },
    directives: {},
    mounted() {
        document.title = "Kuchnia";
        //this.getOrderRecipe();
        //this.Test();
        this.ViewProdu();
        //this.getProductsInfo();
        //this.ViewOrders();
    },
    beforeMount() {
        //this.ViewAllProducts();

    },
    computed: {},
    methods: {
        setId(id) {
            this.actualId = id;
            console.log(this.actualId, "dd");
        },

        UpdateStatus(id) {
            console.log(id, "change status id");
            let formData = new FormData();
            //const update_id = id;
            formData.append("status", "gotowe");
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


        ViewProdu() {
            axios
                .get('/api/v1/orders/all/')
                .then((response) => {
                    this.tablica = response.data.orders;
                    console.log(this.tablica, 'tablica z orders');
                })
                .catch((error) => {
                    console.log(error);
                })

            axios
                .get('/api/v1/recipes/all/')
                .then((response) => {
                    this.tablica_recipes = response.data;
                    console.log(this.tablica_recipes, 'tablica z recipes');
                    //console.log(this.tablica, 'tablica z orderssss');

                    for (let i = 0; i < this.tablica.length; i++) {
                        axios
                            .get(`/api/v1/order/${this.tablica[i].id}/order_recipes/`, {
                                headers: {
                                    Authorization: `Token ${this.$store.state.user.token}`,
                                },
                            })
                            .then((response) => {
                                console.log(response.data, "order recipes");
                                //this.tablicachwilowa.push(response.data[i].recipe_id);
                                for (let a = 0; a < response.data.length; a++) {
                                    //console.log(response.data[a].recipe_id, 'same recipeid');

                                  
                                    let objectToPush = {
                                        'idprzepisu': response.data[a].recipe_id,
                                        'idzamowienia': response.data[a].order_id,
                                        'ilosc': response.data[a].quantity,
                                    }
                                    this.super_array.push(objectToPush);
                   
                                }
                                //this.tablicachwilowa.push(objectToPush);
                                //this.super_array = this.tablicachwilowa.slice(0);

                                //console.log(this.super_array, 'tablica chwilowa z polaczeniami');
                            })
                            .catch((error) => {
                                console.log(error);
                            })
                    }

                    axios
                        .get('/api/v1/recipes/all')
                        .then((response) => {
                            console.log(response.data, 'informacje o przepisach');
                            this.array_przepisy = response.data.recipes;

                            console.log(this.super_array, 'superarray z nowego miejsca');
                            console.log(this.tablica, 'tablica z nowego miejsca');
                            console.log(response.data.recipes[0].name, 'id pierwsze');

                            setTimeout(() => {
                                console.log(this.super_array.length, 'superarrayv2');
                                for (let z = 0; z < this.tablica.length; z++) {
                                    for (let k = 0; k < this.super_array.length; k++) {
                                        if (this.tablica[z].id == this.super_array[k].idzamowienia) {
                                            console.log(this.super_array[k].idprzepisu, 'id zamowienia znalezionego');

                                            setTimeout(() => {
                                                //console.log(response.data.length)
                                                for(let o = 0; o < response.data.recipes.length; o++ ){
                                                    if(response.data.recipes[o].id == this.super_array[k].idprzepisu ){
                                                        //console.log(response.data.recipes[o].name, 'nazwa przepisu');

                                                        
                                                        let objectToP = {
                                                        'idZamowienia': this.tablica[z].id,
                                                        'nazwaPrzepisu': response.data.recipes[o].name,
                                                        'ilosc': this.super_array[k].ilosc,
                                                        }
                                                        this.costam.push(objectToP);
                                                        
                                                    //this.tablica.push(response.data.recipes[o].name) ;
                                                    //this.tablica[z].iloscPrzepisu  = this.super_array[k].ilosc;
                                                    
                                                    }
                                                }
                                            }, 120);
                                            

                                        }
                                    }
                                }
                                console.log(this.costam,'idZamowienia, nazwa_dania, ilosc');
                            }, 250);

                            
                        })
                        .catch((error) => {
                            console.log(error);
                        })

                })
                .catch((error) => {
                    console.log(error);
                })
        },

       


        ViewProducts() {

            axios
                .get("/api/v1/orders/all/")
                .then((response) => {
                    this.tablica = response.data.orders;

                    console.log(this.tablica, 'co tu jet ?');       // informacje o zamówieniach
                    console.log(this.tablica.length, 'dlugosc tablicy');
                    // for (let z = 0; z < this.tablica.length; z++) {

                    axios
                        .get(`/api/v1/order/${this.tablica[0].id}/order_recipes/`, {
                            headers: {
                                Authorization: `Token ${this.$store.state.user.token}`,
                            },
                        })
                        .then((response2) => {
                            // console.log(response2, "resp dwa");

                            this.tablicadwa = response2.data;
                            axios
                                .get('/api/v1/recipes/all')
                                .then((response) => {
                                    console.log(response.data, 'informacje o przepisach');
                                    console.log(this.tablicadwa, 'zawartosc tablicy');



                                    for (let i = 0; i < this.tablicadwa.length; i++) {
                                        for (let b = 0; b < response.data.recipes.length; b++) {
                                            if (this.tablicadwa[i].recipe_id == response.data.recipes[b].id) {
                                                //console.log(response.data.recipes[b].name, "nazwa przepisu");
                                                //console.log(this.tablicadwa[i].quantity, 'ilosc przepisow quantity');

                                                let objectToPush = {
                                                    'nazwa_przepisu': response.data.recipes[b].name,
                                                    'ilosc_przepisu': this.tablicadwa[i].quantity,
                                                }
                                                this.gotowe.push(objectToPush);


                                            }
                                        }
                                    }
                                    //this.tablica[0].email = "email";
                                    //this.tablica[1].email = "emaillllll";
                                    console.log(this.tablica, 'tablica z tego miejsca xdx');
                                    //console.log(this.gotowe, 'co ma teraz gotowe ??');

                                    //tablicadwa mus iporownywac id do id z tablica

                                })
                                .catch((error) => {
                                    console.log(error);
                                })

                        })
                        .catch((error) => {
                            console.log(error);
                        })
                    //}


                })

                .catch((error) => {
                    console.log(error);
                });
        },










    },
};
</script>
