<template>
    <navbar></navbar>
    <div class="mt-4">
    <MDBBtn color="primary" class="float-end mb-2 mx-3"  @click="$router.push('SignUp')" rounded><i class="fas fa-user-plus me-2"></i>Dodaj nowego pracownika </MDBBtn>
    <MDBTable class="align-middle mb-0 bg-white">
        <thead class="bg-light">
            <tr>
                <th>Pracownik</th>
                <th>Rola</th>
                <th>Kontakt</th>
                <th class="text-center">Akcje</th>
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
                </td>
                <td>
                    +48 {{profile.workplace}}
                </td>
                <td class="text-center">
                    <MDBBtn color="danger" size="sm" class="text-right" v-if="profile.role != 'Kierownik'" rounded  @Click="setId(profile.id)">
                        Usuń pracownika
                    </MDBBtn>
                </td>
            </tr>
            
        </tbody>
    </MDBTable>
    
</div>
<div class="modal" id="myModal" :class="{ 'show-modal': actualId }" v-show="actualId">
    <div class="modal-dialog">
        <div class="modal-content">
            <!-- Modal Header -->
            <div class="modal-header">
                <h4 class="modal-title">Czy na pewno chcesz usunąć ?</h4>
                <button type="button" class="btn-close" v-on:click="actualId = null"></button>
            </div>

            <!-- Modal body -->
            <div class="modal-body">Usuniesz pracownika</div>

            <!-- Modal footer -->
            <div class="modal-footer">
                <button type="button" class="btn btn-danger" v-on:click="deleteProduct(actualId)">
                    Usuń
                </button>
                <button type="button" class="btn margin-left" v-on:click="actualId = null">
                    powrót
                </button>
            </div>
        </div>
    </div>
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
            actualId: "",
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
        },
        setId(id) {
            this.actualId = id;
            console.log(this.actualId, "dd");
        },
        async deleteProduct(id) {
            console.log(id, "delete user id");
            axios
                .delete(`/api/v1/single_profile/${id}/`, {
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
    }
};
</script>