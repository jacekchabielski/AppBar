<template>
    <section class="vh-100" style="background-color: #eee;">
        <div class="container h-100">
          <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-lg-12 col-xl-11">
              <div class="card text-black" style="border-radius: 25px;">
                <div class="card-body p-md-5">
                  <div class="row justify-content-center">
                    <div class="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">
      
                      <p class="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">Logowanie</p>
      
                      <form class="mx-1 mx-md-4" @submit.prevent = "submitForm">
      
                        <div class="d-flex flex-row align-items-center mb-4">
                          <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                          <div class="form-outline">
                            
                            <input type="text" id="login" class="form-control" v-model="username" />
                            <label class="form-label" for="form3Example1c">Login</label>
                          </div>
                        </div>
      
      
                        <div class="d-flex flex-row align-items-center mb-4">
                          <i class="fas fa-lock fa-lg me-3 fa-fw"></i>
                          <div class="form-outline flex-fill mb-0">
                            <input type="password" id="password" class="form-control" v-model="password" />
                            <label class="form-label" for="form3Example4c">Haslo</label>
                          </div>
                        </div>

       
      
                        <div class="d-flex justify-content-center">
                          <button type="submit" class="btn btn-primary btn-lg">Zaloguj</button>
                        </div>
                        
                      </form>
                     

                    </div>
                    <div class="col-md-10 col-lg-6 col-xl-7 d-flex align-items-center order-1 order-lg-2">
      
                      <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-registration/draw1.webp"
                        class="img-fluid" alt="Sample image">
      
                    </div>

                                        <!-- Alerty -->
                                        <div class="alert alert-danger" v-if="errors.length">
                                          <p v-for="error in errors" v-bind:key="error">
                                            {{ error }}
                                          </p>
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
    data () {
        return {
            username: '',
            password: '',
            token: '',
            errors: []
        }
    },

    mounted() {
        document.title = 'logowanie'
    },

    methods: {
        async submitForm() {
            axios.defaults.headers.common.Authorization = '' // resetowanie
            localStorage.removeItem('token') //resetowanie cd

            const formData = {
                username: this.username,
                password: this.password
            }

            await axios
                .post('/api/v1/token/login/', formData)
                .then((response) => {
                    this.token = response.data.auth_token //odbieramy token z serwera (backend)
                    this.$store.commit('setToken', this.token) // uruchamiamy metode i przekazujemy od niej token
                    this.$store.commit('setUsername', this.username)
                    axios.defaults.headers.common.Authorization = 'Token' + this.token 
                    localStorage.setItem('token', this.token) //zapis do sesji
                    localStorage.setItem('username', this.username)

                    axios
                        .get('/api/v1/users/me', {
                            headers: {
                                Authorization: `Token ${this.token}`
                            }
                        })
                        .then((response) => {
                            this.$store.commit('setUserId', response.data.id)
                            localStorage.setItem('id', response.data.id)
                            window.location.href = '/'
                        })
                        .catch((error) =>{
                            console.log(error)
                        })

                        
                  
                    
                })
                .catch(error => {
                  if (error.response) {
                    this.errors = []
                    for (const property in error.response.data) {
                      this.errors.push(`${error.response.data[property]}`) // doddajemy do tablicy błędów
                    }
                  } else {
                    this.errors.push('Ups coś poszło nie tak. Spróbuj ponownie')

                    console.log(JSON.stringify(error))
                  }
                })
        }
    }
}
</script>