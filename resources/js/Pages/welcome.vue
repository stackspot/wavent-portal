<template>
  <div>
    <n-h2>Welcome</n-h2>
  </div>
</template>

<script setup>
import { AdminLayout } from '@/layout'
import { usePage } from '@inertiajs/inertia-vue3'

console.log(usePage().props.value.urlPrev)
</script>

<style>
</style>