<template>
  <n-page-header class="mb-6">
    <template #title>
      <n-breadcrumb>
        <n-breadcrumb-item @click="$inertia.get(route('service.index'))">Serviços</n-breadcrumb-item>
        <n-breadcrumb-item>Editar Serviço</n-breadcrumb-item>
      </n-breadcrumb>
    </template>
  </n-page-header>
  <div class="max-w-2xl w-full mx-auto" cols="12">
    <n-alert
      v-if="showError"
      title="Compos Vázios"
      type="error"
      closable
      class="mb-4"
    >Preencha os campos obrigatórios.</n-alert>
    <n-form :model="serviceModel" :rules="rules" ref="formRef" label-placement="top">
      <n-grid cols="12" responsive="screen" :x-gap="24">
        <n-form-item-gi :span="12" label="Nome do serviço" path="name">
          <n-input placeholder="Input" v-model:value="serviceModel.name" />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="Preço do serviço" path="price">
          <n-input-number
            v-model:value="serviceModel.price"
            :step="0.01"
            placeholder="Preço do serviço"
          >
            <template #prefix>€</template>
          </n-input-number>
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="Duração do serviço" path="duration">
          <n-time-picker
            v-model:value="serviceModel.duration"
            placeholder="Duração do serviço"
            :minutes="15"
            format="HH:mm"
          />
        </n-form-item-gi>
        <n-form-item-gi :span="12" label="Atribuir ao pessoal" path="stuff">
          <n-select
            v-model:value="serviceModel.staff"
            :options="staffOptions"
            placeholder="Atribuir ao pessoal"
            multiple
            :max-tag-count="3"
          />
        </n-form-item-gi>
      </n-grid>
      <n-space>
        <n-button
          :desabled="loading"
          @click="updateService"
          type="primary"
          :loading="loading"
        >Guardar Alteração</n-button>
      </n-space>
    </n-form>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
//import { useForm } from "@inertiajs/inertia-vue3"
import { Inertia } from '@inertiajs/inertia'
import { useRoute } from '@/composables'
import { getUnixTime, parseISO } from 'date-fns'

const formRef = ref(null)
const showError = ref(false)

const { route } = useRoute()

const props = defineProps({
  service: Object
})

const serviceModel = reactive({
  name: props.service?.name,
  price: props.service?.price,
  duration: parseISO(props.service?.duration)
})
const loading = ref(false)

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
const updateService = () => {
  formRef.value.validate((errors) => {
    if (!errors) {
      loading.value = true
      Inertia.post(route('service.update', service?.id), serviceModel, {
        onSuccess: () => loading.value = false,
        onError: () => {
          loading.value = false
          showError.value = true
        },
      })
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
</script>