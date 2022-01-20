<template>
  <n-thing content-indented>
    <template #avatar>
      <n-avatar></n-avatar>
    </template>
    <template #header>Company name</template>
    <template #description>Description</template>
    Money is any item or verifiable record that is generally accepted as payment
    for goods and services and repayment of debts, such as taxes, in a particular
    country or socio-economic context.
    <template
      #footer
    >Footer</template>
    <template #action>
      <n-space>
        <n-button size="small">10$</n-button>
        <n-button size="small">100$</n-button>
      </n-space>
    </template>
  </n-thing>
</template>

<script>
export default {

}
</script>

<style>
</style>