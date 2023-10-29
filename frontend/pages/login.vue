<template>
    <div>
        <div v-if="!loading" class="flex min-h-full flex-1 h-[100dvh]">
            <div class="flex flex-1 flex-col justify-center px-4 py-12 sm:px-6 lg:flex-none lg:px-20 xl:px-24">
                <div class="mx-auto w-full max-w-sm lg:w-96">
                    <div>
                        <img class="h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600"
                            alt="Your Company" />
                        <h2 class="mt-8 text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign in to your account
                        </h2>
                    </div>

                    <div class="mt-10">
                        <div>
                            <form @submit.prevent="signInWithPassword" class="space-y-6">
                                <div>
                                    <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email
                                        address</label>
                                    <div class="mt-2">
                                        <UInput v-model="email" id="email" name="email" type="email" autocomplete="email"
                                            required />
                                    </div>
                                </div>

                                <div>
                                    <label for="password"
                                        class="block text-sm font-medium leading-6 text-gray-900">Password</label>
                                    <div class="mt-2">
                                        <UInput v-model="password" id="password" name="password" type="password"
                                            autocomplete="current-password" required />
                                    </div>
                                </div>

                                <div>
                                    <button type="submit"
                                        class="flex w-full justify-center rounded-md bg-primary-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600">Sign
                                        in</button>
                                </div>
                            </form>
                        </div>

                        <div class="mt-10">
                            <div class="relative">
                                <div class="absolute inset-0 flex items-center" aria-hidden="true">
                                    <div class="w-full border-t border-gray-200" />
                                </div>
                                <div class="relative flex justify-center text-sm font-medium leading-6">
                                    <span class="bg-white px-6 text-gray-900">Or continue with</span>
                                </div>
                            </div>

                            <div class="mt-6 grid grid-cols-2 gap-4">
                                <button @click="signInGoogle"
                                    class="flex w-full items-center justify-center gap-3 rounded-md bg-white px-3 py-1.5 text-black border-black border focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#1D9BF0]">
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
                                    <span class="text-sm font-semibold leading-6">Google</span>
                                </button>

                                <button @click="signInGitHub"
                                    class="flex w-full items-center justify-center gap-3 rounded-md bg-[#24292F] px-3 py-1.5 text-white focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#24292F]">
                                    <svg class="h-5 w-5" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20">
                                        <path fill-rule="evenodd"
                                            d="M10 0C4.477 0 0 4.484 0 10.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0110 4.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.203 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.942.359.31.678.921.678 1.856 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0020 10.017C20 4.484 15.522 0 10 0z"
                                            clip-rule="evenodd" />
                                    </svg>
                                    <span class="text-sm font-semibold leading-6">GitHub</span>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="relative items-center hidden w-0 flex-1 lg:flex">
                <img class="absolute rounded-lg h-[80%] w-full object-cover" src="/landing-page-1.jpeg" alt="" />
            </div>
        </div>
        <div v-else>redirecting..</div>
    </div>
</template>


<script setup lang="ts">
import { GoogleAuthProvider, GithubAuthProvider, signInWithPopup, signInWithEmailAndPassword, createUserWithEmailAndPassword, updateProfile } from 'firebase/auth'

definePageMeta({
    layout: false
})

const googleAuthProvider = new GoogleAuthProvider()
const githubAuthProvider = new GithubAuthProvider()
const auth = useFirebaseAuth()!
const currentUser = useCurrentUser()
const toast = useToast()

const loading = ref(true)

const email = ref('')
const password = ref('')

auth.authStateReady().then(() => {
    if (currentUser.value) {
        navigateTo('/')
    } else {
        loading.value = false
    }
})

watch([currentUser], () => {
    if (currentUser.value) {
        navigateTo('/')
    }
})


const signInGoogle = async () => {
    signInWithPopup(auth, googleAuthProvider).catch((reason) => {
        console.error('Failed signinRedirect', reason)
        toast.add({ title: 'Auth Error', description: reason })
    })
}
const signInGitHub = async () => {
    signInWithPopup(auth, githubAuthProvider).catch((reason) => {
        console.error('Failed signinRedirect', reason)
        toast.add({ title: 'Auth Error', description: reason })
    })
}
const signInWithPassword = () => {

    signInWithEmailAndPassword(auth, email.value, password.value).catch((reason) => {
        // create user if not exists
        if (reason == "FirebaseError: Firebase: Error (auth/invalid-login-credentials).") {
            createUserWithEmailAndPassword(auth, email.value, password.value).then((data) => {
                updateProfile(data.user, {
                    displayName: email.value
                })
            }).catch((reason) => {
                toast.add({ title: 'Auth Error', description: reason.message })
            })
        } else {
            toast.add({ title: 'Auth Error', description: reason.message })
        }
    })


}
</script>
