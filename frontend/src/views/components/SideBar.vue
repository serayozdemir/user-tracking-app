<template>
  <aside class="w-64 bg-white shadow-md flex flex-col justify-between min-h-screen">
    <!-- ÜST KISIM -->
    <div>
      <div class="p-6">
        <!-- Profil varsa göster -->
        <div v-if="user" class="flex items-center space-x-4 mb-6">
          <img :src="`https://i.pravatar.cc/150?img=${user.id}`" class="w-14 h-14 rounded-full object-cover border" />
          <div>
            <h2 class="text-base font-semibold">{{ user.name }}</h2>
            <p class="text-sm text-gray-500">{{ user.email }}</p>
          </div>
        </div>
        <hr v-if="user" class="my-4" />

        <!-- Navigation -->
        <nav class="space-y-2">
          <!-- 🔽 Users (sadece user yoksa göster) -->
          <RouterLink
            v-if="!user"
            to="/"
            class="flex items-center px-4 py-2 text-sm font-medium hover:bg-gray-100 rounded-lg"
            active-class="bg-purple-100 text-purple-600 font-semibold"
          >
            <img :src="UsersIcon" class="w-5 h-5 mr-2" />
            Users
          </RouterLink>

          <!-- 🔽 Todos / Posts / Albums (sadece user varsa göster) -->
          <template v-if="user">
            <RouterLink
              :to="`/user/${user.id}/todos`"
              class="flex items-center px-4 py-2 text-sm font-medium hover:bg-gray-100 rounded-lg"
              active-class="bg-purple-100 text-purple-600 font-semibold"
            >
              <img :src="ChecklistIcon" class="w-5 h-5 mr-2" />
              Todos
            </RouterLink>

            <RouterLink
              :to="`/user/${user.id}/posts`"
              class="flex items-center px-4 py-2 text-sm font-medium hover:bg-gray-100 rounded-lg"
              active-class="bg-purple-100 text-purple-600 font-semibold"
            >
              <img :src="ArticleIcon" class="w-5 h-5 mr-2" />
              Posts
            </RouterLink>

            <RouterLink
              :to="`/user/${user.id}/albums`"
              class="flex items-center px-4 py-2 text-sm font-medium hover:bg-gray-100 rounded-lg"
              active-class="bg-purple-100 text-purple-600 font-semibold"
            >
              <img :src="PhotoIcon" class="w-5 h-5 mr-2" />
              Albums
            </RouterLink>
          </template>
        </nav>
      </div>
    </div>

    <!-- ALT KISIM -->
    <div class="p-6 border-t">
      <div class="flex items-center space-x-2">
        <img src="/frontend-logo.png" class="w-6 h-6" />
        <span class="font-semibold text-gray-600">N2Mobil</span>
      </div>
    </div>
  </aside>
</template>

<script setup>
import UsersIcon from '../../assets/icons/users.svg'
import ChecklistIcon from '../../assets/icons/checklist.svg'
import ArticleIcon from '../../assets/icons/article.svg'
import PhotoIcon from '../../assets/icons/photo.svg'

defineProps({
  user: Object
})
</script>
