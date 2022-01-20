<template>
  <div>
    <n-page-header class="mb-6">
      <template #title>
        <n-breadcrumb>
          <n-breadcrumb-item>
            <n-h2>Serviços</n-h2>
          </n-breadcrumb-item>
        </n-breadcrumb>
      </template>
      <template #extra>
        <n-space>
          <n-button @click="$inertia.get(route('service.create'))">Novo Serviço</n-button>
        </n-space>
      </template>
    </n-page-header>
    <n-data-table
      :columns="columns"
      :data="data"
      :pagination="pagination"
      class="max-w-2xl mx-auto"
    />
    <n-modal
      v-model:show="showModal"
      preset="card"
      title="Modal"
      class="max-w-sm"
      :bordered="false"
      size="huge"
      :segmented="{
        content: 'soft',
        footer: 'soft'
      }"
    >
      <n-alert
        v-if="showError"
        title="Compos Vázios"
        type="error"
        closable
        class="mb-4"
      >Preencha os campos obrigatórios.</n-alert>
      <n-form :model="serviceEdit" :rules="rules" ref="formRef" label-placement="top">
        <n-grid cols="12" responsive="screen" :x-gap="24">
          <n-form-item-gi :span="12" label="Nome do serviço" path="name">
            <n-input placeholder="Input" v-model:value="serviceEdit.name" />
          </n-form-item-gi>
          <n-form-item-gi :span="12" label="Preço do serviço" path="price">
            <n-input-number
              v-model:value="serviceEdit.price"
              :step="0.01"
              placeholder="Preço do serviço"
            >
              <template #prefix>€</template>
            </n-input-number>
          </n-form-item-gi>
          <n-form-item-gi :span="12" label="Duração do serviço" path="duration">
            <n-time-picker
              v-model:value="serviceEdit.duration"
              placeholder="Duração do serviço"
              :minutes="15"
              format="HH:mm"
            />
          </n-form-item-gi>
          <!-- <n-form-item-gi :span="12" label="Atribuir ao pessoal" path="stuff">
            <n-select
              v-model:value="serviceEdit.staff"
              :options="staffOptions"
              placeholder="Atribuir ao pessoal"
              multiple
              :max-tag-count="3"
            />
          </n-form-item-gi>-->
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
    </n-modal>
  </div>
</template>

<script setup>
import { h, ref } from 'vue'
import { NNumberAnimation, NButton, NSpace, NTime, useDialog, useMessage } from 'naive-ui'
import { Inertia } from '@inertiajs/inertia'
import { useRoute } from '@/composables'
import { getTime, parseISO, toDate } from 'date-fns'

const dialog = useDialog()
const message = useMessage()
const { route } = useRoute()
const serviceEdit = ref(null)
const showModal = ref(false)
const loading = ref(false)
const formRef = ref(null)
const showError = ref(null)

const props = defineProps({
  services: Array
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

const createColumns = ({ editService, deleteService }) => {
  return [
    {
      title: 'Nome',
      key: 'name'
    },
    {
      title: 'Preço',
      key: 'price',
      render (row) {
        return h(NNumberAnimation,
          {
            precision: 2,
            duration: 500,
            to: row.price,
          }
        )
      }
    },
    {
      title: 'Duração',
      key: 'duration',
      render (row) {
        return h(NTime,
          {
            format: 'HH:mm',
            time: getTime(parseISO(row.duration))
          }
        )
      }
    },
    {
      title: '',
      key: 'editar',
      render (row) {
        return h(NSpace,
          {},
          {
            default: () => [
              h(NButton,
                {
                  size: 'small',
                  type: 'info',
                  onClick: () => editService(row)
                },
                { default: () => 'Editar' }),
              h(NButton,
                {
                  size: 'small',
                  type: 'error',
                  onClick: () => deleteService(row)
                },
                { default: () => 'Delete' })
            ]
          })
      }
    }
  ]
}

const editService = (rowData) => {
  serviceEdit.value = {
    id: rowData.id,
    name: rowData.name,
    price: rowData.price,
    duration: getTime(parseISO(rowData.duration))
  }
  showModal.value = true
}

const updateService = async () => {
  formRef.value.validate((errors) => {
    if (!errors) {
      loading.value = true
      Inertia.post(route('service.update', serviceEdit.value.id),
        {
          name: serviceEdit.value.name,
          price: serviceEdit.value.price,
          duration: toDate(serviceEdit.value.duration),
        }, {
        onSuccess: () => {
          showModal.value = false
          loading.value = false
        },
        onError: () => {
          loading.value = false
        }
      })
    } else {
      showError.value = true
    }
  })

}

const deleteService = (rowData) => {
  dialog.warning({
    title: 'Apagar serviço',
    content: 'O serviço será apagado permanentemente. Tens a certeza?',
    positiveText: 'Sim, apagar!',
    negativeText: 'Cancelar',
    onPositiveClick: () => {
      Inertia.delete(route('service.delete', rowData.id))
      Inertia.reload({ only: ['services'] })
    },
    onNegativeClick: () => {
      message.error('Operação cancelado!')
    }
  })
}
const data = props?.services
const columns = createColumns({ editService, deleteService })

const pagination = {
  pageSize: 10
}
</script>

<style scoped>
.n-h2 {
  margin-bottom: 0;
}
</style>