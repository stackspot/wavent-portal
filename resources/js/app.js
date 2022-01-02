import { createApp, h } from 'vue'

import { app, Link, plugin } from '@inertiajs/inertia-vue3'
import { InertiaProgress as progress } from '@inertiajs/progress'
import { createPinia } from 'pinia'

import naive from './naive'

import route from 'ziggy-js'

import { AdminLayout } from '@/layout'

//require('windi.css')

const el = document.getElementById('app')

progress.init()

const vueApp = createApp({
	render: () =>
		h(app, {
			initialPage: JSON.parse(el.dataset.page),
			resolveComponent: (name) => {
				const page = require(`./Pages/${name}`).default
				page.layout = page.layout || AdminLayout
				return page
			},
		}),
})
	.use(plugin)
	.use(createPinia)
	.use(naive)
	.component('inertia-link', Link)

vueApp.mount(el)
