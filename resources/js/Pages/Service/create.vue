<template>
  <n-page-header class="mb-6">
    <template #title>
      <n-breadcrumb>
        <n-breadcrumb-item @click="$inertia.get(route('services.index'))">Serviços</n-breadcrumb-item>
        <n-breadcrumb-item>Novo Serviço</n-breadcrumb-item>
      </n-breadcrumb>
    </template>
  </n-page-header>
  <div class="max-w-2xl w-full mx-auto" cols="12">
    <n-alert
      v-if="showError"
      title="campos Vázios"
      type="error"
      closable
      class="mb-4"
    >Preencha os campos obrigatórios.</n-alert>
    <n-form :model="service" ref="formRef" :rules="rules" label-placement="top">
      <n-grid cols="12" item-responsive responsive="screen" :x-gap="24">
        <n-form-item-gi span="12" label="Nome do serviço" path="name">
          <n-input placeholder="Input" v-model:value="service.name" />
        </n-form-item-gi>
        <n-form-item-gi span="12 m:6" label="Preço do serviço" path="price">
          <n-input-number v-model:value="service.price" :step="0.01" placeholder="Preço do serviço">
            <template #prefix>€</template>
          </n-input-number>
        </n-form-item-gi>
        <n-form-item-gi span="12 m:6" label="Duração do serviço" path="duration">
          <n-select
            v-model:value="service.duration"
            :options="options"
            placeholder="Duração do serviço"
          />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="Atribuir ao pessoal" path="staff">
          <n-select
            v-model:value="service.staff"
            :options="staffOptions"
            placeholder="Atribuir ao pessoal"
            multiple
            :max-tag-count="3"
          />
        </n-form-item-gi>
      </n-grid>
      <n-space>
        <n-button
          :desabled="service.processing"
          @click="createService"
          type="primary"
          :loading="service.processing"
        >Adicionar serviço</n-button>
      </n-space>
    </n-form>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useForm, usePage } from "@inertiajs/inertia-vue3"
import { useRoute } from '@/composables'

const formRef = ref(null)
const showError = ref(false)
const { route } = useRoute()
const page = usePage()

const props = defineProps({
  errors: Object
})

const service = useForm({
  price: null,
  name: null,
  duration: null,
  staff: null,
  description: ''
})

const rules = {
  price: {
    required: true,
    message: 'Digite o preço do serviço'
  },
  name: {
    required: true,
    message: 'Digite o nome do serviço'
  },
  duration: {
    required: true,
    message: 'Escolha a duração do serviço'
  }
}
const createService = () => {
  formRef.value.validate((errors) => {
    if (!errors) {
      service.post(route('service.store'))
    }
    showError.value = true
  })
}
const generateTime = () => {
  let quarterHours = ["00", "15", "30", "45"];
  let times = [];
  for (let i = 0; i < 24; i++) {
    for (let j = 0; j < 4; j++) {
      let time = i + "h" + quarterHours[j] + "min";
      if (i < 10) {
        time = "0" + time;
      }
      times.push(time);
    }
    return times
  }
}
const staffOptions = [
  {
    label: 'John',
    value: 123
  },
  {
    label: 'Jack',
    value: 342
  },
  {
    label: "David",
    value: 264
  }
]
const options = [
  {
    label: "15min",
    value: 900,
  },
  {
    label: "30min",
    value: 1800,
  },
  {
    label: "45min",
    value: 2700,
  },
  {
    label: "1h",
    value: 3600,
  },
  {
    label: "1h15min",
    value: 4500,
  },
  {
    label: "1h30min",
    value: 5400,
  },
  {
    label: "1h45min",
    value: 8100,
  },
  {
    label: "2h",
    value: 9000,
  },
]
const bodyStyle = {
  width: '600px'
}

const segmentes = {
  content: 'soft',
  footer: 'soft'
}

</script>