<template>
  <div class="flex min-h-screen text-gray-800 bg-gray-50">
    <Sidebar :user="user" />
    <main class="flex-1 p-6 overflow-y-auto">
      <router-view />
    </main>
  </div>
</template>

<script setup>
import Sidebar from './components/SideBar.vue'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const userId = route.params.id
const user = ref({})

onMounted(async () => {
  const res = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}`)
  user.value = await res.json()
})
</script>
