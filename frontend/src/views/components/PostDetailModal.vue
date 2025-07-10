<template>
  <div v-if="show" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
    <div class="bg-white w-3/4 max-w-4xl rounded-lg shadow-lg p-6 flex relative">
      <button class="absolute top-2 right-2 text-gray-500 hover:text-black" @click="close">
        <i class="fas fa-times"></i>
      </button>

      <!-- Post İçeriği -->
      <div class="w-1/2 pr-4 border-r">
        <h2 class="text-xl font-bold mb-4">{{ post.title }}</h2>
        <p class="text-sm text-gray-700 whitespace-pre-line">{{ post.body }}</p>
      </div>

      <!-- Yorumlar -->
      <div class="w-1/2 pl-4 max-h-[400px] overflow-y-auto">
        <h3 class="text-lg font-semibold mb-3">Comments</h3>
        <div v-for="comment in comments" :key="comment.id" class="mb-4 flex items-start gap-3">
          <img :src="`https://i.pravatar.cc/40?u=${comment.email}`" class="rounded-full w-10 h-10" />
          <div>
            <p class="text-sm font-semibold">{{ comment.name }}</p>
            <p class="text-xs text-gray-600">{{ comment.body }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  show: Boolean,
  post: Object,
  comments: Array,
  close: Function
})
</script>
