<template>
  <div v-if="!schedulesRef">
    <n-list class="mb-4" bordered>
      <n-list-item v-for="schedule in schedules" :key="schedule.name">
        <n-grid x-gap="12" :cols="2">
          <n-gi>
            <n-form-item :label="schedule.name" label-placement="left">
              <n-switch v-model:value="schedule.is_working">
                <template #checked>Aberto</template>
                <template #unchecked>Fechado</template>
              </n-switch>
            </n-form-item>
          </n-gi>
          <n-gi>
            <n-space>
              <n-time-picker
                v-model:value="schedule.start_time"
                :disabled="!schedule.is_working"
                :minutes="10"
                :hours="hoursInterval"
                format="HH:mm"
                placeholder="Tempo de início"
              />
              <n-time-picker
                v-model:value="schedule.finish_time"
                :disabled="!schedule.is_working"
                :minutes="10"
                :hours="hoursInterval"
                format="HH:mm"
                placeholder="Tempo de fim"
              />
            </n-space>
          </n-gi>
        </n-grid>
      </n-list-item>
    </n-list>

    <n-button type="primary" @click="saveSchedule">Guardar</n-button>
  </div>
  <div v-else>
    <n-list class="mb-4" bordered>
      <n-list-item v-for="schedule in schedulesRef" :key="schedule.name">
        <n-grid x-gap="12" :cols="2">
          <n-gi>
            <n-form-item :label="schedule.name" label-placement="left">
              <n-switch v-model:value="schedule.is_working">
                <template #checked>Aberto</template>
                <template #unchecked>Fechado</template>
              </n-switch>
            </n-form-item>
          </n-gi>
          <n-gi>
            <n-space>
              <n-time-picker
                v-model:value="schedule.start_time"
                :disabled="!schedule.is_working"
                :minutes="10"
                :hours="hoursInterval"
                format="HH:mm"
                placeholder="Tempo de início"
              />
              <n-time-picker
                v-model:value="schedule.finish_time"
                :disabled="!schedule.is_working"
                :minutes="10"
                :hours="hoursInterval"
                format="HH:mm"
                placeholder="Tempo de fim"
              />
            </n-space>
          </n-gi>
        </n-grid>
      </n-list-item>
    </n-list>
    <n-button type="primary" @click="updateSchedule">Guardar</n-button>
  </div>
</template>
<script setup>
import { onBeforeMount, ref } from 'vue'
import { getTime, eachHourOfInterval, toDate, parseISO } from 'date-fns'
import { Inertia } from '@inertiajs/inertia'
import { useRoute, useUser } from '@/composables'
import axios from 'axios'

const newTime = new Date()
const { route } = useRoute()
const { getUser } = useUser()
const currentUser = getUser()

const start = getTime(newTime.setHours(8, 0, 0, 0))
const end = getTime(newTime.setHours(18, 0, 0, 0))

const hoursInterval = []
const schedulesRef = ref(null)
const schedules = ref([
  {
    name: "Segunda",
    start_time: null,
    finish_time: null,
    is_working: true
  },
  {
    name: "Terça",
    start_time: null,
    finish_time: null,
    is_working: true
  },
  {
    name: "Quarta",
    start_time: null,
    finish_time: null,
    is_working: true
  },
  {
    name: "Quinta",
    start_time: null,
    finish_time: null,
    is_working: true
  },
  {
    name: "Sexta",
    start_time: null,
    finish_time: null,
    is_working: true
  }
])

const getSchedules = async () => {
  const response = await axios.get(route('schedule.index'))
  schedulesRef.value = response.data.schedules.map((schedule) => {
    return {
      id: schedule.id,
      name: schedule.name,
      start_time: getTime(parseISO(schedule.start_time)),
      finish_time: getTime(parseISO(schedule.finish_time)),
      is_working: schedule.is_working,
      account_id: schedule.account_id
    }
  })
}
const saveSchedule = async () => {
  const data = {
    "schedules": schedules.value.map((schedule) => {
      return {
        name: schedule.name,
        start_time: toDate(schedule.start_time),
        finish_time: toDate(schedule.finish_time),
        is_working: schedule.is_working,
        account_id: currentUser.account_id
      }
    })
  }
  Inertia.post(route('schedule.store'), data, {
    onError: (e) => console.log('error', e),
    onSuccess: () => getSchedules()
  })
}
const updateSchedule = async () => {
  const data = {
    "schedules": schedulesRef.value.map((schedule) => {
      return {
        id: schedule.id,
        name: schedule.name,
        start_time: toDate(schedule.start_time),
        finish_time: toDate(schedule.finish_time),
        is_working: schedule.is_working,
        account_id: schedule.account_id
      }
    })
  }
  Inertia.post(route('schedule.update'), data, {
    onError: (e) => console.log('error', e),
    onSuccess: () => getSchedules()
  })
  console.log(schedulesRef.value)
}


const allowHours = eachHourOfInterval({
  start: newTime.setHours(8),
  end: newTime.setHours(23)
})

allowHours.forEach(hours => {
  hoursInterval.push(hours.getHours())
})

onBeforeMount(() => getSchedules())
</script>

<style>
</style>