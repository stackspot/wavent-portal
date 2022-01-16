<template>
  <n-page-header class="mb-6">
    <template #title>
      <n-breadcrumb>
        <n-breadcrumb-item @click="$inertia.get('/admin/equipa')">Equipa</n-breadcrumb-item>
        <n-breadcrumb-item>Novo membro</n-breadcrumb-item>
      </n-breadcrumb>
    </template>
  </n-page-header>
  <div class="max-w-2xl w-full mx-auto" cols="12">
    <n-form :model="staff" ref="formRef" label-placement="top">
      <n-grid cols="12" responsive="screen" :x-gap="24">
        <n-form-item-gi :span="12" label="Nome" path="staff_name">
          <n-input placeholder="Nome" v-model:value="staff.name" />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="Email" path="staff_email">
          <n-input type="email" placeholder="Email" v-model:value="staff.email" />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="Nº tlemovel" path="staff_phone">
          <n-input type="tel" placeholder="Nº Telemovel" v-model:value="staff.phone" />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="Serviços">
          <n-select
            v-model:value="staff.services"
            :options="servicesOptions"
            placeholder="Atribuir serviço ao novo membro"
            multiple
            :max-tag-count="3"
          />
        </n-form-item-gi>
      </n-grid>
      <n-space>
        <n-button
          @click="createStaff"
          :disabled="staff.processing"
          type="primary"
          :loading="staff.processing"
        >Adicionar membro</n-button>
      </n-space>
    </n-form>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useForm } from "@inertiajs/inertia-vue3"
import { useRoute } from '@/composables'

const props = defineProps({
  services: Array
})

const staff = useForm({
  name: null,
  email: null,
  phone: null,
  services: null,
})

const { route } = useRoute()


const createStaff = () => {
  staff.post(route('staff.store'))
}
const servicesOptions = [
  {
    label: 'Hair Cut',
    value: 123
  },
  {
    label: 'Razor Cut',
    value: 342
  },
  {
    label: 'Beard Trim',
    value: 264
  }
]

</script>