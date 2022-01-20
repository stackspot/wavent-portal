<template>
  <n-layout-footer>
    <n-p>&copy; {{ new Date().getFullYear() }} Stackspot. All rights reserved.</n-p>
  </n-layout-footer>
</template>

<script setup>
import { Icon } from '@/components'

</script>

<style scoped>
.n-layout-footer {
  opacity: 0.6;
  padding: 24px;
  text-align: center;
}
</style>