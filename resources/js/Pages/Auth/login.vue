<template>
  <n-card class="max-w-sm mx-auto mt-6">
    <template #header>Bem Vindo!</template>
    <n-alert
      type="error"
      closable
      v-if="user.errors.errors"
      class="mb-4"
    >{{ user.errors?.errors[0] }}</n-alert>
    <n-form :model="user" ref="formRef" :rules="rules">
      <n-form-item path="email" label="Email">
        <n-input type="email" v-model:value="user.email" @keydown.enter.prevent placeholder="Email" />
      </n-form-item>
      <n-form-item path="password" label="Palavra-passe">
        <n-input
          v-model:value="user.password"
          type="password"
          @keydown.enter.prevent
          show-password-on="mousedown"
        />
      </n-form-item>
      <n-button
        text
        size="tiny"
        @click="$inertia(route('password_reset'))"
      >Esqueceu a Palavra-passe?</n-button>
      <n-divider>Ou Continue com</n-divider>
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
        <n-button type="primary" @click="login">Aceder</n-button>
        <n-button text @click="$inertia.get(route('register'))">Não tem conta? Criar conta!</n-button>
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
  email: null,
  password: null,
})


const rules = {
  password: [
    {
      required: true,
      message: 'Palavra-passe obrigatório!'
    }
  ],
  email: [
    {
      required: true,
      message: 'Email obrigatório!'
    }
  ],

}

function login (e) {
  e.preventDefault()
  formRef.value.validate((errors) => {
    if (!errors) {
      user.post(route('login.store'))
    } else {
      console.log(errors)
      message.error('Invalid')
    }
  })
}
</script>

<style>
</style>