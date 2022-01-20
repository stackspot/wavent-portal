import { createSharedComposable } from '@vueuse/core'
import route from 'ziggy-js'
import { Ziggy } from '@/routes'

export const useRoute = createSharedComposable(() => {
	const routes = (name, params = {}, absolute = true) => {
		return route(name, params, absolute, Ziggy)
	}

	return { route: routes }
})
