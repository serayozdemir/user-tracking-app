<template>
  <div>
    <!-- Go Home -->
    <RouterLink to="/" class="inline-block mb-4 text-green-500 hover:underline">
      ← Go Home
    </RouterLink>

    <h1 class="text-xl font-bold mb-6 text-gray-800">Posts</h1>

    <div class="space-y-4 max-w-4xl mx-auto">
      <div
        v-for="post in posts"
        :key="post.id"
        class="border rounded-lg shadow-sm px-6 py-4 bg-white hover:shadow-md transition-all duration-200"
      >
        <h3 class="font-semibold text-lg text-purple-800 mb-2 truncate">{{ post.title }}</h3>
        <p class="text-sm text-gray-600 mb-3">{{ post.body }}</p>
        <button
          @click="openModal(post)"
          class="text-purple-600 text-sm flex items-center gap-1 hover:underline"
        >
          See More <i class="fas fa-arrow-circle-right"></i>
        </button>
      </div>
    </div>

    <PostDetailModal
      :show="showModal"
      :post="selectedPost"
      :comments="comments"
      :close="() => (showModal = false)"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import PostDetailModal from './PostDetailModal.vue'

const route = useRoute()
const userId = route.params.id

const user = ref({})
const posts = ref([])
const comments = ref([])
const showModal = ref(false)
const selectedPost = ref({})

onMounted(async () => {
  const [userRes, postsRes] = await Promise.all([
    fetch(`https://jsonplaceholder.typicode.com/users/${userId}`).then(r => r.json()),
    fetch(`https://jsonplaceholder.typicode.com/posts?userId=${userId}`).then(r => r.json())
  ])
  user.value = userRes
  posts.value = postsRes
})

const openModal = async (post) => {
  selectedPost.value = post
  showModal.value = true
  comments.value = await fetch(`https://jsonplaceholder.typicode.com/comments?postId=${post.id}`).then(r => r.json())
}
</script>
