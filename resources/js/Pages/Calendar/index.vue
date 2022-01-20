<template>
  <section ref="container">
    <n-drawer v-model:show="showEventDrawer" :width="320" :mask-closable="false">
      <n-drawer-content title="Criar Marcação" closable :native-scrollbar="false">
        <n-form :model="form" :label-width="80" ref="formRef">
          <n-form-item label="Serviço" path="service">
            <n-select v-model:value="form.services" multiple tag clearable :options="services" />
          </n-form-item>
          <n-form-item label="Cliente" path="client">
            <n-select v-model:value="form.client_id" clearable :options="options" />
          </n-form-item>
          <!-- <div v-show="newClient">
            <n-form-item label="Nome do Cliente" path="client.name">
              <n-input v-model:value="form.client.name" placeholder="Nome do Cliente" />
            </n-form-item>
            <n-form-item label="Email do Cliente" path="client.email">
              <n-input v-model:value="form.client.email" placeholder="Email do Cliente" />
            </n-form-item>
            <n-form-item label="Nº Telemovel do Cliente" path="client.phone">
              <n-input v-model:value="form.client.phone" placeholder="Nº Telemovel do Cliente" />
            </n-form-item>
          </div>-->
          <n-form-item label="Barbeiro" path="staff">
            <n-select v-model:value="form.staff" clearable :options="staffs" />
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
          <!-- <n-form-item label="Data e Hora final" path="end_time">
            <n-date-picker
              v-model:value="form.start_time"
              format="yyyy-MM-dd HH:mm"
              type="datetime"
              clearable
              placeholder="Data e Hora final"
            />
          </n-form-item>-->
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
    <FullCalendar class="z-1" :options="calendarOptions" ref="calendarApp">
      <template v-slot:eventContent="arg">
        <n-popover class="max-w-xs">
          <template #trigger>
            <span class="p-1 max-h-6">
              <n-scrollbar>
                <div class="flex flex-col">
                  <span class="text-sm mb-1">{{ arg.event.title }}</span>
                  <span class="text-xs">{{ arg.timeText }}</span>
                </div>
              </n-scrollbar>
            </span>
          </template>
          <n-thing>
            <template #avatar>
              <n-avatar>J</n-avatar>
            </template>
            <template #header>{{ arg.event.title }}</template>
            <template #description>{{ arg.timeText }}</template>
            <template #footer>Footer</template>
            <template #action>
              <n-space>
                <n-button size="small">1$</n-button>
              </n-space>
            </template>
          </n-thing>
        </n-popover>
      </template>
    </FullCalendar>
  </section>
</template>

<script setup>
import { ref, reactive } from "vue";
import { useForm } from '@inertiajs/inertia-vue3'
import { getTime, toDate } from 'date-fns'
import '@fullcalendar/core/vdom' // solve problem with Vite
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'
import ptLocale from '@fullcalendar/core/locales/pt';
import { useEvents, useRoute } from "@/composables"
import { Icon } from '@/components'


let { events } = useEvents()
const { route } = useRoute()

const props = defineProps({
  services: Array,
  staffs: Array
})

const calendarApp = ref()
const showEventDrawer = ref(false)
const newClient = ref(false)
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

const options = ref([
  {
    label: 'Drive My Car',
    value: 'song1'
  },
  {
    label: 'Norwegian Wood',
    value: 'song2'
  },
  {
    label: "You Won't See",
    value: 'song3',
    disabled: true
  }])


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
  initialEvents: events, // alternatively, use the `events` setting to fetch from a feed
  editable: true,
  selectable: true,
  selectMirror: true,
  dayMaxEvents: true,
  weekends: true,
  select: onSelectDate,
  /*eventClick: handleEventClick,
  eventsSet: handleEvents, */
  /* you can update a remote database when these fire:
  eventAdd:
  eventChange:
  eventRemove:
  */
  height: 'auto', // will activate stickyHeaderDates automatically!
  scrollTime: '08:00',
  slotMinTime: '08:00:00',
  slotMaxTime: '20:30:00',
  slotDuration: '00:15:00',
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


</script>

<style scoped>
</style>
