<template>
    <navbar></navbar>
    <div class="alert alert-danger" v-if="errors.length">
        <p v-for="error in errors" v-bind:key="error">
            {{ error }}
        </p>
    </div>

    <div class="alert alert-success" v-if="alert"> <!-- ALERT OD POMYSLNEJ ZMIANY LOGINU --->
        <p>
            {{ alert }}
        </p>
    </div>
    <div class="alert alert-danger" v-if="errorsUser.length"> <!-- ERROR OD NIEPOMYSLNEJ ZMIANY hasła --->
        <p v-for="error in errorsUser" v-bind:key="error">
            {{ error }}
        </p>
    </div>
    <section class="vh-100" style="background-color: #eee;">
        <div class="container py-1 h-75">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col col-lg-8 mb-4 mb-lg-0">
                    <div class="card mb-3" style="border-radius: .5rem;">
                        <div class="row g-0">
                            <div class="col-md-4 gradient-custom text-center text-white"
                                style="border-top-left-radius: .5rem; border-bottom-left-radius: .5rem;">
                                <h5 class="text-dark mt-5">{{ username }}</h5>
                                <p class="text-dark">{{ user.role }}</p>
                                <form @submit.prevent="ChangeAvatar">
                                    <div v-if="imagePreview.length === 0">
                                        <div v-if="user.get_image == '' ">
                                            <img  src="https://mdbootstrap.com/img/Photos/Others/placeholder-avatar.jpg" alt="" loading="lazy" class="img-fluid mt-5 mb-2 rounded" style="width: 120px; height: 120px" />
                                        </div>
                                        <div v-if="user.get_image != '' ">
                                            <img  :src="user.get_image" alt="" loading="lazy" class="img-fluid mt-5 mb-2 rounded" style="width: 120px; height: 120px" />
                                        </div>
                                    </div>
                                    <div v-if="imagePreview.length > 0">
                                        <img :src="imagePreview" alt="zdjecie" class="img-fluid my-5 rounded" style="width: 120px;height: 120px" />
                                    </div>
                                    <div>
                                        <div class="mt-1 mb-1">
                                            <MDBFile class="form-control d-none" label="Wybierz zdjęcie"
                                                @change="handleFileUpload($event)" id="image" accept=".jpg,.jpeg,.png" />
                                        </div>
                                    </div>
                                    <MDBBtn color="warning" class="btn-sm" type="submit">Zatwierdź zdjęcie</MDBBtn>
                                </form>

                            </div>
                            <div class="col-md-8">
                                <div class="card-body p-4">
                                    <h6>Informacje</h6>
                                    <hr class="mt-0 mb-4">
                                    <div class="row pt-1">
                                        <div class="col-6 mb-3">
                                            <h6>Email</h6>
                                            <p class="text-muted">{{ user.email }}</p>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <h6>Telefon</h6>
                                            <p class="text-muted">+48 {{ user.workplace }}</p>
                                        </div>
                                    </div>
                                    <h6>Zmiana danych</h6>
                                    <hr class="mt-0 mb-4">
                                    <div class="row pt-1">
                                        <div class="col-6">
                                            <h6>nazwa uzytkownika</h6>
                                            <form @submit.prevent="ChangeUsername">
                                                <MDBInput label="Nowa nazwe użytkownika" v-model="new_username" type="text"
                                                    required class="mb-1" />
                                                <MDBInput label="Powtórz nazwę użytkownika" v-model="re_new_username"
                                                    type="text" required class="mb-1" />
                                                <MDBInput label="Podaj hasło" type="password" v-model="loginCurrentPassword"
                                                    required class="mb-1" />
                                                <MDBBtn color="primary" type="submit" text="center">zmień nazwę</MDBBtn>
                                            </form>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <h6>hasło</h6>
                                            <form @submit.prevent="ChangePassword">
                                                <MDBInput label="stare haslo" type="password" v-model="current_password"
                                                    required class="mb-1" />
                                                <MDBInput label="nowe haslo" type="password" v-model="new_password" required
                                                    class="mb-1" />
                                                <MDBInput label="powtorz nowe haslo" type="password"
                                                    v-model="re_new_password" required class="mb-1" />
                                                <MDBBtn color="primary" type="submit">zmień hasło</MDBBtn>
                                            </form>
                                        </div>
                                    </div>

                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import HelloWorld from "@/components/HelloWorld.vue";
import Navbar from "@/components/ui/Navbar.vue";
import axios from "axios";
import {
    MDBBtn,
    mdbRipple,
    MDBCol,
    MDBRow,
    MDBContainer,
    MDBTable,
    MDBBadge,
    MDBCardTitle,
    MDBCardBody,
    MDBCard,
    MDBInput,
    MDBFile,
} from "mdb-vue-ui-kit";

