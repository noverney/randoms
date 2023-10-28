<template>
  <div class="flex items-center justify-center h-screen">
    <UCard class="w-9/12 sm:min-w-80 max-w-md" :ui="{ shadow: 'shadow-lg' }">
      <div class="flex flex-col items-center space-x-4">
        <div class="flex items-center space-x-4 pb-4">
          <UAvatar
            src="https://avatars.githubusercontent.com/u/25683183?v=4"
            alt="Avatar"
            size="3xl"
          />
          <div class="space-y-2">
            <p class="font-semibold text-xl">{{ username }}</p>
            <p>RDIA</p>
          </div>
        </div>
        <UTextarea
          class="w-9/12"
          autoresize
          v-model="funfacts"
          :ui="{ placeholder: 'Fun facts' }"
        />
        <div class="py-3 space-x-2">
          <USelectMenu
            v-model="selected"
            :options="interests"
            multiple
            placeholder="Select interests"
          />
        </div>
        <UButton color="primary" variant="solid" @click="saveChanges"
          >Save Changes</UButton
        >
      </div>
    </UCard>
  </div>
</template>

<script setup lang="ts">
import { doc, setDoc } from "firebase/firestore";

definePageMeta({
  middleware: ["auth"],
});
const isLoading = ref(false);
const interests = ["Mangas", "Harry Potter", "Hacking"];
const selected = ref([]);

const username = ref("Joe Doe");
const userMatched = ref("Joe Doe");
const funfacts = ref(
  "I have a talent for remembering an unusual number of random trivia facts. It's like having a mental library of quirky information, and I'm always ready to share a fun fact at any social gathering!"
);

const firestore = useFirestore();
const user = useCurrentUser();

const saveChanges = async () => {
  // Save the interests and funfacts to the users database
  console.log("SAVING");
  if (!user.value?.uid) {
    console.log("No user");
    return;
  }

  const interestsObject = Object.fromEntries(selected.value.map((x) => [x, 5]));
  console.log(interestsObject);

  await setDoc(doc(firestore, "users", user.value.uid), {
    preferences: interestsObject,
    funfacts: funfacts.value,
  });
  console.log("SAVED");
};
</script>
