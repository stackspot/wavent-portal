<template>
  <section ref="container">
    <n-drawer v-model:show="showEventDrawer" :width="320" :mask-closable="false">
      <n-drawer-content title="Criar Marcação" closable :native-scrollbar="false">
        <n-form :model="form" :label-width="80" ref="formRef">
          <n-tabs type="segment">
            <n-tab-pane name="detalhes" tab="Informação">
              <n-form-item label="Serviço" path="service">
                <n-select
                  v-model:value="form.services"
                  placeholder="Selecionar Serviços existente"
                  multiple
                  tag
                  clearable
                  :options="services"
                />
              </n-form-item>
              <n-form-item label="Cliente" path="client">
                <n-select
                  v-model:value="form.client_id"
                  placeholder="Selecionar Cliente existente"
                  clearable
                  :options="clients"
                />
              </n-form-item>
              <n-form-item label="Barbeiro" path="staff">
                <n-select
                  v-model:value="form.staff"
                  placeholder="Selecionar Funcionário"
                  clearable
                  :options="staffs"
                />
              </n-form-item>
              <n-form-item label="Data e Hora inicial" path="start_time">
                <n-date-picker
                  v-model:value="form.start_time"
                  format="yyyy-MM-dd HH:mm"
                  type="datetime"
                  clearable
                  placeholder="Data e Hora inicial"
                />
              </n-form-item>
              <n-form-item label="Data e Hora final" path="end_time">
                <n-date-picker
                  v-model:value="form.finish_time"
                  format="yyyy-MM-dd HH:mm"
                  type="datetime"
                  clearable
                  placeholder="Data e Hora final"
                />
              </n-form-item>
            </n-tab-pane>
            <n-tab-pane name="clients" tab="Novo Cliente">
              <n-form-item label="Nome do Cliente" path="client.name">
                <n-input v-model:value="form.client.name" placeholder="Nome do Cliente" />
              </n-form-item>
              <n-form-item label="Email do Cliente" path="client.email">
                <n-input v-model:value="form.client.email" placeholder="Email do Cliente" />
              </n-form-item>
              <n-form-item label="Nº Telemovel do Cliente" path="client.phone">
                <n-input v-model:value="form.client.phone" placeholder="Nº Telemovel do Cliente" />
              </n-form-item>
            </n-tab-pane>
          </n-tabs>
          <n-form-item>
            <n-space>
              <n-button
                type="primary"
                @click="onCreateEvent"
                :disabled="form.processing"
                :loading="form.precessing"
              >Criar Marcação</n-button>
              <n-button @click="showEventDrawer = false">Cancelar</n-button>
            </n-space>
          </n-form-item>
        </n-form>
      </n-drawer-content>
    </n-drawer>
    <div class="wavent-calendar-wrapper shadow-lg shadow-light-100 px-2">
      <FullCalendar class="z-1" :options="calendarOptions" id="calendarApp">
        <template v-slot:eventContent="arg">
          <span class="p-1 max-h-6">
            <n-scrollbar>
              <div class="flex flex-col">
                <span class="text-sm mb-1">{{ arg.event.title }}</span>
                <span class="text-xs">{{ arg.timeText }}</span>
              </div>
            </n-scrollbar>
          </span>
        </template>
      </FullCalendar>
    </div>
    <n-drawer v-model:show="showEventSelectedDrawer" :width="320">
      <n-drawer-content>
        <n-thing>
          <template #avatar>
            <n-avatar class="bg-blue-300 text-lg">{{ eventSelected.extendedProps.client?.name[0] }}</n-avatar>
          </template>
          <template #header>{{ eventSelected.extendedProps.client.name }}</template>
          <template #description>
            <n-time :time="eventSelected.start" format="hh:mm" />
            <span>-</span>
            <n-time :time="eventSelected.end" format="hh:mm" />
          </template>
          <n-descriptions label-placement="top" :column="1">
            <n-descriptions-item label="Cliente">
              <div class="flex flex-col gap-2">
                <span>Nome: {{ eventSelected.extendedProps.client.name }}</span>
                <span>Email: {{ eventSelected.extendedProps.client.email }}</span>
                <span>Nº Telemovel: {{ eventSelected.extendedProps.client.phone }}</span>
              </div>
            </n-descriptions-item>
            <n-descriptions-item label="Serviços">
              <div class="flex flex-col gap-2">
                <span
                  v-for="service in eventSelected.extendedProps.services"
                  :key="service.id"
                >{{ service.name }}</span>
              </div>
            </n-descriptions-item>
            <n-descriptions-item label="Status">
              <n-tag type="success" round>Pendente</n-tag>
            </n-descriptions-item>
            <n-descriptions-item label="Funcionário">{{ eventSelected.extendedProps.staff.name }}</n-descriptions-item>
          </n-descriptions>
          <template #footer></template>
          <template #action>
            <n-space>
              <n-button size="small" type="primary">Confirmar</n-button>
            </n-space>
          </template>
        </n-thing>
      </n-drawer-content>
    </n-drawer>
  </section>
