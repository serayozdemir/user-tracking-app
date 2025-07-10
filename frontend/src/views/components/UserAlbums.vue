<template>
  <div>
    <RouterLink to="/" class="inline-block mb-4 text-green-500 hover:underline">
      ← Go Home
    </RouterLink>

    <h1 class="text-xl font-bold mb-6 text-gray-800">Albums</h1>

    <div class="flex flex-wrap gap-6">
      <RouterLink
        v-for="album in albums"
        :key="album.id"
        :to="`/user/${userId}/albums/${album.id}`"
        class="block border rounded-lg shadow-sm bg-white hover:shadow-md transition-all p-2 w-[180px] md:w-[200px]"
      >
        <div class="grid grid-cols-2 gap-1 aspect-square">
          <div
            v-for="i in 4"
            :key="i"
            class="overflow-hidden rounded-sm"
          >
            <img
              :src="`https://picsum.photos/seed/${album.id}-${i}/300`"
              alt="Album photo"
              class="w-full h-full object-cover"
            />
          </div>
        </div>
        <div class="mt-2 px-1">
          <h3 class="text-sm font-medium text-gray-700 truncate">
            {{ album.title }}
          </h3>
        </div>
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const userId = route.params.id

const user = ref({})
const albums = ref([])

onMounted(async () => {
  const [userRes, albumsRes] = await Promise.all([
    fetch(`https://jsonplaceholder.typicode.com/users/${userId}`).then(r => r.json()),
    fetch(`https://jsonplaceholder.typicode.com/albums?userId=${userId}`).then(r => r.json())
  ])
  user.value = userRes
  albums.value = albumsRes
})
</script>
