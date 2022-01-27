import { createSharedComposable } from '@vueuse/core'
import { reactive, computed } from 'vue'
import axios from 'axios'
import { useRoute } from './route'

/* let events = reactive([
	{
		start: '2022-01-25 10:35',
		end: '2022-01-25 12:30',
		title: 'Doctor appointment',
	},
	{
		start: '2022-01-25 18:30',
		end: '2022-01-25 19:15',
		title: 'Dentist appointment',
	},
	{
		start: '2022-01-27 18:30',
		end: '2022-01-27 19:30',
		title: 'Crossfit',
	},
	{
		start: '2022-01-26 12:00',
		end: '2022-01-26 13:00',
		title: 'Brunch with Jane',
	},
	{
		start: '2022-01-28 19:00',
		end: '2022-01-28 19:45',
		title: 'Swimming lesson',
	},
	{
		start: '2022-01-29 19:00',
		end: '2022-01-29 19:45',
		title: 'Swimming lesson',
	},
	{
		start: '2022-01-29 12:00',
		end: '2022-01-29 14:00',
		title: 'LUNCH',
		class: 'lunch',
		background: true,
	},
	{
		start: '2022-01-28 12:00',
		end: '2022-01-28 14:00',
		title: 'LUNCH',
		class: 'lunch',
		background: true,
	},
]) */

const { route } = useRoute()

export const useEvents = createSharedComposable(() => {
	const appointments = reactive([])

	const getEvents = async () => {
		const response = await axios.get(route('appointment.api'))
		appointments = response.data.appointments
	}

	const events = computed(() => {
		return [
			...appointments.map((appointment) => {
				return {
					id: appointment.id,
					title: appointment?.client.name,
					start: appointment?.start_time,
					end: appointment?.finish_time,
					price: appointment?.price,
					staff: appointment?.staff,
					client: appointment?.client,
					services: appointment.services,
				}
			}),
		]
	})

	const createEvent = (appointment) => {
		Inertia.post(route('appointment.store'), appointment)
	}

	const updateEvent = (appointment_id) => {
		Inertia.post(route('appointment.update'), appointment_id)
	}

	const removeEvent = (appointment_id) => {
		Inertia.post(route('appointment.delete'), appointment_id)
	}

	return { events, getEvents, createEvent, updateEvent, removeEvent }
})
