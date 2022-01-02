<template>
  <n-layout-footer>
    <n-p>
      <n-a href="https://github.com/zce/fearless">
        <icon type="code"></icon>
      </n-a>with
      <n-text type="error">♥</n-text>by
      <n-a href="https://zce.me">devjames</n-a>
    </n-p>
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
.n-a {
  text-decoration: none;
}
</style>