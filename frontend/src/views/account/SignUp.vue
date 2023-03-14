<template>
  <section class="vh-100" style="background-color: #eee;">
    <div class="container h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-lg-12 col-xl-11">
          <div class="card text-black" style="border-radius: 25px;">
            <div class="card-body p-md-5">
              <div class="row justify-content-center">
                <div class="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">

                  <p class="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">Rejestracja pracownika</p>

                  <form class="mx-1 mx-md-4" @submit.prevent="submitForm">

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <MDBInput type="text" label="login" id="login" class="form-control" v-model="username" />
                      </div>
                    </div>

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <MDBInput type="text" label="imie" id="first_name" class="form-control" v-model="first_name" />
                      </div>
                    </div>

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <MDBInput type="text" label="nazwisko" id="first_name" class="form-control" v-model="last_name" />
                      </div>
                    </div>

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <MDBInput type="email" id="email" label="email" class="form-control" v-model="email" />
                      </div>
                    </div>

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <select class="form-select" id="login" aria-label="Default select example" v-model="role">
                          <option value="Kucharz">wybierz role</option>
                          <option value="Kucharz">Kucharz</option>
                          <option value="Sprzedawca">Sprzedawca</option>
                          <option value="Kierownik">Kierownik</option>
                        </select>
                      </div>
                    </div>


                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-lock fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <MDBInput type="password" id="password" label="hasło" class="form-control" v-model="password" />
                      </div>
                    </div>

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-key fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <MDBInput type="password" id="password2" label="Powtórz hasło" class="form-control" v-model="password2" />
                      </div>
                    </div>

                    <div class="d-flex justify-content-center">
                      <button type="submit" class="btn btn-primary btn-lg">Dodaj nowego pracownika</button>
                    </div>
                    <router-link to="/ViewUser">powrót</router-link>

                  </form>
                  <div class="alert alert-danger" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                  </div>

                </div>
                <div class="col-md-10 col-lg-6 col-xl-7 d-flex align-items-center order-1 order-lg-2">

                  <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-registration/draw1.webp"
                    class="img-fluid" alt="Sample image">

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
import axios from 'axios'
import { MDBInput } from 'mdb-vue-ui-kit';
export default {
  name: 'SignUp',
  data() {
    return {
      username: '',
      first_name: '',
      last_name: '',
      email: '',
      role: '',
      password: '',
      password2: '',
      errors: [],
    }
  },
  components: {
    MDBInput,
  },
  mounted() {
    document.title = 'Rejestracja pracownika'
  },
  methods: {
    submitForm() {
      this.errors = []
      if (this.username === '') {
        this.errors.push('nie podano nazwy uzytkownika !')
      }
      if (this.password === '') {
        this.errors.push('hasło jest za krótkie !')
      }
      if (this.password !== this.password2) {
        this.errors.push('hasła do siebie nie pasują !')
      }

      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password,

        }
        let ProfileData = new FormData();
        ProfileData.append('first_name', this.first_name);
        ProfileData.append('last_name', this.last_name);
        ProfileData.append('role', this.role);
        ProfileData.append('workplace', this.workplace);
        ProfileData.append('email', this.email);
        axios
          .post('/api/v1/users/', formData)
          .then(response => {
            //setTimeout(() => { this.alertMessage = ""; }, 4300);
            axios

              .put('/api/v1/profile_register/', ProfileData)
              .then(response => {
                console.log(response)
              })
              .catch(error => {
                console.log(error)
              })
            this.$router.push('/ViewUser')
          })
          .catch(error => {
            if (error.response) {
              console.log(JSON.stringify(error.response.data))
            } else if (error.message) {
              this.errors.push('Something went wrong. Please try again')

              console.log(JSON.stringify(error))
            }
          })
      }
    }
  }

}
</script>
<style></style>