</template>

<script setup>
import { ref, reactive, computed, onBeforeMount, watch } from "vue";
import { useForm } from '@inertiajs/inertia-vue3'
import { getTime, toDate, format } from 'date-fns'
import '@fullcalendar/core/vdom' // solve problem with Vite
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'
import ptLocale from '@fullcalendar/core/locales/pt';
import { useEvents, useRoute } from "@/composables"
import axios from 'axios'

//let { events, getEvents } = useEvents()
const { route } = useRoute()

const eventSelected = ref(null)
const showEventSelectedDrawer = ref(false)
const showEventDrawer = ref(false)
const appointments = ref([])

const props = defineProps({
  services: Array,
  staffs: Array,
  clients: Array,
  appointments: Array,
})

const form = useForm({
  services: null,
  staff: null,
  client_id: null,
  client: {
    name: null,
    email: null,
    phone: null
  },
  start_time: null,
  finish_time: null,
})



/* 
const getEvents = async () => {
  const response = await axios.get(route('appointment.api'))
  console.log(response.data)
  appointments.value = response.data.appointments
  console.log(appointments.value)
} */

const events = computed(() => {
  return [
    ...props.appointments.map((appointment) => {
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

const onEventClick = (arg) => {
  eventSelected.value = arg.event
  showEventSelectedDrawer.value = true
}
const onSelectDate = (arg) => {
  const cal = arg.view.calendar
  cal.unselect()
  form.start_time = getTime(arg.start)
  form.finish_time = getTime(arg.end)
  showEventDrawer.value = true
}

let calendarOptions = reactive({
  plugins: [
    dayGridPlugin,
    timeGridPlugin,
    interactionPlugin // needed for dateClick
  ],
  headerToolbar: {
    left: 'prev,next today',
    center: 'title',
    right: 'timeGridWeek,timeGridDay'
  },
  locale: ptLocale,
  initialView: 'timeGridWeek',
  initialEvents: events.value, // alternatively, use the `events` setting to fetch from a feed
  editable: true,
  selectable: true,
  selectMirror: true,
  dayMaxEvents: true,
  weekends: true,
  select: onSelectDate,
  eventClick: onEventClick,
  /* eventsSet: handleEvents, */
  /* you can update a remote database when these fire:
  eventAdd:
  eventChange:
  eventRemove:
  */
  height: 'auto', // will activate stickyHeaderDates automatically!
  slotMinTime: '06:00:00',
  slotDuration: '00:15:00',
  slotLabelInterval: "01:00",
  nowIndicator: true,
})

const onCreateEvent = async () => {
  form.transform((data) => ({
    services: data.services,
    staff: data.staff,
    client_id: data.client_id,
    client_name: data.client.name,
    client_email: data.client.email,
    client_phone: data.client.phone,
    start_time: toDate(data.start_time),
    finish_time: toDate(data.finish_time)
  })).post(route('appointment.store'), {
    onSuccess: () => {
      showEventDrawer.value = false
    }
  })
}
/* 
onBeforeMount(() => getEvents())

watch(appointments.value, () => {
  calendarOptions.events = events.value
}) */
</script>

<style scoped>
</style>
