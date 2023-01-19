<template>
    <navbar></navbar>
    <MDBContainer>
        <div class="col-md-12">
            <div></div>
        </div>
        <p>witaj {{ username }}</p>                             <!-- ERROR OD NIEPOMYSLNEJ ZMIANY UZYTKOWNIKA --->
        <div class="alert alert-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">
                {{ error }}
            </p>
        </div>

        <div class="alert alert-success" v-if="alert">          <!-- ALERT OD POMYSLNEJ ZMIANY LOGINU --->
            <p>
                {{ alert }}
            </p>
        </div>
        <div class="alert alert-danger" v-if="errorsUser.length"> <!-- ERROR OD NIEPOMYSLNEJ ZMIANY hasła --->
            <p v-for="error in errorsUser" v-bind:key="error">
                {{ error }}
            </p>
        </div>
        <MDBCard>
            <MDBCardBody>
                <form @submit.prevent="ChangeUsername">
                    <MDBCardTitle>Edycja nazwy uzytkownika</MDBCardTitle>
                    <MDBInput label="podaj nowa nazwe uzytkownika" v-model="new_username" type="text" required />
                    <MDBInput label="powtorz nowa nazwe uzytkownika" v-model="re_new_username" type="text" required />
                    <MDBInput label="Podaj haslo" type="password" v-model="loginCurrentPassword" required />
                    <MDBBtn color="primary" type="submit">zmień</MDBBtn>
                </form>
            </MDBCardBody>
        </MDBCard>
        <MDBCard>
            <MDBCardBody>
                <form @submit.prevent="ChangePassword">
                    <MDBCardTitle>Edycja hasła</MDBCardTitle>
                    <MDBInput label="stare haslo" type="password" v-model="current_password" required />
                    <MDBInput label="nowe haslo" type="password" v-model="new_password" required />
                    <MDBInput label="powtorz nowe haslo" type="password" v-model="re_new_password" required />
                    <MDBBtn color="primary" type="submit">zmień</MDBBtn>
                </form>
            </MDBCardBody>
        </MDBCard>
        <MDBCard>
            <MDBCardBody>
                <form @submit.prevent="ChangeAvatar">
                    <MDBCardTitle>Edycja avatara</MDBCardTitle>
                    <div v-if="imagePreview.length === 0">
                        <img src="https://mdbootstrap.com/img/Photos/Others/placeholder-avatar.jpg"
                            class="rounded-circle" alt="example placeholder" style="width: 200px" />
                    </div>
                    <div v-if="imagePreview.length > 0">
                        <img :src="imagePreview" alt="zdjecie" class="rounded-circle" style="width: 200px" />
                    </div>
                    <div>
                        <div class="btn btn-primary btn-rounded">
                            <MDBFile class="form-control d-none" label="zdjecie" @change="handleFileUpload($event)"
                                id="image" accept=".jpg,.jpeg,.png" />
                        </div>
                    </div>
                    <MDBBtn color="primary" type="submit">zmień</MDBBtn>
                </form>
            </MDBCardBody>
        </MDBCard>
    </MDBContainer>
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
    },
    beforeMount(){
        this.username = this.getUsername;
        this.id = this.getId;
    },
    computed: {
    getUsername(){
        return this.$store.state.user.username;
    },
    getId(){
        return this.$store.state.user.id;
    },
    },
    methods: {
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
                        console.log(response,"dziala zmiana nazwy uzytkownika");
                        this.$store.commit(
                        "setUsername",this.new_username
                        );
                        location.reload();
                        this.alert="Pomyślnie zmieniono nazwe uzytkownika !";
                        //this.notification = "pomyslnie zmieniono hasło ";
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
                        console.log(response,"dziala lol");
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
