<template>
  <div>
    <RouterLink :to="`/user/${userId}/albums`" class="inline-block mb-4 text-primary hover:underline">
      ← Go Albums
    </RouterLink>

    <h1 class="text-xl font-bold mb-6 text-dark">Album Photos</h1>

    <div class="grid gap-6" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));">
      <div v-for="i in 9" :key="i" class="overflow-hidden rounded shadow hover:shadow-md transition">
        <img
          :src="`https://picsum.photos/seed/${albumId}-${i}/300`"
          alt="Album photo"
          class="w-full aspect-square object-cover rounded"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
const route = useRoute()
const userId = route.params.id
const albumId = route.params.albumId
</script>
