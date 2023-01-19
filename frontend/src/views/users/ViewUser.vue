<template>
    <navbar></navbar>
    <div class="mt-4">
    <MDBBtn color="primary" class="float-end mb-2 mx-3"  @click="$router.push('SignUp')" rounded><i class="fas fa-user-plus me-2"></i>Dodaj nowego pracownika </MDBBtn>
    <MDBTable class="align-middle mb-0 bg-white">
        <thead class="bg-light">
            <tr>
                <th>Pracownik</th>
                <th>Rola</th>
                <th>Status</th>
                <th>Position</th>
                <th>Akcje</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="profile in profiles.profiles" v-bind:key="profile.id">
                <td>
                    <div class="d-flex align-items-center">
                        <i v-if="profile.get_image == '' " class="fas fa-user-alt fa-2xl"></i>
                        <img v-else :src="profile.get_image" style="width: 2rem" class="img-fluid rounded" alt="...">
                        <div class="ms-3">
                            <p class="fw-bold mb-1">{{ profile.first_name }} {{ profile.last_name }}</p>
                            <p class="text-muted mb-0">{{profile.email}}</p>
                        </div>
                    </div>
                </td>
                <td>
                    <p class="fw-normal mb-1">{{ profile.role }}</p>
                    <p class="text-muted mb-0">{{ profile.workplace }}</p>
                </td>
                <td>
                    <MDBBadge badge="success" pill class="d-inline">Pracuje</MDBBadge>
                </td>
                <td>Starszy</td>
                <td>
                    <MDBBtn color="link" size="sm" rounded>
                        Edit
                    </MDBBtn>
                </td>
            </tr>
            
        </tbody>
    </MDBTable>
</div>
</template>

<script>
import HelloWorld from "@/components/HelloWorld.vue";
import Navbar from "@/components/ui/Navbar.vue";
import axios from "axios";
import {MDBBtn, mdbRipple, MDBCol, MDBRow, MDBContainer, MDBTable, MDBBadge } from "mdb-vue-ui-kit";

export default {
    name: "Home",
    components: {
        MDBBtn,
        MDBCol,
        MDBRow,
        MDBContainer,
        MDBTable,
        MDBBadge,
        HelloWorld,
        Navbar,
    },
    data() {
        return {
            profiles: [],
        }
    },
    directives: {
        mdbRipple
    },
    mounted() {
        document.title = 'Użytkownicy'
        this.getProfiles();

    },
    methods:{
        async getProfiles() {
            axios
                .get('/api/v1/all_profiles/')
                .then((response)=>{
                    this.profiles = response.data;
                    console.log(response, 'uzytkownicy')
                })
                .catch((error)=>{
                    console.log(error)
                })
        }
    }
};
</script>