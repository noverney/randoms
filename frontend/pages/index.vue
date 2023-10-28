<template>
    <div>
        <h1>
            hello from firebase hosting - new one
        </h1>
        <button @click="logout">LogOut</button>

        User:
        <pre>{{ user }}</pre>
        <NuxtLink to="/login">Login</NuxtLink>
        <NuxtLink to="/user">User</NuxtLink>
    </div>
</template>


<script setup lang="ts">
definePageMeta({
    middleware: ['auth'],
})

const user = useCurrentUser()

const auth = useFirebaseAuth()!

const logout = async () => {
    await auth.signOut()
}
</script>