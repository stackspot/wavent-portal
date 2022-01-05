<template>
  <FullCalendar class="demo-app-calendar" :options="calendarOptions" ref="calendar">
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
//import useEvent from "@/composables/useEvents.js"

let emit = defineEmits(['createEvent'])

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
  initialEvents: [], // alternatively, use the `events` setting to fetch from a feed
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
  slotDuration: '00:30:00',
  nowIndicator: true,
  businessHours: true,
  eventColor: "#001280",
})

</script>

<style scoped>
</style>