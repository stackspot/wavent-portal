<template>
  <n-card class="max-w-sm mx-auto mt-6">
    <template #header>Criar uma Conta</template>
    <n-form :model="user" ref="formRef" :rules="rules">
      <n-form-item path="name" label="Nome">
        <n-input v-model:value="user.name" @keydown.enter.prevent placeholder="Ex. João Silva" />
      </n-form-item>
      <n-form-item path="email" label="Email">
        <n-input
          type="email"
          v-model:value="user.email"
          @keydown.enter.prevent
          placeholder="Email"
        />
      </n-form-item>
      <n-form-item path="phone" label="Nº Telemovel">
        <n-input
          type="tel"
          v-model:value="user.phone"
          @keydown.enter.prevent
          placeholder="Nº Telemovel"
        />
      </n-form-item>
      <n-form-item path="password" label="Palavra-passe">
        <n-input
          v-model:value="user.password"
          :minlength="8"
          show-password-on="mousedown"
          type="password"
          @keydown.enter.prevent
        />
      </n-form-item>
      <n-form-item path="confirm_password" label="Confirmar Palavra-passe">
        <n-input
          :disabled="!user.password"
          v-model:value="user.password_confirmation"
          type="password"
          :minlength="8"
          show-password-on="mousedown"
          @keydown.enter.prevent
        />
      </n-form-item>
      <n-divider>Ou Registar com</n-divider>
      <n-space justify="space-between">
        <n-button type="success">
          <template #icon>
            <Icon type="google"></Icon>
          </template>
          Google
        </n-button>
        <n-button type="info">
          <template #icon>
            <Icon type="facebook"></Icon>
          </template>
          Facebook
        </n-button>
      </n-space>
    </n-form>
    <template #action>
      <n-space justify="space-between" align="center">
        <n-button type="primary" @click="register">Registar</n-button>
        <n-button text @click="$inertia.get(route('login'))">Já tem conta? Entrar!</n-button>
      </n-space>
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
import { Icon } from '@/components'

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
    user.password &&
    user.password.startsWith(value) &&
    user.password.length >= value.length
  )
}

function validatePasswordSame (rule, value) {
  return user.password_confirmation === user.password
}

const rules = {
  email: {
    required: true,
  },
  name: {
    required: true,
  },
  password: {
    required: true,
    message: 'Palavra-passe obrigatório!'
  }
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