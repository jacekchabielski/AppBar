<template>
    <navbar></navbar>
    <MDBContainer>
        <MDBCard class="bg-light mt-4">
            <MDBCardHeader><h4>Podsumowanie</h4></MDBCardHeader>
            <MDBCardBody>
                <div class="row">
                    <MDBCard class="col-md-3">
                        <MDBCardBody>
                            <div class="row">
                                <div class="col-md-10">
                                    <MDBCardTitle><p class="text-primary">Dzisiejszy przychód </p></MDBCardTitle>
                                    <MDBCardText>
                                        0 zł 
                                    </MDBCardText>
                                </div>
                                <div class="col-md-2 mt-2">
                                    <h1><i class="fas fa-coins"></i></h1>
                                </div>
                            </div>
                        </MDBCardBody>
                    </MDBCard>
                    <MDBCard class="col-md-3 ">
                        <MDBCardBody>
                            <MDBCardTitle><p class="text-success">Wczorajszy przychód</p></MDBCardTitle>
                            <MDBCardText>
                                0 zł
                            </MDBCardText>
                        </MDBCardBody>
                    </MDBCard>
                    <MDBCard class="col-md-3 ">
                        <MDBCardBody>
                            <MDBCardTitle><p class="text-info">Tygodniowy przychód</p></MDBCardTitle>
                            <MDBCardText>
                                0 zł
                            </MDBCardText>
                        </MDBCardBody>
                    </MDBCard>
                    <MDBCard class="col-md-3">
                        <MDBCardBody>
                            <MDBCardTitle><p class="text-warning">Miesięczny przychód</p></MDBCardTitle>
                            <MDBCardText>
                                0 zł
                            </MDBCardText>
                        </MDBCardBody>
                    </MDBCard>
                </div>
            </MDBCardBody>
        </MDBCard>
    </MDBContainer>
</template>

<script>
import HelloWorld from "@/components/HelloWorld.vue";
import Navbar from "@/components/ui/Navbar.vue";
import { MDBBtn, mdbRipple, MDBCol, MDBRow, MDBContainer, MDBTable, MDBBadge, MDBCard, MDBCardHeader, MDBCardBody, MDBCardTitle } from "mdb-vue-ui-kit";

export default {
    name: "Home",
    components: {
        MDBBtn,
        MDBCol,
        MDBRow,
        MDBContainer,
        MDBTable,
        MDBBadge,
        MDBCard,
        MDBCardHeader,
        MDBCardBody,
        MDBCardTitle,
        HelloWorld,
        Navbar,
    },
    data() {
        return {
        }
    },
    directives: {
    },
    mounted() {
        document.title = 'Użytkownicy'

    },
    beforeMount() {
        
    },
    computed: {
    }
    
};

</script>