<template>
  <n-page-header class="mb-6">
    <template #title>
      <n-breadcrumb>
        <n-breadcrumb-item>Serviços</n-breadcrumb-item>
        <n-breadcrumb-item>Novo Serviço</n-breadcrumb-item>
      </n-breadcrumb>
    </template>
  </n-page-header>
  <div class="max-w-2xl w-full mx-auto" cols="12">
    <n-form :model="service" ref="formRef" label-placement="top">
      <n-grid cols="12" responsive="screen" :x-gap="24">
        <n-form-item-gi
          :span="12"
          label="Nome do serviço"
          path="service_name"
          :feadback="service.name?.errors"
          :validation-status="service.name?.errors ? 'error' : ''"
        >
          <n-input placeholder="Input" v-model:value="service.name" />
        </n-form-item-gi>
        <n-form-item-gi
          :span="12"
          label="Preço do serviço"
          path="service_price"
          :feadback="service.price?.errors"
          :validation-status="service.price?.errors ? 'error' : ''"
        >
          <n-input-number v-model:value="service.price" :step="0.01" placeholder="Preço do serviço">
            <template #prefix>€</template>
          </n-input-number>
        </n-form-item-gi>
        <n-form-item-gi
          :span="12"
          label="Duração do serviço"
          path="service_duration"
          :feadback="service.duration?.errors"
          :validation-status="service.duration?.errors ? 'error' : ''"
        >
          <n-select
            v-model:value="service.duration"
            :options="options"
            placeholder="Duração do serviço"
          />
        </n-form-item-gi>
        <n-form-item-gi
          :span="12"
          label="Atribuir ao pessoal"
          path="service_duration"
          :feadback="service.staff?.errors"
          :validation-status="service.staff?.errors ? 'error' : ''"
        >
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
        <n-button :desabled="service.processing" @click="createService">Adicionar serviço</n-button>
      </n-space>
    </n-form>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useForm } from "@inertiajs/inertia-vue3"


const service = useForm({
  price: null,
  name: null,
  duration: null,
  staff: null,
  description: ''
})

const createService = () => {
  service.post('/admin/servicos')
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