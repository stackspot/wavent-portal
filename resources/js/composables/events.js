import { createSharedComposable } from '@vueuse/core'

export default createSharedComposable(function useEvents() {
	let events = ref([
		{
			start: '2021-12-22 10:35',
			end: '2021-12-22 12:30',
			title: 'Doctor appointment',
		},
		{
			start: '2021-12-22 18:30',
			end: '2021-12-22 19:15',
			title: 'Dentist appointment',
		},
		{
			start: '2021-12-23 18:30',
			end: '2021-12-23 19:30',
			title: 'Crossfit',
		},
		{
			start: '2021-12-24 12:00',
			end: '2021-12-24 13:00',
			title: 'Brunch with Jane',
		},
		{
			start: '2021-12-25 19:00',
			end: '2021-12-25 19:45',
			title: 'Swimming lesson',
		},
		{
			start: '2021-12-30 19:00',
			end: '2021-12-30 19:45',
			title: 'Swimming lesson',
		},
		{
			start: '2021-12-26 12:00',
			end: '2021-12-26 14:00',
			title: 'LUNCH',
			class: 'lunch',
			background: true,
		},
		{
			start: '2021-12-27 12:00',
			end: '2021-12-27 14:00',
			title: 'LUNCH',
			class: 'lunch',
			background: true,
		},
	])

	return { events }
})
