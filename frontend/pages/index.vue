<template>
  <div>
    <div class="bg-white py-16 sm:py-24">
      <div v-if="!matchedUserFs?.id" class="w-full flex justify-center text-center">
        <div class="space-y-2">
          <h2 class="text-lg">Nothing to see here, wait for your next match..</h2>
          <img class="max-w-xl" src="/empty-state.jpg">
        </div>
      </div>
      <div v-else class="mx-auto max-w-7xl sm:px-6 lg:px-8">
        <h1 class="text-2xl font-bold py-5">It's a match!! 🎉</h1>
        <div
          class="relative overflow-hidden bg-gray-900 px-6 py-20 shadow-xl sm:rounded-3xl sm:px-10 sm:py-24 md:px-12 lg:px-20">
          <div class="absolute inset-0 bg-gray-900/90 mix-blend-multiply" />
          <div class="absolute -left-80 -top-56 transform-gpu blur-3xl" aria-hidden="true">
            <div class="aspect-[1097/845] w-[68.5625rem] bg-gradient-to-r from-[#A8005C] to-[#009EE3] opacity-[0.45]"
              style="
                clip-path: polygon(
                  74.1% 44.1%,
                  100% 61.6%,
                  97.5% 26.9%,
                  85.5% 0.1%,
                  80.7% 2%,
                  72.5% 32.5%,
                  60.2% 62.4%,
                  52.4% 68.1%,
                  47.5% 58.3%,
                  45.2% 34.5%,
                  27.5% 76.7%,
                  0.1% 64.9%,
                  17.9% 100%,
                  27.6% 76.8%,
                  76.1% 97.7%,
                  74.1% 44.1%
                );
              " />
          </div>
          <div class="hidden md:absolute md:bottom-16 md:left-[50rem] md:block md:transform-gpu md:blur-3xl"
            aria-hidden="true">
            <div class="aspect-[1097/845] w-[68.5625rem] bg-gradient-to-r from-[#A8005C] to-[#009EE3] opacity-25" style="
                clip-path: polygon(
                  74.1% 44.1%,
                  100% 61.6%,
                  97.5% 26.9%,
                  85.5% 0.1%,
                  80.7% 2%,
                  72.5% 32.5%,
                  60.2% 62.4%,
                  52.4% 68.1%,
                  47.5% 58.3%,
                  45.2% 34.5%,
                  27.5% 76.7%,
                  0.1% 64.9%,
                  17.9% 100%,
                  27.6% 76.8%,
                  76.1% 97.7%,
                  74.1% 44.1%
                );
              " />
          </div>
          <div class="relative mx-auto max-w-2xl lg:mx-0">
            <div class="flex">
              <img class="h-24 w-auto object-cover rounded-full" :src="matchedUser?.avatarUrl || ''" alt="" />
              <div class="pl-7">
                <div class="text-2xl font-semibold text-white">
                  {{ matchedUser?.name }}
                </div>
                <div class="mt-1 text-gray-400 pb-3">
                  {{ matchedUser?.team }}
                </div>
                <UButton variant="solid" icon="i-heroicons-envelope" @click="sendEmail()" trailing>
                  Contact
                </UButton>
              </div>
            </div>
            <figure>
              <blockquote class="mt-6 text-lg font-semibold text-white sm:text-xl sm:leading-8">
                <p class="italic font-light">“{{ matchedUserFs?.funfacts }}”</p>
              </blockquote>
              <figcaption class="mt-6 text-base text-white">
                <div class="pb-4 space-x-2">
                  <UBadge v-for="(key, value) in matchedUserFs?.preferences" color="white" variant="outline">{{ value }}
                  </UBadge>
                </div>
              </figcaption>
            </figure>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { collection, doc, getDocs } from "firebase/firestore";

export type User = {
  days: Array<string>;
  name: string;
  team: string;
  preferences: {
    [key: string]: number;
  };
  funfacts: string;
};

function sendEmail() {
  window.open(
    `mailto:${matchedUser?.email}?subject=Let's meet! 👋&body=${body.value}`,
    "_blank"
  );
}

definePageMeta({
  middleware: ["auth"],
});

const showEmptyState = ref(true);

const firestore = useFirestore();
const user = useCurrentUser();
const userId = user.value?.uid;
const username = user.value?.displayName;
const docsSnap = await getDocs(
  collection(firestore, `users/${userId}/matches`)
);

// Get the latest match
let matchedUserId = undefined
let matchedUser = {}
let matchedUserFs = undefined

const lastDoc = docsSnap.docs[docsSnap.docs.length - 1];


if (lastDoc) {

  const participants = lastDoc.data().participants;
  matchedUser = participants[0];

  if (matchedUser.id === userId) {
    matchedUser = participants[1];
  }

  matchedUserId = matchedUser.id
  matchedUserFs = useDocument<User>(
    doc(collection(firestore, "users"), matchedUserId)
  );
  const body = computed(() => `Hi, ${matchedUser?.name} %0D%0A%0D%0A How about grabbing a coffee sometime this week%3F %0D%0A%0D%0A Best, %0D%0A ${username}`)
}


</script>