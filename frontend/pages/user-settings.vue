<template>
  <div class="flex items-center justify-center h-full">
    <UCard class="w-[50rem]" :ui="{ shadow: 'shadow-lg' }">
      <form @submit.prevent="saveChanges" class="space-y-8 p-6">
        <div class="flex items-center space-x-4 pb-4">
          <UAvatar class="border" :src="user?.photoURL || ''" alt="Avatar" size="3xl" />
          <div class="space-y-2">
            <p class="font-semibold text-xl">{{ user?.displayName }}</p>
            <p>{{ extendedUserInformation?.team || 'no team selected' }}</p>
          </div>
        </div>
        <UFormGroup required label="Type your department name" name="team">
          <UInput v-model="department" class="mt-4" />
        </UFormGroup>
        <UFormGroup required label="Add a funfact about you" name="description">
          <UTextarea v-model="funfact" class="mt-4" />
        </UFormGroup>
        <UFormGroup required label="On which days are you normally available?" name="days">
          <ul role="list"
            class="grid justify-items-stretch mt-4 grid-cols-3 gap-x-4 gap-y-6 sm:grid-cols-5 sm:gap-x-6 lg:grid-cols-5">
            <li v-for="(value, key) of days" :key="key" class="col-span-1 flex rounded-md shadow-sm">
              <button @click="toggleWeekDay(value)" type="button"
                :class="[selectedDays.includes(value) ? 'ring-2 ring-primary-500 ring-offset-2 ring-offset-gray-100' : '']"
                class="flex flex-1 items-center justify-between truncate rounded-md border border-gray-200 bg-white">
                <div class="flex-1 truncate px-4 py-2 text-sm">
                  <h2 class="font-medium text-gray-900 hover:text-gray-600">{{ value }}</h2>
                </div>
              </button>
            </li>
          </ul>
        </UFormGroup>
        <UFormGroup required label="Select your interests (at least one)" name="preferences">
          <ul role="list"
            class="grid justify-items-stretch mt-4 grid-cols-2 gap-x-4 gap-y-6 sm:grid-cols-3 sm:gap-x-6 lg:grid-cols-4">
            <li v-for="(value, key) of interests" :key="key" class="col-span-1 flex rounded-md shadow-sm">
              <div v-if="value"
                class="flex flex-1 items-center justify-between truncate rounded-md border border-gray-200 bg-white">
                <div class="flex-1 truncate px-4 py-2 text-sm">
                  <h2 class="font-medium text-gray-900 hover:text-gray-600">{{ value }}</h2>
                  <StarRating :name="value" :rating="(extendedUserInformation?.preferences[value] || 0)"
                    @update="ratingUpdated" />
                </div>
              </div>
            </li>
          </ul>
        </UFormGroup>
        <div class="w-full flex space-x-4 justify-end pt-4">
          <UButton color="gray" variant="outline" @click="navigateTo('/')">Cancel</UButton>
          <UButton type="submit">
            Save changes
          </UButton>
        </div>
      </form>
    </UCard>
  </div>
</template>

<script setup lang="ts">
import { collection, doc, setDoc } from "firebase/firestore";
import type { User } from "./index.vue";

type UserInterests = {
  [key: string]: number
}

definePageMeta({
  middleware: ["auth"],
});

const interests = ['Mangas', 'Harry Potter', 'Hacking']
const days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

const user = useCurrentUser();
const firestore = useFirestore()

const extendedUserInformation = useDocument<User>(
  doc(collection(firestore, "users"), user.value?.uid)
);
// init page state
watch(extendedUserInformation, () => {
  if (extendedUserInformation.value?.funfacts) {
    funfact.value = extendedUserInformation.value.funfacts
  }
  if (extendedUserInformation.value?.preferences) {
    userInterests.value = extendedUserInformation.value.preferences
  }
  if (extendedUserInformation.value?.team) {
    department.value = extendedUserInformation.value.team
  }
  if (extendedUserInformation.value?.days) {
    selectedDays.value = extendedUserInformation.value.days
  }
})

const department = ref('')
const funfact = ref('')
const userInterests = ref<UserInterests>({})
const selectedDays = ref<Array<string>>([])

const ratingUpdated = (key: string, rating: number) => {
  userInterests.value[key] = rating
}
const toggleWeekDay = (key: string) => {
  if (selectedDays.value.includes(key)) {
    selectedDays.value = selectedDays.value.filter(day => day != key);
  } else {
    selectedDays.value.push(key)
  }
}

const funfacts = ref(
  "I have a talent for remembering an unusual number of random trivia facts. It's like having a mental library of quirky information, and I'm always ready to share a fun fact at any social gathering!"
);


const saveChanges = async () => {
  // Save the interests and funfacts to the users database
  if (!user.value?.uid) {
    console.log("No user");
    return;
  }

  await setDoc(doc(firestore, "users", user.value.uid), {
    preferences: userInterests.value,
    funfacts: funfact.value,
    team: department.value,
    days: selectedDays.value
  });
};
</script>
