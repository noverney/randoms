<template>
  <!-- <NuxtLink to="/login">Login</NuxtLink>
  <NuxtLink to="/user">User</NuxtLink>
  <br />

  <button @click="logout">LogOut</button> -->

  <!-- <pre>User: {{ user?.displayName }}</pre>

  <pre>{{ users }}</pre> -->
  <div class="flex items-center justify-center h-screen">
    <UCard class="w-auto min-w-80 max-w-md" :ui="{ shadow: 'shadow-lg' }">
      <div v-if="isLoading" class="flex items-center space-x-4">
        <USkeleton class="h-12 w-12" :ui="{ rounded: 'rounded-full' }" />
        <div class="space-y-2">
          <USkeleton class="h-4 w-[250px]" />
          <USkeleton class="h-4 w-[200px]" />
        </div>
      </div>

      <div v-else class="flex flex-col items-center space-x-4">
        <div class="flex items-center space-x-4">
          <UAvatar
            src="https://avatars.githubusercontent.com/u/25683183?v=4"
            alt="Avatar"
            size="3xl"
          />
          <div class="space-y-2">
            <p class="font-semibold text-xl">{{ users.at(0)?.name }}</p>
            <p>RDIA</p>
          </div>
        </div>
        <p class="italic pt-3">"{{ funfacts }}"</p>
        <div class="pt-3 space-x-2">
          <UBadge color="sky" variant="outline">Mangas</UBadge>
          <UBadge color="sky" variant="outline">Harry Potter</UBadge>
          <UBadge color="sky" variant="outline">Hacking</UBadge>
        </div>
      </div>
    </UCard>
  </div>
</template>

<script setup lang="ts">
import { collection } from "firebase/firestore";

definePageMeta({
  middleware: ["auth"],
});

const funfacts = ref(
  "I have a talent for remembering an unusual number of random trivia facts. It's like having a mental library of quirky information, and I'm always ready to share a fun fact at any social gathering!"
);

const firestore = useFirestore();
const auth = useFirebaseAuth()!;
const user = useCurrentUser();
useFirestore();

const users = useCollection(collection(firestore, "users"));

const logout = async () => {
  await auth.signOut();
};
</script>
