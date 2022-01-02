<template>
  <n-layout-sider
    :width="220"
    :native-scrollbar="false"
    :collapsed="collapsed"
    collapse-mode="width"
    show-trigger="bar"
    bordered
    @update:collapsed="toggle"
  >
    <inertia-link href="/" class="n-a logo">
      <wavent-icon></wavent-icon>
      <span>Wavent</span>
    </inertia-link>
    <n-menu
      :value="currentKey"
      :default-expanded-keys="expandedKeys"
      :options="options"
      :root-indent="18"
      @update:value="k => { currentKey = k }"
    />
  </n-layout-sider>
</template>

<script setup>
import { h, ref, computed, watchEffect } from 'vue'
import { Link as InertiaLink } from '@inertiajs/inertia-vue3'
import { usePage } from '@inertiajs/inertia-vue3'
import { Inertia } from '@inertiajs/inertia'
//import { useMenus } from '@/composables'
import { Icon, WaventIcon } from '@/components'

const collapsed = ref(false)

const toggle = async () => {
  collapsed.value = !collapsed.value
}

// TODO: loading state
const menus = ref([
  {
    label: 'Painel',
    id: 'dashboard',
    url: '/admin/painel',
    icon: 'dashboard',
    children: null,
  },
  {
    label: 'Calendário',
    id: 'calendar',
    url: '/admin/calendario',
    icon: 'calendar',
    children: null,
  },
  {
    label: 'Clientes',
    id: 'clients',
    url: '/admin/clients',
    icon: 'clients',
    children: null,
  },
  {
    label: 'Equipa',
    id: 'staff',
    url: '/admin/equipa',
    icon: 'team',
    children: null,
  },
  {
    label: 'Serviços',
    id: 'services',
    url: '/admin/servicos',
    icon: 'services',
    children: null,
  },
  {
    label: 'Definições',
    id: 'settings',
    url: '/admin/definicao',
    icon: 'settings',
    children: null,
  },
])

const page = usePage()

const mapping = (items) => items.map(item => ({
  ...item,
  key: item.id,
  label: item.url != null ? () => h(InertiaLink, { href: item.url }, { default: () => item.label }) : item.label,
  icon: item.icon != null ? () => h(Icon, { type: item.icon }) : undefined,
  children: item.children && mapping(item.children)
}))

const options = computed(() => (menus.value ? mapping(menus.value) : []))

const currentKey = ref('')
const expandedKeys = ref([])

const routeMatched = (menu) => {
  return page.url.value === menu.url && (menu.params == null || JSON.stringify(page.url.value) === JSON.stringify(menu.params))
}

const matchExpanded = (items) => {
  let matched = false
  for (const item of items) {
    if (item.children != null) {
      matchExpanded(item.children) && expandedKeys.value.push(item.id)
    }
    if (routeMatched(item)) {
      currentKey.value = item.id
      matched = true
    }
  }
  return matched
}

//watchEffect(() => menus.value && matchExpanded(menus.value))
</script>

<style scoped>
.logo {
  position: sticky;
  top: 0;
  z-index: 1;
  display: flex;
  align-items: center;
  padding: 12px 20px;
  /* border-bottom: 1px solid var(--border-color); */
  background: var(--color);
  font-size: 1.8em;
  font-weight: 600;
  line-height: 1;
  text-decoration: none;
  transition: padding 0.3s var(--bezier), font-size 0.3s var(--bezier);
}

.n-layout-sider--collapsed .logo {
  padding: 8px;
  font-size: 0;
}

.logo svg {
  flex: 0 0 32px;
  height: 32px;
  margin-right: 12px;
  transition: margin 0.3s var(--bezier);
}

.n-layout-sider--collapsed .logo svg {
  margin-right: 0;
}
</style>