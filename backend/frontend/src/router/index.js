import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import CompareMaterial from '../views/CompareMaterial.vue'
// import MaterialResultComponent from '../views/MaterialResultComponent.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/compare-material',
    name: 'compareMaterial',
    component: CompareMaterial
  },
  // {
  //   path: '/best-materials',
  //   name: 'bestMaterials',
  //   component: MaterialResultComponent
  // },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
]

const router = createRouter({
  history: createWebHistory("/"),
  routes
})

export default router
