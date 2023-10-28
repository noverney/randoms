<template>
  <div>
    <div class="bg-white py-16 sm:py-24">
      <div class="mx-auto max-w-7xl sm:px-6 lg:px-8">
        <div
          class="relative overflow-hidden bg-gray-900 px-6 py-20 shadow-xl sm:rounded-3xl sm:px-10 sm:py-24 md:px-12 lg:px-20"
        >
          <div class="absolute inset-0 bg-gray-900/90 mix-blend-multiply" />
          <div
            class="absolute -left-80 -top-56 transform-gpu blur-3xl"
            aria-hidden="true"
          >
            <div
              class="aspect-[1097/845] w-[68.5625rem] bg-gradient-to-r from-[#ff4694] to-[#776fff] opacity-[0.45]"
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
              "
            />
          </div>
          <div
            class="hidden md:absolute md:bottom-16 md:left-[50rem] md:block md:transform-gpu md:blur-3xl"
            aria-hidden="true"
          >
            <div
              class="aspect-[1097/845] w-[68.5625rem] bg-gradient-to-r from-[#ff4694] to-[#776fff] opacity-25"
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
              "
            />
          </div>
          <div class="relative mx-auto max-w-2xl lg:mx-0">
            <img
              class="h-24 w-auto object-cover rounded-full"
              :src="user?.photoURL || ''"
              alt=""
            />
            <figure>
              <blockquote
                class="mt-6 text-lg font-semibold text-white sm:text-xl sm:leading-8"
              >
                <p>“{{ funfacts }}”</p>
              </blockquote>
              <figcaption class="mt-6 text-base text-white">
                <div class="pb-4 space-x-2">
                  <UBadge
                    v-for="(value, key) in nextMatchedUser?.preferences"
                    color="white"
                    variant="outline"
                    >{{ key }}
                  </UBadge>
                  <UBadge
                    v-if="
                      Object.keys(nextMatchedUser?.preferences || {}).length ===
                      0
                    "
                    color="white"
                    variant="outline"
                    >#BoringPerson</UBadge
                  >
                </div>
                <div class="font-semibold">{{ nextMatchedUser?.name }}</div>
                <div class="mt-1">{{ nextMatchedUser?.team }}</div>
              </figcaption>
            </figure>
          </div>
        </div>
        <p class="italic pt-3">"{{ funfacts }}"</p>
        <div class="flex items-center pt-3 space-x-2">
          <UBadge color="sky" variant="outline">Mangas</UBadge>
          <UBadge color="sky" variant="outline">Harry Potter</UBadge>
          <UBadge color="sky" variant="outline">Hacking</UBadge>
        </div>
      </div>
    </div>
  </div>

  <!-- Show all user details in a list -->
  <!-- <ul>
    <li v-for="user in users" :key="user.id">
      {{ user.name }} : {{ user.preferences }}
    </li>
  </ul> -->
</template>

<script setup lang="ts">
import { collection, doc } from "firebase/firestore";

type User = {
  days: Array<string>;
  name: string;
  team: string;
  preferences: {
    [key: string]: string;
  };
};

definePageMeta({
  middleware: ["auth"],
});

const funfacts = ref(
  "I have a talent for remembering an unusual number of random trivia facts. It's like having a mental library of quirky information, and I'm always ready to share a fun fact at any social gathering!"
);

const isLoading = ref(false);

const firestore = useFirestore();
const user = useCurrentUser();

const nextMatchedUser = useDocument<User>(
  doc(collection(firestore, "users"), user.value?.uid)
);
</script>
