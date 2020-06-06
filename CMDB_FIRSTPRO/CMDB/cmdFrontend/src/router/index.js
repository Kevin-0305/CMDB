import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import UsersList from '../components/users/UsersList'
import server from '../components/server/server'
import index from '../components/index'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      name: 'users',
      path: '/users',
      component: UsersList
    },
    {
      name: 'server',
      path: '/server',
      component: server
    }
  ]
})
