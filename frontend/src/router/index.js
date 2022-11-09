import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import SignUp from '../views/account/SignUp.vue'
import Login from '../views/account/Login.vue'
import store from '../store'
import Logout from '../views/account/Logout.vue'
import AddProduct from '../views/product/AddProduct.vue'
import ViewProduct from '../views/product/ViewProduct.vue'
import EditProduct from '../views/product/EditProduct.vue'
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home, 
    meta: { requireLogin: true}
  },
  {
    path: '/addProduct',
    name: 'addProduct',
    component: AddProduct, 
    meta: { requireLogin: true}
  },
  {
    path: '/ViewProduct',  //! url do wszystkich produktow
    name: 'ViewProduct',
    component: ViewProduct, 
    meta: { requireLogin: true},
    props: true
  },
  {
    path: '/EditProduct/:id/', //! url do edycji konkretnego produktu
    name: 'EditProduct',
    component: EditProduct, 
    meta: { requireLogin: true}
  },
  {
    path: '/about',
    name: 'About',
    meta: { requireLogin: true},
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/SignUp',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/Login',
    name: 'Login',
    component: Login
  },
  {
    path: '/Logout',
    name: 'Logout',
    component: Logout
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach ((to, from, next) => { //! zanim router wykona jakies przekierowanie na inna strone
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.user.isAuthenticated) { //!jesli strona wymaga logowania i nie jestesmy authenticated
    next ('/Login') //! to przenies z automatu na strone logowania
  }else {
    next () //! jesli jestesmy zalogowani, to przenies na strone docelowa
  }
})

export default router
