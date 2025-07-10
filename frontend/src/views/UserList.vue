<template>
  <div class="flex min-h-screen">
    <Sidebar />
    <div class="flex-1 p-6 bg-lightgray">
      <h1 class="text-3xl font-bold mb-6 text-dark">All Users</h1>
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        <div
          v-for="user in users"
          :key="user.id"
          @click="goToUser(user.id)"
          class="bg-white p-5 rounded-xl shadow hover:shadow-lg cursor-pointer flex flex-col items-center transition-all"
        >
          <img :src="`https://i.pravatar.cc/150?img=${user.id}`" class="w-24 h-24 rounded-full object-cover border mb-4" />
          <h2 class="text-xl font-semibold text-center text-dark">{{ user.name }}</h2>
          <p class="text-sm text-muted">{{ user.email }}</p>
          <p class="text-sm text-muted mt-2">📍 {{ user.address.street }}, {{ user.address.city }}</p>
          <p class="text-sm text-muted">🏢 {{ user.company.name }}</p>
          <p class="text-sm text-primary underline">🌐 {{ user.website }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Sidebar from './components/SideBar.vue'

const users = ref([])
const router = useRouter()

onMounted(async () => {
  const res = await fetch('https://jsonplaceholder.typicode.com/users')
  users.value = await res.json()
})

const goToUser = (id) => {
  router.push(`/user/${id}/todos`)
}
</script>
