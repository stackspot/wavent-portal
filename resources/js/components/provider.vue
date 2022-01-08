<template>
  <n-config-provider :theme="theme" :breakpoints="breakpoints">
    <n-loading-bar-provider>
      <n-message-provider>
        <n-dialog-provider>
          <slot />
        </n-dialog-provider>
      </n-message-provider>
    </n-loading-bar-provider>
  </n-config-provider>
</template>

<script setup>
import { computed } from 'vue'
import { useOsTheme, darkTheme } from 'naive-ui'

const osTheme = useOsTheme()
const breakpoints = { xs: 0, s: 640, m: 768, l: 1024, xl: 1280, xxl: 1536 }
const theme = computed(() => (osTheme.value === 'dark' ? darkTheme : null))
</script>