export default {
    name: "Home",
    components: {
        MDBBtn,
        MDBCol,
        MDBRow,
        MDBContainer,
        MDBTable,
        MDBBadge,
        MDBCardTitle,
        MDBCardBody,
        MDBCard,
        MDBInput,
        MDBFile,
        HelloWorld,
        Navbar,
    },
    data() {
        return {
            user: {},
            id: "",
            username: "",
            image: "",
            imagePreview: "",
            new_username: "",
            re_new_username: "",
            current_password: "",
            loginCurrentPassword: "",
            new_password: "",
            re_new_password: "",
            alert: "",
            errors: [],
            errorsUser: [],

        };
    },
    directives: {
        mdbRipple,
    },
    mounted() {
        document.title = "Mój profil";
        this.getUser();
    },
    beforeMount() {
        this.username = this.getUsername;
        this.id = this.getId;
    },
    computed: {
        getUsername() {
            return this.$store.state.user.username;
        },
        getId() {
            return this.$store.state.user.id;
        },
    },
    methods: {
        getUser() {
            axios
                .get(`/api/v1/single_profile/${this.id}/`, {
                    //params: {id: product_id},
                    headers: {
                        Authorization: `Token ${this.$store.state.user.token}`
                    }
                })
                .then((response) => {
                    this.user = response.data;
                })
                .catch((error) => {
                    console.log(error);
                })
        },
        ChangeUsername() {
            this.alert = "";
            this.errorsUser = [];
            if (this.new_username === "") {
                this.errors.push("nowa nazwa jest zbyt krótka !");
            }
            if (this.new_username !== this.re_new_username) {
                this.errors.push("nazwy uzytkownika do siebie nie pasują !");
            }
            if (this.username === this.new_username) {
                this.errors.push("nazwa uzytkownika jest identyczne jak stara !");
            }
            if (!this.errors.length) {
                let formUsername = new FormData();
                formUsername.append("new_username", this.new_username);
                formUsername.append("re_new_username", this.re_new_username);
                formUsername.append("current_password", this.loginCurrentPassword);

                axios
                    .post(`/api/v1/users/set_username/`, formUsername, {
                        headers: {
                            Authorization: `Token ${this.$store.state.user.token}`,
                        },
                    })
                    .then((response) => {
                        this.$store.commit(
                            "setUsername", this.new_username
                        );
                        location.reload();
                        this.alert = "Pomyślnie zmieniono nazwe uzytkownika !";
                        this.alert = "pomyslnie zmieniono hasło ";
                        //this.$store.commit("setAlert", this.notification);
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            }
        },
        ChangePassword() {
            this.errors = [];
            if (this.new_password === "") {
                this.errors.push("hasło jest zbyt krótkie !");
            }
            if (this.new_password !== this.re_new_password) {
                this.errors.push("hasła do siebie nie pasują !");
            }
            if (this.new_password === this.current_password) {
                this.errors.push("nowe hasło jest identyczne jak stare !");
            }
            if (!this.errors.length) {
                let formPassword = new FormData();
                formPassword.append("current_password", this.current_password);
                formPassword.append("new_password", this.new_password);
                formPassword.append("re_new_password", this.re_new_password);

                axios
                    .post(`/api/v1/users/set_password/`, formPassword, {
                        headers: {
                            Authorization: `Token ${this.$store.state.user.token}`,
                        },
                    })
                    .then((response) => {
                        console.log(response, "dziala lol");
                        location.reload();
                        //this.notification = "pomyslnie zmieniono hasło ";
                        //this.$store.commit("setAlert", this.notification);
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            }
        },
        ChangeAvatar() {
            let formImage = new FormData();
            formImage.append('image', this.image);
            formImage.append('id', this.id);
            axios
                .put(`/api/v1/change_avatar/`, formImage, {
                    headers: {
                        Authorization: `Token ${this.$store.state.user.token}`,

                    }
                })
                .then((response) => {
                    console.log(response, "zmieniono zdjecie !");
                    location.reload();

                })
                .catch((error) => {
                    console.log(error);
                })
        },

        handleFileUpload(event) {
            var input = event.target;
            if (input.files && input.files[0]) {
                //! jesli mamy plik
                var reader = new FileReader();
                reader.onload = (e) => {
                    this.imagePreview = e.target.result;
                };
                reader.readAsDataURL(input.files[0]); //base 64
            }
            this.image = event.target.files[0];
        },
    },
};
</script>
