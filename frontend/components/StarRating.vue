<template>
    <ul class="flex">
        <li v-for="id in maxRating">
            <UButton size="sm" color="yellow" square variant="ghost" @click="updateRating(id)">
                <UIcon v-if="props.rating < id" name="i-heroicons-star" />
                <UIcon v-else name="i-heroicons-star-solid" />
            </UButton>
        </li>
    </ul>
</template>
<script setup lang="ts">
const maxRating = 5
const props = defineProps({
    rating: {
        type: Number,
        required: true
    },
    name: {
        type: String,
        required: true
    }
})
const emit = defineEmits<{ (event: 'update', key: string, rating: number): void }>()

const updateRating = (id: number) => {
    emit('update', props.name, id)
}
</script>