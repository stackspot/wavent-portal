<template>
  <n-card content-style="padding: 0;">
    <n-tabs type="line" size="large" :tabs-padding="20" pane-style="padding: 20px;">
      <n-tab-pane name="Horário Comercial">
        <schedules></schedules>
      </n-tab-pane>
      <n-tab-pane name="Empresa">
        <company-profile></company-profile>
      </n-tab-pane>
    </n-tabs>
  </n-card>
</template>
<script setup>
import schedules from './schedules.vue'
import CompanyProfile from './companyInfo.vue'
</script>