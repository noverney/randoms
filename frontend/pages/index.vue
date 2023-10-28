<template>
    <div>
        <h1>
            hello from firebase hosting - new one
        </h1>
        <NuxtLink to="/login">Login</NuxtLink>
        <NuxtLink to="/user">User</NuxtLink>

        <br>

        <button @click="logout">LogOut</button>

        <pre>User: {{ user?.displayName }}</pre>

        <pre>{{ users }}</pre>
    </div>
</template>


<script setup lang="ts">
import { collection } from 'firebase/firestore';

definePageMeta({
    middleware: ['auth'],
})

const firestore = useFirestore()
const auth = useFirebaseAuth()!
const user = useCurrentUser()
useFirestore()

const users = useCollection(collection(firestore, 'users'))

const logout = async () => {
    await auth.signOut()
}
</script>