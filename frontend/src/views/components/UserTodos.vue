<template>
  <div class="p-6 w-full min-h-screen">
    <!-- Go Home -->
    <router-link
      to="/"
      class="text-sm text-gray-600 hover:text-purple-600 font-medium inline-block mb-6"
    >
      ← Go Home
    </router-link>

    <!-- Başlık -->
    <h2 class="text-2xl font-bold mb-6 text-gray-800">Todo List</h2>

    <!-- Liste -->
    <ul class="space-y-4">
      <li
        v-for="todo in todos"
        :key="todo.id"
        class="flex items-start gap-3"
      >
        <!-- Custom checkbox -->
        <div class="relative">
          <input
            type="checkbox"
            :checked="todo.completed"
            disabled
            class="peer hidden"
            :id="'todo-' + todo.id"
          />
          <label
            :for="'todo-' + todo.id"
            class="w-5 h-5 border-2 border-purple-600 rounded-sm flex items-center justify-center cursor-default
                   peer-checked:bg-purple-600 peer-checked:text-white"
          >
            <svg
              v-if="todo.completed"
              xmlns="http://www.w3.org/2000/svg"
              class="w-4 h-4"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="3"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M5 13l4 4L19 7"
              />
            </svg>
          </label>
        </div>

        <!-- Metin -->
        <span class="text-gray-800 text-base">
          {{ todo.title }}
        </span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "UserTodos",
  data() {
    return {
      todos: [],
    };
  },
  async created() {
    const userId = this.$route.params.id;

    try {
      const response = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}/todos`);
      if (!response.ok) throw new Error("Veri alınamadı");
      this.todos = await response.json();
    } catch (error) {
      console.error("Hata:", error);
    }
  },
};
</script>

<style scoped>
/* Gerekirse ekstra stil buraya */
</style>
