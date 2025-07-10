import { createRouter, createWebHistory } from 'vue-router'
import UserList from '../views/UserList.vue'
import UserDetail from '../views/UserDetail.vue'
import UserTodos from '../views/components/UserTodos.vue'
import UserPosts from '../views/components/UserPosts.vue'
import UserAlbums from '../views/components/UserAlbums.vue'
import GoAlbums from '../views/components/GoAlbums.vue'

const routes = [
  {
    path: '/',
    component: UserList,
  },
  {
    path: '/user/:id',
    component: UserDetail,
    children: [
      { path: '', redirect: 'todos' },
      { path: 'todos', component: UserTodos },
      { path: 'posts', component: UserPosts },
      { path: 'albums', component: UserAlbums },
      { path: 'albums/:albumId', component: GoAlbums },
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
