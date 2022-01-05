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
          <n-button @click="$inertia.get('/admin/servicos/novo')">Novo Serviço</n-button>
        </n-space>
      </template>
    </n-page-header>
    <n-data-table
      :columns="columns"
      :data="data"
      :pagination="pagination"
      class="max-w-2xl mx-auto"
    />
  </div>
</template>

<script setup>
import { h, ref, reactive } from 'vue'
import { NButton, NSpace, useMessage } from 'naive-ui'

const message = useMessage()

const state = reactive({
  showModal: false
})

const toggleModel = (value) => {
  state.showModel = value
}
const handleBack = () => {
  window.navigator.back()
}
const createColumns = ({ sendMail }) => {
  return [
    {
      title: 'Nome',
      key: 'name'
    },
    {
      title: 'Preço',
      key: 'price'
    },
    {
      title: 'Duração',
      key: 'duration'
    },
    {
      title: '',
      key: 'actions',
      render (row) {
        const actions = ['Editar', 'Apagar'].map((actName) => {
          return h(
            NButton,
            {
              size: 'small',
              onClick: () => sendMail(row)
            },
            { default: () => actName }
          )
        })
        return h(NSpace,
          {},
          { default: () => actions })
      }
    }
  ]
}

const createData = () => [
  {
    key: 0,
    name: 'Hair Cut',
    price: '10.00',
    duration: '1h'
  },
  {
    key: 1,
    name: 'Razor Cut',
    price: '7.00',
    duration: '45min'
  },
  {
    key: 2,
    name: 'Beard Trim',
    price: '4.00',
    duration: '30min'
  }
]
const props = defineProps({
  users: Array
})

const data = createData()
const columns = createColumns({
  sendMail (rowData) {
    message.info('Editar ' + rowData.name)
  }
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