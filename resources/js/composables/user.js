import { usePage } from '@inertiajs/inertia-vue3'
import { createSharedComposable } from '@vueuse/core'

export const useUser = createSharedComposable(() => {
	const page = usePage()
	const getUser = () => {
		return page.props.value.auth.user
	}

	return { getUser }
})
