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
      <svg viewBox="0 0 472 450">
        <defs>
          <mask id="mask" fill="#fff">
            <path
              d="M472 114.26L203.029 335.74H407.1L472 449.48H64.9L0 335.74l268.971-221.48H64.9L0 .52h407.1z"
            />
          </mask>
          <filter
            id="shadow"
            x="-12.7%"
            y="-13.4%"
            width="125.4%"
            height="126.7%"
            filterUnits="objectBoundingBox"
          >
            <feOffset in="SourceAlpha" result="offset-outer" />
            <feGaussianBlur stdDeviation="20" in="offset-outer" result="blue-outer" />
            <feComposite in="blue-outer" in2="SourceAlpha" operator="out" result="blue-outer" />
            <feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0" in="blue-outer" />
          </filter>
        </defs>
        <g mask="url(#mask)">
          <path fill="currentColor" d="M0 0h472v449H0z" />
          <path d="M0 335.74l64.9 113.74L472 114.26 407.1.52z" filter="url(#shadow)" />
        </g>
      </svg>
      <span>Jack</span>
    </inertia-link>
    <!-- <n-menu :value="currentKey" :default-expanded-keys="expandedKeys" :options="options" :root-indent="18" @update:value="k => { currentKey = k }" /> -->
  </n-layout-sider>
</template>

<script setup>
import { h, ref, computed, watchEffect } from 'vue'
//import { useMenus, Menu } from '@/composables'
import { Icon } from '@/components'
import { Link as InertiaLink } from '@inertiajs/inertia-vue3'
import { usePage } from '@inertiajs/inertia-vue3'
import { Inertia } from '@inertiajs/inertia'

const collapsed = ref(false)

const toggle = async () => {
  collapsed.value = !collapsed.value
}

// TODO: loading state
//const { data: menus } = useMenus()

const page = usePage()

/* const mapping = (items) => items.map(item => ({
  ...item,
  key: item.id,
  label: item.name != null ? () => h(InertiaLink, { href: item }, { default: () => item.label }) : item.label,
  icon: item.icon != null ? () => h(Icon, { type: item.icon }) : undefined,
  children: item.children && mapping(item.children)
})) */

//const options = computed(() => (menus.value ? mapping(menus.value) : []))

const currentKey = ref('')
const expandedKeys = ref([])

const routeMatched = (menu) => {
  return page.url.value === menu.name && (menu.params == null || JSON.stringify(page.url.value) === JSON.stringify(menu.params))
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