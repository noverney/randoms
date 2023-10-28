<template>
    <header class="shrink-0 bg-gray-900">
        <div class="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
            <NuxtLink to="/">
                <img class="h-8 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500"
                    alt="Your Company" />
            </NuxtLink>
            <div class="flex items-center gap-x-8">
                <UDropdown :items="items" :ui="{ item: { disabled: 'cursor-text select-text' } }"
                    :popper="{ placement: 'bottom-start' }">
                    <UAvatar :src="currentUser?.photoURL || 'https://avatars.githubusercontent.com/u/739984?v=4'" />
                    <template #account="{ item }">
                        <div class="text-left">
                            <p>
                                Signed in as
                            </p>
                            <p class="truncate font-medium text-gray-900 dark:text-white">
                                {{ currentUser?.email || 'darth@vader.com' }}
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
        <slot />
    </main>
</template>

<script setup lang="ts">
const currentUser = useCurrentUser()
const auth = useFirebaseAuth()

const items = [
    [{
        label: 'ben@example.com',
        slot: 'account',
        disabled: true
    }], [{
        label: 'User Settings',
        icon: 'i-heroicons-cog-8-tooth',
        click: () => { navigateTo('/user') }
    }], [{
        label: 'Sign out',
        icon: 'i-heroicons-arrow-left-on-rectangle',
        click: () => { auth?.signOut() }
    }]
]
</script>