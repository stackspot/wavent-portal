<template>
  <n-card class="max-w-sm mx-auto mt-6">
    <template #header>Criar uma Conta</template>
    <n-form :model="user" ref="formRef" :rules="rules">
      <n-form-item path="name" label="Nome">
        <n-input v-model:value="user.name" @keydown.enter.prevent placeholder="Ex. João Silva" />
      </n-form-item>
      <n-form-item path="email" label="Email">
        <n-input v-model:value="user.email" @keydown.enter.prevent placeholder="Email" />
      </n-form-item>
      <n-form-item path="password" label="Palavra-passe">
        <n-input v-model:value="user.password" type="password" @keydown.enter.prevent />
      </n-form-item>
      <n-form-item first path="confirm_password" label="Confirmar Palavra-passe">
        <n-input
          :disabled="!user.password"
          v-model:value="user.password_confirmation"
          type="password"
          @keydown.enter.prevent
        />
      </n-form-item>
    </n-form>
    <template #action>
      <n-button type="primary" @click="register">Criar Conta</n-button>
      <n-button text @click="$inertia(route('login'))">Já tem conta? Entrar!</n-button>
    </template>
  </n-card>
</template>

<script>
import { AuthLayout } from '@/layout'

export default {
  layout: AuthLayout
}
</script>
<script setup>
import { ref } from 'vue'
import { useForm } from '@inertiajs/inertia-vue3'
import { useMessage } from 'naive-ui'
import { useRoute } from '@/composables'

const formRef = ref(null)
const message = useMessage()
const { route } = useRoute()

const user = useForm({
  name: null,
  email: null,
  phone: null,
  password: null,
  password_confirmation: null
})

function validatePasswordStartWith (rule, value) {
  return (
    user.value.password &&
    user.value.password.startsWith(value) &&
    user.value.password.length >= value.length
  )
}

function validatePasswordSame (rule, value) {
  return value === user.value.password
}

const rules = {
  password: [
    {
      required: true,
      message: 'Palavra-passe obrigatório!'
    }
  ],
  confirm_password: [
    {
      required: true,
      message: 'Confirmar palavra-passe obrigatório!',
      trigger: ['input', 'blur']
    },
    {
      validator: validatePasswordStartWith,
      message: 'Palavra-passes não são iguais!',
      trigger: 'input'
    },
    {
      validator: validatePasswordSame,
      message: 'Palavra-passes não são iguais!',
      trigger: ['blur']
    }
  ]
}

function register (e) {
  e.preventDefault()
  formRef.value.validate((errors) => {
    if (!errors) {
      user.post(route('register.store'))
    } else {
      console.log(errors)
      message.error('Invalid')
    }
  })
}
</script>

<style>
</style>