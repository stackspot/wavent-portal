<template>
  <n-layout-header bordered class="bg-white">
    <n-button text @click="$inertia.reload()">
      <icon type="refresh" size="20" :depth="2" />
    </n-button>
    <n-space :size="20" align="center" style="line-height: 1">
      <n-tooltip>
        <template #trigger>
          <inertia-link href="/about">
            <icon type="help" size="22" :depth="2" />
          </inertia-link>
        </template>
        Dashboard help
      </n-tooltip>
      <n-popover trigger="click" placement="bottom-end" :width="300">
        <template #trigger>
          <n-badge dot processing>
            <icon type="notifications" size="22" :depth="2" />
          </n-badge>
        </template>
        <n-tabs type="line" justify-content="space-evenly" style="--pane-padding: 0">
          <n-tab-pane name="notifications" tab="Notifications (5)">
            <n-list style="margin: 0">
              <n-list-item v-for="i in 5" :key="i">Notification {{ i }}</n-list-item>
            </n-list>
          </n-tab-pane>
          <n-tab-pane name="messages" tab="Messages (6)">
            <n-list style="margin: 0">
              <n-list-item v-for="i in 6" :key="i">Message {{ i }}</n-list-item>
            </n-list>
          </n-tab-pane>
        </n-tabs>
      </n-popover>
      <n-dropdown
        placement="bottom-end"
        show-arrow
        :options="options"
        @select="handleOptionsSelect"
      >
        <n-avatar size="small" round class="bg-blue-300 text-lg">{{ currentUser.name[0] }}</n-avatar>
      </n-dropdown>
    </n-space>
  </n-layout-header>
</template>

<script setup>
import { h, computed } from 'vue'
import { useMessage, NButton } from 'naive-ui'
// import { useCurrentUser } from '@/composables'
import { Icon } from '@/components'
import { Link as InertiaLink } from '@inertiajs/inertia-vue3'
import { Inertia } from '@inertiajs/inertia'
import { useRoute, useUser } from '@/composables'

const message = useMessage()
const { route } = useRoute()
const { getUser } = useUser()

const currentUser = getUser()
const renderIcon = (icon) => {
  return h(Icon, { type: icon })
}

const labelLink = (to, label) => h(InertiaLink, { href: to }, { default: (props) => label })

const options = computed(() => [
  { key: 'me', label: `Hey, ${currentUser.name}!` },
  { key: 'divider', type: 'divider' },
  { key: 'profile', label: () => labelLink('/profile', 'Perfil'), icon: () => h(Icon, { type: 'user' }) },
  { key: 'settings', label: () => labelLink(route('settings'), 'Difinições'), icon: () => h(Icon, { type: 'settings' }) },
  { key: 'divider', type: 'divider' },
  { key: 'logout', label: () => labelLink(route('logout'), 'Sair') }
])

const handleOptionsSelect = async (key) => {
  if (key === 'me') {
    message.success(`Welcome back, ${currentUser.name}!`)
  }
}
</script>

<style scoped>
.n-layout-header {
  position: sticky;
  top: 0;
  display: flex;
  align-items: center;
  padding: 9px 18px;
  z-index: 10;
}

.n-button {
  margin-right: 15px;
}

.n-space {
  margin-left: auto;
}
</style>