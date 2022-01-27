<template>
  <n-page-header class="mb-6">
    <template #title>
      <n-breadcrumb>
        <n-breadcrumb-item @click="$inertia.get('/admin/equipa')">Equipa</n-breadcrumb-item>
        <n-breadcrumb-item>Editar membro</n-breadcrumb-item>
      </n-breadcrumb>
    </template>
  </n-page-header>
  <div class="max-w-2xl w-full mx-auto" cols="12">
    <n-alert type="error" closable v-if="errors" class="mb-4">
      <n-list>
        <n-list-item v-for="(error, index) in errors" :key="index">{{ error }}</n-list-item>
      </n-list>
    </n-alert>
    <n-form :model="staff" ref="formRef" label-placement="top">
      <n-grid cols="12" responsive="screen" :x-gap="24">
        <n-form-item-gi :span="12" label="Nome" path="staff_name">
          <n-input placeholder="Nome" v-model:value="staff.name" />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="Email" path="staff_email">
          <n-input type="email" placeholder="Email" v-model:value="staff.email" />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="Nº tlemovel" path="staff_phone">
          <n-input type="phone" placeholder="Nº Telemovel" v-model:value="staff.phone" />
        </n-form-item-gi>>
        <n-form-item-gi :span="12" label="Servoços" path="service_duration">
          <n-select
            v-model:value="staff.services"
            :options="services"
            placeholder="Atribuir serviço ao novo membro"
            multiple
            :max-tag-count="3"
          />
        </n-form-item-gi>
      </n-grid>
      <n-space>
        <n-button
          @click="updateStaff"
          :disabled="loading"
          type="primary"
          :loading="loading"
        >Guardar membro</n-button>
      </n-space>
    </n-form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { Inertia } from "@inertiajs/inertia"
import { useRoute } from '@/composables'

const props = defineProps({
  staff: Object,
  services: Array,
})

const errors = ref(null)
const loading = ref(false)
const { route } = useRoute()

const updateStaff = () => {
  loading.value = true
  Inertia.post(route('staff.update', props.staff.id), props.staff, {
    onSuccess: () => loading.value = false,
    onError: (e) => {
      errors.value = e
      loading.value = false
    },
  })
}


</script>