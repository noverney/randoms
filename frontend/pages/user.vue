<template>
  <div class="flex items-center justify-center h-screen">
    <UCard class="w-auto sm:min-w-80 max-w-md" :ui="{ shadow: 'shadow-lg' }">
      <div v-if="isLoading" class="flex items-center space-x-4">
        <USkeleton class="h-12 w-12" :ui="{ rounded: 'rounded-full' }" />
        <div class="space-y-2">
          <USkeleton class="h-4 w-[250px]" />
          <USkeleton class="h-4 w-[200px]" />
        </div>
      </div>

      <div v-else class="flex flex-col items-center space-x-4">
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
        <!-- nuxt UI text component for funfacts -->
        <UTextarea
          autoresize
          v-model="funfacts"
          :ui="{ placeholder: 'Fun facts' }"
        />
        <div class="pt-3 space-x-2">
          <UBadge color="sky" variant="outline">Mangas</UBadge>
          <UBadge color="sky" variant="outline">Harry Potter</UBadge>
          <UBadge color="sky" variant="outline">Hacking</UBadge>
          <UButton
            icon="i-heroicons-pencil-square"
            size="2xs"
            color="primary"
            square
            variant="outline"
          />
        </div>
      </div>
    </UCard>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  middleware: ["auth"],
});
const isLoading = ref(false);

const username = ref("Joe Doe");
const userMatched = ref("Joe Doe");
const funfacts = ref(
  "I have a talent for remembering an unusual number of random trivia facts. It's like having a mental library of quirky information, and I'm always ready to share a fun fact at any social gathering!"
);
</script>
