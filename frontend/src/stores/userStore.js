import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    users: [],
  }),
  actions: {
    async fetchUsers() {
      const res = await fetch('https://jsonplaceholder.typicode.com/users')
      this.users = await res.json()
    },
  },
})
