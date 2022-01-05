import { createGlobalState, useStorage } from '@vueuse/core'
import { reactive } from 'vue'

export default createGlobalState(function useState() {
	const sidebar = reactive({
		open: true,
	})

	const toggleSidebar = () => {
		sidebar.open = !sidebar.open
	}

	return { sidebar, toggleSidebar }
})
