import { createSharedComposable } from '@vueuse/core'
import { reactive } from 'vue'
import { Inertia } from '@inertiajs/inertia'
import { useRoute } from './route'

let events = reactive([
	{
		start: '2022-01-12 10:35',
		end: '2022-01-12 12:30',
		title: 'Doctor appointment',
	},
	{
		start: '2022-01-12 18:30',
		end: '2022-01-12 19:15',
		title: 'Dentist appointment',
	},
	{
		start: '2022-01-13 18:30',
		end: '2022-01-13 19:30',
		title: 'Crossfit',
	},
	{
		start: '2022-01-14 12:00',
		end: '2022-01-14 13:00',
		title: 'Brunch with Jane',
	},
	{
		start: '2022-01-15 19:00',
		end: '2022-01-15 19:45',
		title: 'Swimming lesson',
	},
	{
		start: '2022-01-10 19:00',
		end: '2022-01-10 19:45',
		title: 'Swimming lesson',
	},
	{
		start: '2022-01-16 12:00',
		end: '2022-01-16 14:00',
		title: 'LUNCH',
		class: 'lunch',
		background: true,
	},
	{
		start: '2022-01-17 12:00',
		end: '2022-01-17 14:00',
		title: 'LUNCH',
		class: 'lunch',
		background: true,
	},
])

const { route } = useRoute()

export const useEvents = createSharedComposable(() => {
	const getEvents = () => {
		const appointments = Inertia.get(route('appointment.ajax'))
		return appointments
	}
	const setEvents = () => {}
	const createEvent = (appointment) => {
		Inertia.post(route('appointment.store'), appointment)
	}

	const updateEvent = (appointment_id) => {
		Inertia.post(route('appointment.update'), appointment_id)
	}

	const removeEvent = (appointment_id) => {
		Inertia.post(route('appointment.delete'), appointment_id)
	}
	return { events, createEvent, updateEvent, removeEvent }
})
