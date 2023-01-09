<template>
    <navbar></navbar>
    <div class="mt-4">
    <MDBBtn color="primary" class="float-end mb-2 mx-3" rounded><i class="fas fa-user-plus me-2"></i> Dodaj nowego pracownika</MDBBtn>
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
            <tr>
                <td>
                    <div class="d-flex align-items-center">
                        <img src="https://mdbootstrap.com/img/new/avatars/8.jpg" alt=""
                            style="width: 45px; height: 45px" class="rounded-circle" />
                        <div class="ms-3">
                            <p class="fw-bold mb-1">John Doe</p>
                            <p class="text-muted mb-0">john.doe@gmail.com</p>
                        </div>
                    </div>
                </td>
                <td>
                    <p class="fw-normal mb-1">Kucharz</p>
                    <p class="text-muted mb-0">Kuchnia</p>
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
            <tr>
                <td>
                    <div class="d-flex align-items-center">
                        <img src="https://mdbootstrap.com/img/new/avatars/6.jpg" class="rounded-circle" alt=""
                            style="width: 45px; height: 45px" />
                        <div class="ms-3">
                            <p class="fw-bold mb-1">Alex Ray</p>
                            <p class="text-muted mb-0">alex.ray@gmail.com</p>
                        </div>
                    </div>
                </td>
                <td>
                    <p class="fw-normal mb-1">Sprzedawca / Kelner</p>
                    <p class="text-muted mb-0">Kasa / Sala</p>
                </td>
                <td>
                    <MDBBadge badge="primary" pill class="d-inline">urlop</MDBBadge>
                </td>
                <td>Początkujący</td>
                <td>
                    <MDBBtn color="link" size="sm" rounded class="fw-bold" :ripple="{ color: 'dark' }">
                        Edit
                    </MDBBtn>
                </td>
            </tr>
            <tr>
                <td>
                    <div class="d-flex align-items-center">
                        <img src="https://mdbootstrap.com/img/new/avatars/7.jpg" class="rounded-circle" alt=""
                            style="width: 45px; height: 45px" />
                        <div class="ms-3">
                            <p class="fw-bold mb-1">Kate Hunington</p>
                            <p class="text-muted mb-0">kate.hunington@gmail.com</p>
                        </div>
                    </div>
                </td>
                <td>
                    <p class="fw-normal mb-1">Kelner</p>
                    <p class="text-muted mb-0">Sala</p>
                </td>
                <td>
                    <MDBBadge badge="warning" pill class="d-inline">nie pracuje</MDBBadge>
                </td>
                <td>Starszy</td>
                <td>
                    <MDBBtn color="link" size="sm" rounded class="fw-bold" :ripple="{ color: 'dark' }">
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
            username: '',
        }
    },
    directives: {
        mdbRipple
    },
    mounted() {
        document.title = 'Użytkownicy'

    },
    beforeMount() {
        this.username = this.getUsername;
    },
    computed: {
        getUsername() {
            return this.$store.state.user.username;
        }
    }
};
</script>