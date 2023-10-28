<template>
  <NuxtPage />
</template>

<script setup lang="ts">
const router = useRouter()
const route = useRoute()
const user = useCurrentUser()

// we don't need this watcher on server
onMounted(() => {
  watch(user, (user, prevUser) => {
    if (prevUser && !user) {
      // user logged out
      navigateTo('/login', { replace: true })
    } else if (user && typeof route.query.redirect === 'string') {
      // user logged in
      router.push(route.query.redirect || '/')
    }
  })
})
</script>
