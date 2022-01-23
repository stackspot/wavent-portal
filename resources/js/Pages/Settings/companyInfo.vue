<template>
  <n-form :model="company" ref="formRef" label-placement="top" class="max-w-md md:mx-auto">
    <n-grid cols="12" responsive="screen" :x-gap="24">
      <n-form-item-gi :span="12" label="Nome" path="name">
        <n-input placeholder="Nome" v-model:value="company.name" />
      </n-form-item-gi>
      <n-form-item-gi :span="12" label="Email" path="email">
        <n-input type="email" placeholder="Email" v-model:value="company.email" />
      </n-form-item-gi>
      <n-form-item-gi :span="12" label="Nº telemovel" path="phone">
        <n-input type="tel" placeholder="Nº Telemovel" v-model:value="company.phone" />
      </n-form-item-gi>
      <n-form-item-gi :span="12" label="Endereço" path="address">
        <n-input placeholder="Endereço" v-model:value="company.address" />
      </n-form-item-gi>
      <n-form-item-gi :span="12" label="Descrição" path="description">
        <n-input
          type="textarea"
          placeholder="Breve descrição da empresa"
          v-model:value="company.description"
        />
      </n-form-item-gi>
    </n-grid>
    <n-space>
      <n-button type="primary" @click="createProvider">Guardar</n-button>
    </n-space>
  </n-form>
</template>

<script setup>
import { ref, onBeforeMount } from 'vue'
import { Inertia } from '@inertiajs/inertia'
import axios from 'axios'
import { useRoute } from '@/composables'

const logoUpdalod = ref()
const brandUpdalod = ref()
const provider = ref(null)
const { route } = useRoute()

const company = ref({
  name: null,
  email: null,
  phone: null,
  address: null,
  description: null,
  logo: null,
  brand_image: null,
})

const getProvider = async () => {
  const response = await axios.get(route('provider.index'))
  provider.value = response.data.provider
  company.value = provider.value
}

/* const toBase64 = file => new Promise((resolve, reject) => {
  const reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onload = () => resolve(reader.result);
  reader.onerror = error => reject(error);
})

const handleLogoChange = async ({ file }) => {
  company.value.logo = await toBase64(file.file)
}
const handleBrandChange = async ({ file }) => {
  company.value.brand_image = await toBase64(file.file)
} */
const createProvider = () => {
  Inertia.post(route('provider.store'), company.value, {
    onSuccess: () => getProvider(),
    onError: (e) => console.log(e)
  })
}

onBeforeMount(() => getProvider())
</script>

<style>
</style>