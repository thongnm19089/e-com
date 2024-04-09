import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

// eslint-disable-line
const pathToRegexpOptions = {
  sensitive: true,
  strict: true
}
const Product = () =>
  import(
    '../pages/product/index.vue'
  ).then((m) => m.default || m)

const PageNotFound = () =>
  import(
    '../pages/notfound.vue'
  ).then((m) => m.default || m)

const Home = () =>
  import(
    '../pages/home/index.vue'
  ).then((m) => m.default || m)

export default new Router({
  mode: 'history',
  scrollBehavior (to, from, savePosition) {
    if (savePosition) {
      return savePosition
    }

    if (to.hash) {
      return {
        selector: to.hash
      }
    }

    return { x: 0, y: 0 }
  },
  routes: [
    {
      path: '/',
      component: Home,
      props: true,
      pathToRegexpOptions
    },
    {
      path: '/product/:id',
      component: Product,
      props: true,
      pathToRegexpOptions
    },
    { path: '/404', component: PageNotFound },
    { path: '*', redirect: '/404' }
  ]
})
