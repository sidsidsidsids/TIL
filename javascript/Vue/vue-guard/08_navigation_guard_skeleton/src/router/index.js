import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView.vue'
import LoginView from '@/views/LoginView.vue'
import DogView from '@/views/DogView.vue'
import NotFound404View from '@/views/NotFound404'

Vue.use(VueRouter)
const isLoggedIn = true

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log('already login')
        next({ name:'home'}) // 로그인 되어 있으면 로그인 대신 홈으로        
      } else {
        next() // 로그인 안 되어 있으면 로그인으로 이동 가능
      }
    }
  },
  {
    path: '/dog/:breed',
    name: 'dog',
    component: DogView,
  },
  {
    path: '*',
    redirect: '/404',
    component: NotFound404View
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// // router/index.js
// router.beforeEach((to, from, next) => {
//   // CODE HERE
//   // console.log('to',to)
//   // console.log('from',from)
//   // console.log('next',next)
  
//   // 로그인 여부
//   // const isLoggedIn = True
//   const isLoggedIn = false
  
//   // 로그인 필요 페이지 지정
//   // const authPages = ['hello']
//   const allowAuthPages = ['login']
  
//   // 앞으로 이동할 페이지가 로그인이 필요한 페이지인지 확인
//   // const isAuthRequired = authPages.includes(to.name)
//   const isAuthRequired = !allowAuthPages.includes(to.name)

//   if (isAuthRequired && !isLoggedIn) {
//     console.log('Login으로 이동하기')
//     next({ name: 'login' })
//   } else {
//     console.log('to로 이동하기')
//     next()
//   }
// })

export default router
