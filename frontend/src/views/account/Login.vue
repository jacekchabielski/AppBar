<template>

  <section class="vh-100" style="background-color: #eee;">
    <div class="container h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-lg-12 col-xl-11">
          <div class="card" style="border-radius: 25px;">
            <div class="card-body p-md-5" style="border-radius: 25px;">
              <div class="row justify-content-center">
                <div class="col-md-10 col-lg-6 col-xl-5 order-2§ order-lg-1">

                  <p class="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">Logowanie</p>

                  <form class="mx-1 mx-md-4" @submit.prevent="submitForm">

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-user fa-lg me-3 fa-fw"></i>

                      <div class="form-outline card flex-fill mb-0">
                        <MDBInput type="text" label="login" id="login" class="form-control" v-model="username" />


                      </div>
                    </div>


                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-lock fa-lg me-3 fa-fw"></i>
                      <div class="form-outline card flex-fill mb-0">
                        <MDBInput type="password" label="haslo" id="password" class="form-control" v-model="password" />

                      </div>
                    </div>




                    <div class="d-flex justify-content-center">
                      <button type="submit" class="btn btn-primary btn-lg">Zaloguj</button>

                    </div>

                  </form>
                  

                </div>
                <div class="col-md-10 col-lg-6 col-xl-7 d-flex align-items-center order-1 order-lg-2">

                  <MDBTable>
                    <thead>
                      <tr>
                        <th scope="col">#</th>
                        <th scope="col">Login</th>
                        <th scope="col">Haslo</th>
                        <th scope="col">Rola</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <th scope="row">1</th>
                        <td>KucharzMarcin</td>
                        <td>haslo123!</td>
                        <td>Kucharz</td>
                      </tr>
                      <tr>
                        <th scope="row">2</th>
                        <td>MarcinKierownik</td>
                        <td>haslo123!</td>
                        <td>Kierownik</td>
                      </tr>
                      <tr>
                        <th scope="row">3</th>
                        <td>SprzedawcaWojtek</td>
                        <td>haslo123!</td>
                        <td>Sprzedawca</td>
                      </tr>
                    </tbody>
                  </MDBTable>

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
    <!-- -->

  </section>

</template>

<script>
import { MDBInput, MDBTable } from 'mdb-vue-ui-kit';
import axios from 'axios'
export default {
  data() {
    return {
      username: '',
      password: '',
      token: '',
      id: '',
      errors: []
    }
  },
  components: {
    MDBInput,
    MDBTable,
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

              axios
                .get(`/api/v1/single_profile/${response.data.id}/`, {
                    //params: {id: product_id},
                    headers: {
                        Authorization: `Token ${this.$store.state.user.token}`
                    }
                })
                .then((response2) => {
            
                    if(response2.data.role === 'Kucharz'){
                      window.location.href = '/Kitchen'
                    }
                    if(response2.data.role === 'Sprzedawca'){
                      window.location.href = '/'
                    }
                    if(response2.data.role === 'Kierownik'){
                      window.location.href = '/ViewUser'
                    }
                })
                .catch((error) => {
                    console.log(error);
                })
              //window.location.href = '/'
            })
            .catch((error) => {
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