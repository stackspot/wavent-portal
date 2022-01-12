<template>
  <n-layout-sider
    :width="220"
    :native-scrollbar="false"
    :collapsed="state.openSideBar"
    collapse-mode="width"
    show-trigger="bar"
    bordered
    @update:collapsed="toggleSidebar"
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
import { computed, watchEffect } from 'vue'
import { useMenus, useState } from '@/composables'
import { WaventIcon } from '@/components'

const { state, toggleSidebar } = useState()
const { menus, mapping, matchExpanded, currentKey, expandedKeys } = useMenus()


/* const toggleCollapsed = async () => {
		toggleSidebar()
	} */
const options = computed(() => (menus.value ? mapping(menus.value) : []))
watchEffect(() => menus.value && matchExpanded(menus.value))
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