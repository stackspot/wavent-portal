<template>
  <div>
    <n-page-header class="mb-6">
      <template #title>
        <n-breadcrumb>
          <n-breadcrumb-item>
            <n-h2>Equipa</n-h2>
          </n-breadcrumb-item>
        </n-breadcrumb>
      </template>
      <template #extra>
        <n-space>
          <n-button @click="$inertia.get(route('staff.create'))">Novo membro</n-button>
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

const { route } = useRoute()
const message = useMessage()
const dialog = useDialog()

const createColumns = ({ editStaff, deleteStaff }) => {
  return [
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
                  onClick: () => editStaff(row)
                },
                { default: () => 'Editar' }),
              h(NButton,
                {
                  size: 'small',
                  onClick: () => deleteStaff(row)
                },
                { default: () => 'Delete' })
            ]
          })
      }
    }
  ]
}

const createData = () => [
  {
    key: 0,
    name: 'John Brown',
    email: "john.brown@gmail.com",
    phone: '+355984672364'
  },
  {
    key: 1,
    name: 'Jim Green',
    email: "jim.green@gmail.com",
    phone: '+355963672364'
  },
  {
    key: 2,
    name: 'Joe Black',
    email: "joe.black@gmail.com",
    phone: '+355927672894'
  }
]
const props = defineProps({
  staffs: Array
})

const editStaff = (rowData) => {
  Inertia.get(route('staff.edit', rowData.id))
}

const deleteStaff = (rowData) => {
  dialog.warning({
    title: 'Apagar serviço',
    content: 'O serviço será apagado permanentemente. Tens a certeza?',
    positiveText: 'Sim, apagar!',
    negativeText: 'Cancelar',
    onPositiveClick: () => {
      Inertia.delete(route('staff.delete', rowData.id))
      Inertia.reload({ only: ['staffs'] })
    },
    onNegativeClick: () => {
      message.info('Operação cancelado!')
    }
  })
}

const data = props.staffs
const columns = createColumns({
  editStaff, deleteStaff
})

const pagination = {
  pageSize: 10
}
</script>

<style scoped>
.n-h2 {
  margin-bottom: 0;
}
</style>