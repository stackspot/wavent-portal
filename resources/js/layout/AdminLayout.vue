<template>
  <base-layout>
    <n-layout position="absolute" has-sider>
      <sidebar />
      <n-layout :native-scrollbar="false">
        <Header />
        <n-layout-content content-style="padding: 16px; min-height: 85vh">
          <slot />
        </n-layout-content>
        <Footer />
      </n-layout>
    </n-layout>
  </base-layout>
</template>

<script setup>
import { BaseLayout, Sidebar, Header, Footer } from './index'
// workbench
</script>