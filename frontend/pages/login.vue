<template>
    <div>

        <div v-if="error">{{ error }}</div>
        <button @click="signinRedirect">SignIn with Google</button>

    </div>
</template>

<script setup lang="ts">
import { signInWithRedirect, GoogleAuthProvider } from 'firebase/auth'

definePageMeta({
    layout: false
})

const googleAuthProvider = new GoogleAuthProvider()
const auth = useFirebaseAuth()!
const currentUser = useCurrentUser()
const error = ref(null)

watch([currentUser], () => {
    // redirect if already logged in
    if (currentUser.value) {
        navigateTo('/')
    }
})

const signinRedirect = async () => {
    signInWithRedirect(auth, googleAuthProvider).catch((reason) => {
        console.error('Failed signinRedirect', reason)
        error.value = reason
    })
}
</script>