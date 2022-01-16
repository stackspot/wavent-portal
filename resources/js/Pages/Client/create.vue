<template>
  <n-page-header>
    <template #title>
      <n-breadcrumb>
        <n-breadcrumb-item @click="$inertia.get('/admin/cliente')">Clientes</n-breadcrumb-item>
        <n-breadcrumb-item>Novo cliente</n-breadcrumb-item>
      </n-breadcrumb>
    </template>
  </n-page-header>
  <div class="max-w-2xl w-full mx-auto mt-6" cols="12">
    <n-form :model="client" ref="formRef" label-placement="top">
      <n-grid cols="12" responsive="screen" :x-gap="24">
        <n-form-item-gi :span="12" label="Nome" path="client_name">
          <n-input placeholder="Nome" v-model:value="client.name" />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="Email" path="client_email">
          <n-input type="email" placeholder="Email" v-model:value="client.email" />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="Nº tlemovel" path="client_phone">
          <n-input type="phone" placeholder="Nº Telemovel" v-model:value="client.phone" />
        </n-form-item-gi>
      </n-grid>
      <n-space>
        <n-button
          @click="createClient"
          :disabled="client.processing"
          :loading="client.processing"
        >Adicionar cliente</n-button>
      </n-space>
    </n-form>
  </div>
</template>

<script setup>
//import { ref, reactive } from 'vue'
import { useForm } from '@inertiajs/inertia-vue3'
import { useRoute } from '@/composables'

const { route } = useRoute()

const client = useForm({
  name: null,
  email: null,
  phone: null,
})

const createClient = () => {
  try {
    client.post(route('client.store'))
  } catch (e) {
    console.log(e)
  }
}
</script>