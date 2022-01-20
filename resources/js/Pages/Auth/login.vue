<template>
  <n-card class="max-w-sm mx-auto mt-6">
    <template #header>Bem Vindo!</template>
    <n-form :model="user" ref="formRef" :rules="rules">
      <n-form-item path="email" label="Email">
        <n-input v-model:value="user.email" @keydown.enter.prevent placeholder="Email" />
      </n-form-item>
      <n-form-item path="password">
        <template #label>
          <n-space>
            <span>Palavra-passe</span>
            <n-button text @click="$inertia(route('password_reset'))">Esqueceu a Palavra-passe?</n-button>
          </n-space>
        </template>
        <n-input v-model:value="user.password" type="password" @keydown.enter.prevent />
      </n-form-item>
    </n-form>
    <template #action>
      <n-button type="primary" @click="login">Aceder</n-button>
      <n-button text @click="$inertia.get(route('register'))">Não tem conta? Criar conta!</n-button>
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