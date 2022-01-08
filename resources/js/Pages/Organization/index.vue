<template>
  <n-thing content-indented>
    <template #avatar>
      <n-avatar>
        <n-upload action="https://www.mocky.io/v2/5e4bafc63100007100d8b70f" list-type="image" />
      </n-avatar>
    </template>
    <template #header>Company Info</template>
    <template #description>Description</template>
    <n-form inline :label-width="80" :model="formValue" :rules="rules" :size="size" ref="formRef">
      <n-form-item label="Name" path="user.name">
        <n-input v-model:value="formValue.user.name" placeholder="Input Name" />
      </n-form-item>
      <n-form-item label="Name" path="user.name">
        <n-input v-model:value="formValue.user.name" placeholder="Input Name" />
      </n-form-item>
      <n-form-item label="Name" path="user.name">
        <n-input v-model:value="formValue.user.name" placeholder="Input Name" />
      </n-form-item>
    </n-form>
    <template #footer>Footer</template>
    <template #action>
      <n-space>
        <n-button size="small">1$</n-button>
        <n-button size="small">10$</n-button>
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