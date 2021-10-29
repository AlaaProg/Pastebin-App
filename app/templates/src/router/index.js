import Vue from 'vue'
import VueRouter from 'vue-router'
import store from "./../store"

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import(/* webpackChunkName: "about" */ '../views/Home.vue'),
    meta: {
      isAuth: true
    }
  },
  {
    path: '/login',
    name: 'Login',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Login.vue'),
    meta: {
      isAuth: false
    }
  },
  {
    path: '/text/:hash',
    name: 'TextView',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/TextView.vue'),
    meta: {
      isAuth: true
    }
  },
  {
    path: '/register',
    name: 'register',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Register.vue'),
    meta: {
      isAuth: false
    }
  }
]




const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.isAuth)) {
    if (localStorage.getItem("auth_token") != null) {
      store.commit("setToken", localStorage.getItem("auth_token"))
      if (!store.state.isLogin) {
        store.dispatch("user")
          .then( () => {
            next()
          }).catch( ()=>{
            store.dispatch("logout")
            next("login")
          })
      } else {
        next()
      }
    } else {
      store.dispatch("logout")
      next("login")
    }
  } else {
    if (store.state.isLogin && to.meta.isAuth == false) {
      next("/")
    } else {
      next()
    }
  }

})

export default router
