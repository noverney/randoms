<template>
  <header class="shrink-0 bg-gray-900 sticky top-0 z-10">
    <div class="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
      <NuxtLink to="/">
        <img class="h-8 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500"
          alt="Your Company" />
      </NuxtLink>
      <div class="flex items-center gap-x-8">
        <UDropdown :items="items" :ui="{ item: { disabled: 'cursor-text select-text' } }"
          :popper="{ placement: 'bottom-end' }">
          <UAvatar :src="currentUser?.photoURL ||
            'https://avatars.githubusercontent.com/u/739984?v=4'
            " />
          <template #account="{ item }">
            <div class="text-left">
              <p>Signed in as</p>
              <p class="truncate font-medium text-gray-900 dark:text-white">
                {{ currentUser?.email || "darth@vader.com" }}
              </p>
            </div>
          </template>
          <template #item="{ item }">
            <span class="truncate">{{ item.label }}</span>
            <UIcon :name="item.icon" class="flex-shrink-0 h-4 w-4 text-gray-400 dark:text-gray-500 ms-auto" />
          </template>
        </UDropdown>
      </div>
    </div>
  </header>
  <main>
    <div class="mx-auto max-w-7xl items-center p-4 sm:px-6 lg:px-8 overflow-y-auto h-[calc(100dvh-4rem)]">
      <slot />
    </div>
  </main>
</template>

<script setup lang="ts">
import { collection, doc, setDoc } from 'firebase/firestore';

const currentUser = useCurrentUser();
const auth = useFirebaseAuth();
const firestore = useFirestore()

const items = [
  [
    {
      label: "ben@example.com",
      slot: "account",
      disabled: true,
    },
  ],
  [
    {
      label: "User Settings",
      icon: "i-heroicons-cog-8-tooth",
      click: () => {
        navigateTo("/user");
      },
    },
  ],
  [
    {
      label: "Sign out",
      icon: "i-heroicons-arrow-left-on-rectangle",
      click: () => {
        auth?.signOut();
      },
    },
  ],
];

// redirect user on first sign up and init user document
const user = await getCurrentUser()
const me = useDocument(doc(collection(firestore, 'users'), user.uid))

watch([me], async () => {
  if (user && !me.value) {
    await setDoc(doc(firestore, "users", user.uid), {
      name: user.displayName,
      preferences: {},
      days: [],
    });
    navigateTo('/user')
  }
})

</script>
