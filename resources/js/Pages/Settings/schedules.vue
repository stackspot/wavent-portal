<template>
  <n-descriptions bordered>
    <n-descriptions-item
      v-for="week in ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']"
      :key="week"
    >
      <template #label>
        <n-form-item :label="week" label-placement="left">
          <n-switch v-model:value="active">
            <template #checked>Aberto</template>
            <template #unchecked>Fechado</template>
          </n-switch>
        </n-form-item>
      </template>
      <n-space v-if="active">
        <n-time-picker
          v-model:value="time"
          :hours="schedule"
          format="HH:mm"
          placeholder="Tempo de início"
        />
        <n-time-picker v-model:value="time" format="HH:mm" placeholder="Tempo de fim" />
      </n-space>
    </n-descriptions-item>
  </n-descriptions>
</template>
<script setup>
import { ref } from 'vue'
import { getTime, eachHourOfInterval } from 'date-fns'

const newTime = new Date()
const active = ref(false)

const schedule = []

const allowHours = eachHourOfInterval({
  start: newTime.setHours(8),
  end: newTime.setHours(20)
})

allowHours.forEach(hours => {
  schedule.push(hours.getHours())
})

const time = ref(getTime(new Date()))
</script>

<style>
</style>