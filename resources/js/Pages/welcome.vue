<template>
  <div>
    <n-h2>Welcome</n-h2>
    <n-h3>{{ user_account }}</n-h3>
  </div>
</template>

<script setup>
import { AdminLayout } from '@/layout'
import { usePage } from '@inertiajs/inertia-vue3'

const props = defineProps({
  user_account: Object
})
</script>

<style>
</style>