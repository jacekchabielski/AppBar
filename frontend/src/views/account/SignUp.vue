<template>
    <section class="vh-100" style="background-color: #eee;">
        <div class="container h-100">
          <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-lg-12 col-xl-11">
              <div class="card text-black" style="border-radius: 25px;">
                <div class="card-body p-md-5">
                  <div class="row justify-content-center">
                    <div class="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">
      
                      <p class="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">Rejestrowanie pracownika</p>
      
                      <form class="mx-1 mx-md-4" @submit.prevent = "submitForm">
      
                        <div class="d-flex flex-row align-items-center mb-4">
                          <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                          <div class="form-outline flex-fill mb-0">
                            <input type="text" id="login" class="form-control" v-model="username" />
                            <label class="form-label" for="form3Example1c">Login</label>
                          </div>
                        </div>

                        <div class="d-flex flex-row align-items-center mb-4">
                          <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                          <div class="form-outline flex-fill mb-0">
                            <input type="text" id="first_name" class="form-control" v-model="first_name" />
                            <label class="form-label" for="form3Example1c">imie</label>
                          </div>
                        </div>

                        <div class="d-flex flex-row align-items-center mb-4">
                          <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                          <div class="form-outline flex-fill mb-0">
                            <input type="text" id="last_name" class="form-control" v-model="last_name" />
                            <label class="form-label" for="form3Example1c">nazwisko</label>
                          </div>
                        </div>

                        <div class="d-flex flex-row align-items-center mb-4">
                          <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                          <div class="form-outline flex-fill mb-0">
                            <input type="email" id="email" class="form-control" v-model="email" />
                            <label class="form-label" for="form3Example1c">email</label>
                          </div>
                        </div>

                        <div class="d-flex flex-row align-items-center mb-4">
                          <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                          <div class="form-outline flex-fill mb-0">
                            <input type="text" id="login" class="form-control" v-model="role" />
                            <label class="form-label" for="form3Example1c">Role</label>
                          </div>

                        </div>
                        <div class="d-flex flex-row align-items-center mb-4">
                          <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                          <div class="form-outline flex-fill mb-0">
                            <input type="text" id="login" class="form-control" v-model="workplace" />
                            <label class="form-label" for="form3Example1c">Workplace</label>
                          </div>
                        </div>
      
      
                        <div class="d-flex flex-row align-items-center mb-4">
                          <i class="fas fa-lock fa-lg me-3 fa-fw"></i>
                          <div class="form-outline flex-fill mb-0">
                            <input type="password" id="password" class="form-control" v-model="password" />
                            <label class="form-label" for="form3Example4c">Haslo</label>
                          </div>
                        </div>

                        <div class="d-flex flex-row align-items-center mb-4">
                          <i class="fas fa-key fa-lg me-3 fa-fw"></i>
                          <div class="form-outline flex-fill mb-0">
                            <input type="password" id="password2" class="form-control" v-model="password2" />
                            <label class="form-label" for="form3Example4cd">Repeat your password</label>
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
export default {
  name: 'SignUp',
  data() {
    return {
      username: '',
      first_name: '',
      last_name: '',
      email: '',
      role: '',
      workplace: '',
      password: '',
      password2: '',
      errors: [],
    }
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
                    
                      .put('/api/v1/profile_register/',ProfileData)
                      .then(response =>{
                        console.log(response)
                      })
                      .catch(error =>{
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
<style>

</style>