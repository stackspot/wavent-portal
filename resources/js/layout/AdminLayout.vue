<template>
  <base-layout>
    <n-layout position="absolute" has-sider>
      <sidebar />
      <n-layout :native-scrollbar="false">
        <Header />
        <Content />
        <Footer />
      </n-layout>
    </n-layout>
  </base-layout>
</template>

<script setup>
import BaseLayout from './BaseLayout.vue'
import Sidebar from './sidebar.vue'
import Header from './header.vue'
import Content from './content.vue'
import Footer from './footer.vue'
// workbench
</script>