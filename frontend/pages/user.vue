<template>
    <div>Hello from user settings page</div>
</template>

<script setup lang="ts">
definePageMeta({
    middleware: ['auth'],
})
</script>