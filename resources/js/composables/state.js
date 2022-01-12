import { createGlobalState, useStorage, useToggle } from '@vueuse/core'
import { toRef } from 'vue'

export const useState = createGlobalState(() => {
	const state = useStorage('wavent-storage', {
		openSideBar: true,
	})
	const toggleSidebar = async () => {
		state.value.openSideBar = !state.value.openSideBar
	}

	return { state, toggleSidebar }
})
