import { createStore } from 'vuex'

export default createStore({
  state: {
    user: {       //? obiekt uzytkownik - sesja
      username: '',
      id: '',
      isAuthenticated: false,
      token: '',
    }
  },
  mutations: { //! nie mozemy zmienic danych state i robimy to w mutations
    initializeStore (state){ //! funkcja inicjalizujaca nasz local storage
      if (localStorage.getItem('token')){ //token uzytkownika zapisany w localstorage gdy by wlaczyl przegladarke (dziala nawet gdy ktos ylaczy przegladarke czy kompa, maja date waznosci)
        state.user.token = localStorage.getItem('token') //przypisanie tokenu
        state.user.isAuthenticated = true
      } else {
        state.user.isAuthenticated = false
        state.user.token = ''
      }

      if (localStorage.getItem('username')) {
        state.user.username = localStorage.getItem('username')
      } else {
        state.user.username = ''
      }

      if (localStorage.getItem('id')) {
        state.user.id = localStorage.getItem('id')
      } else {
        state.user.id = ''
      }
    },
    setToken (state, token) { //! funcja przypisujaca token przy zalogowaniu
      state.user.token = token
      state.user.isAuthenticated = true
    },
    removeToken (state){
      state.user.token = ''
      state.user.isAuthenticated = false
    },
    setUserId(state, id){
      state.user.id = id
    },
    setUsername(state, username){
      state.user.username = username
    },
    logoutUser(state){ //! wylogowywanie
      state.user.username = ''
      state.user.id = 0
      state.user.token = ''
      state.user.isAuthenticated = false
      localStorage.removeItem('username') 
      localStorage.removeItem('id')
      localStorage.removeItem('token') 
    }
  },
















  actions: {
  },
  modules: {
  }
})
