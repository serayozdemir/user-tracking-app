<template>
  <div>
    <!-- Albüm sayfasına dönüş bağlantısı -->
    <RouterLink
      :to="`/user/${userId}/albums`"
      class="inline-block mb-4 text-green-500 hover:underline"
    >
      ← Go Albums
    </RouterLink>

    <h1 class="text-xl font-bold mb-6 text-gray-800">Album Photos</h1>

    <!-- Geniş ve duyarlı grid yapısı -->
    <div
      class="grid gap-6"
      style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));"
    >
      <div
        v-for="i in 9"
        :key="i"
        class="overflow-hidden rounded shadow hover:shadow-md transition"
      >
        <img
          :src="`https://picsum.photos/seed/${albumId}-${i}/300`"
          alt="Album photo"
          loading="lazy"
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
