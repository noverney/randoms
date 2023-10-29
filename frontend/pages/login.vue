<template>
    <section class="flex items-center justify-center bg-gray-50 h-screen">

    <div class="flex bg-sky-100 max-w-3xl rounded-2xl shadow-lg p-5">
        <!-- IMAGE -->
        <div class="sm:block hidden w-1/2">
         <img class="rounded-2xl" src="~/public/landing-page-1.jpeg">
        </div>
        
        <!-- FORM -->
        <div class="sm:w-1/2 bg-sky-200 px-20">
            <h2 class="font-bold text-2xl mb-2">Let's meet some cool people!</h2>
            <p class="text-xs">Already registered? Login below.</p>

            <form class="flex flex-col">
                <UInput class="p-1 mt-4" type="text" placeholder="Email"></UInput>
                <UInput class="p-1" type="password" placeholder="Password"></UInput>
                <UButton>Login</UButton>
            </form>
            <div class="mt-2 grid grid-cols-3 items-center">
                <hr>
                <p class="text-gray-500">OR</p>
                <hr>
            </div>
            <!-- GOOGLE SIGN-IN -->
                            <button @click="signinRedirect"
                    class="flex w-full items-center justify-center gap-3 rounded-md bg-[#24292F] px-3 py-1.5 text-white focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#24292F]">
                    <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24">
                        <path
                            d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"
                            fill="#4285F4" />
                        <path
                            d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
                            fill="#34A853" />
                        <path
                            d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"
                            fill="#FBBC05" />
                        <path
                            d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"
                            fill="#EA4335" />
                        <path d="M1 1h22v22H1z" fill="none" />
                    </svg>
                    <span class="text-sm font-semibold leading-6">Sign in with Google</span>
                </button>
        </div>

    </div>
    </section>
</template>

<script setup lang="ts">
import { signInWithRedirect, GoogleAuthProvider, signInWithPopup } from 'firebase/auth'

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
    signInWithPopup(auth, googleAuthProvider).catch((reason) => {
        console.error('Failed signinRedirect', reason)
        error.value = reason
    })
}
</script>