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
import { BaseLayout, Sidebar, Header, Content, Footer } from './index'
// workbench
</script>