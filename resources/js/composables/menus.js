import { h, ref } from 'vue'
import { createSharedComposable } from '@vueuse/core'
import { usePage, Link } from '@inertiajs/inertia-vue3'
import { Icon } from '@/components'
import { useRoute } from './route'

export const useMenus = createSharedComposable(() => {
	const { route } = useRoute()
	const menuOptions = ref([
		{
			label: 'Painel',
			id: 'dashboard',
			url: route('dashboard'),
			icon: 'dashboard',
			children: null,
		},
		{
			label: 'Calendário',
			id: 'calendar',
			url: route('appointment.index'),
			icon: 'calendar',
			children: null,
		},
		{
			label: 'Clientes',
			id: 'clients',
			url: route('client.index'),
			icon: 'clients',
			children: null,
		},
		{
			label: 'Equipa',
			id: 'staff',
			url: route('staff.index'),
			icon: 'team',
			children: null,
		},
		{
			label: 'Serviços',
			id: 'services',
			url: route('service.index'),
			icon: 'services',
			children: null,
		},
		{
			label: 'Definições',
			id: 'settings',
			url: route('settings'),
			icon: 'settings',
			children: null,
		},
	])

	const currentKey = ref('') // the current menu item selected
	const expandedKeys = ref([]) // the current menu item selected expanded (for child menus)

	const page = usePage()

	const uuid = () => {
		Date.now().toString(16) +
			Math.floor((1 + Math.random()) * 0x10000).toString(16)
	}

	// mapping sidebar item to proper format
	const mapping = (items) =>
		items.map((item) => ({
			...item,
			key: item.id,
			label:
				item.url != null
					? () => h(Link, { href: item.url }, { default: () => item.label })
					: item.label,
			icon: item.icon != null ? () => h(Icon, { type: item.icon }) : undefined,
			children: item.children && mapping(item.children),
		}))

	// match each sidebar item to the correct link -> for current active link
	const routeMatched = (menu) => {
		return page.url.value === menu.url
	}

	// macth current link to the child menu so that they can expand
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

	return {
		// variables
		menus: menuOptions,
		uuid,
		currentKey,
		expandedKeys,
		// methods
		matchExpanded,
		mapping,
	}
})
