<template>
  <FullCalendar class="z-1" :options="calendarOptions" ref="calendar">
    <template v-slot:eventContent="arg">
      <div class="flex flex-col gap-2 p-1">
        <b>{{ arg.timeText }}</b>
        <i>{{ arg.event.title }}</i>
      </div>
    </template>
  </FullCalendar>
</template>

<script setup>
import { ref, reactive } from "vue";
import '@fullcalendar/core/vdom' // solve problem with Vite
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'
import ptLocale from '@fullcalendar/core/locales/pt';
import { useEvents } from "@/composables"

let emit = defineEmits(['createEvent'])
let events = ref([
  {
    start: '2022-01-09 10:35',
    end: '2022-01-09 12:30',
    title: 'Doctor appointment',
  },
  {
    start: '2022-01-08 18:30',
    end: '2022-01-08 19:15',
    title: 'Dentist appointment',
  },
  {
    start: '2022-01-03 18:30',
    end: '2022-01-03 19:30',
    title: 'Crossfit',
  },
  {
    start: '2022-01-04 12:00',
    end: '2022-01-04 13:00',
    title: 'Brunch with Jane',
  },
  {
    start: '2022-01-05 19:00',
    end: '2022-01-05 19:45',
    title: 'Swimming lesson',
  },
  {
    start: '2022-01-07 19:00',
    end: '2022-01-07 19:45',
    title: 'Swimming lesson',
  },
  {
    start: '2022-01-06 12:00',
    end: '2022-01-06 14:00',
    title: 'LUNCH',
    class: 'lunch',
    background: true,
  },
  {
    start: '2022-01-07 12:00',
    end: '2022-01-07 14:00',
    title: 'LUNCH',
    class: 'lunch',
    background: true,
  },
])


let calendarOptions = reactive({
  plugins: [
    dayGridPlugin,
    timeGridPlugin,
    interactionPlugin // needed for dateClick
  ],
  customButtons: {
    createEvent: {
      text: 'Criar Marcação',
      click: function () {
        emit('createEvent')
      }
    },
  },
  headerToolbar: {
    left: 'prev,next today',
    center: 'title',
    right: 'createEvent timeGridWeek,timeGridDay'
  },
  locale: ptLocale,
  initialView: 'timeGridWeek',
  initialEvents: events.value, // alternatively, use the `events` setting to fetch from a feed
  editable: true,
  selectable: true,
  selectMirror: true,
  dayMaxEvents: true,
  weekends: true,
  /* select: handleDateSelect,
  eventClick: handleEventClick,
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
  businessHours: true,
  eventColor: "#ffa101",
})

</script>

<style scoped>
</style>