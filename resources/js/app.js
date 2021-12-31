import { createApp, h } from 'vue'

import { app, Link, plugin } from '@inertiajs/inertia-vue3'
import { InertiaProgress as progress } from '@inertiajs/progress'

import VueApexCharts from 'vue3-apexcharts'

import ElementPlus from 'element-plus'
import 'element-plus/theme-chalk/index.css'
import 'element-plus/theme-chalk/display.css'

/* import route from 'ziggy-js'
import { Ziggy } from '@/routes' */

const el = document.getElementById('app')

progress.init()

const vueApp = createApp({
	render: () =>
		h(app, {
			initialPage: JSON.parse(el.dataset.page),
			resolveComponent: (name) => {
				const page = require(`./Pages/${name}`).default
				page.layout = page.layout
				return page
			},
		}),
})
	.use(plugin)
	.use(ElementPlus)
	.use(VueApexCharts)
	.component('inertia-link', Link)

vueApp.mount(el)
