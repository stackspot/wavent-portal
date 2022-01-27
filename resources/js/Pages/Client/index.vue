<template>
  <div>
    <n-page-header class="mb-6">
      <template #title>
        <n-breadcrumb>
          <n-breadcrumb-item>
            <n-h2 class="mb-0">Clientes</n-h2>
          </n-breadcrumb-item>
        </n-breadcrumb>
      </template>
      <template #extra>
        <n-space>
          <n-button @click="$inertia.get(route('client.create'))">Novo Cliente</n-button>
        </n-space>
      </template>
    </n-page-header>
    <n-data-table :columns="columns" :data="data" :pagination="pagination" />
  </div>
</template>

<script setup>
import { h } from 'vue'
import { NButton, NSpace, useMessage, useDialog } from 'naive-ui'
import { Inertia } from '@inertiajs/inertia'
import { useRoute } from '@/composables'

const dialog = useDialog()
const message = useMessage()
const { route } = useRoute()

const createColumns = ({ editClient, deleteClient }) => {
  return [
    {
      title: 'ID',
      key: 'id'
    },
    {
      title: 'Nome',
      key: 'name'
    },
    {
      title: 'Email',
      key: 'email'
    },
    {
      title: 'Nº Telemovel',
      key: 'phone'
    },
    {
      title: '',
      key: 'actions',
      render (row) {
        return h(NSpace,
          {},
          {
            default: () => [
              h(NButton,
                {
                  size: 'small',
                  type: 'info',
                  onClick: () => editClient(row)
                },
                { default: () => 'Editar' }),
              h(NButton,
                {
                  size: 'small',
                  type: 'error',
                  onClick: () => deleteClient(row)
                },
                { default: () => 'Delete' })
            ]
          })
      }
    }
  ]
}

const props = defineProps({
  clients: Array
})

const editClient = (rowData) => {
  Inertia.get(route('client.edit', rowData.id))
}

const deleteClient = (rowData) => {
  dialog.warning({
    title: 'Apagar serviço',
    content: 'O serviço será apagado permanentemente. Tens a certeza?',
    positiveText: 'Sim, apagar!',
    negativeText: 'Cancelar',
    onPositiveClick: () => {
      Inertia.delete(route('client.delete', rowData.id))
      Inertia.reload({ only: ['clients'] })
    },
    onNegativeClick: () => {
      message.error('Operação cancelada!')
    }
  })
}
const data = props.clients
const columns = createColumns({
  editClient, deleteClient
})

const pagination = {
  pageSize: 10
}
</script>

<style scoped>
</style>