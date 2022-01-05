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
          <n-button @click="$inertia.get('/admin/equipa/novo')">Novo membro</n-button>
        </n-space>
      </template>
    </n-page-header>
    <n-data-table :columns="columns" :data="data" :pagination="pagination" />
  </div>
</template>

<script setup>
import { h } from 'vue'
import { NButton, NSpace, useMessage } from 'naive-ui'

const message = useMessage()


const createColumns = ({ sendMail }) => {
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
  users: Array
})

const data = createData()
const columns = createColumns({
  sendMail (rowData) {
    message.info('send mail to ' + rowData.name)
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