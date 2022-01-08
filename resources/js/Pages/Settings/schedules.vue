<template>
  <n-card>
    <n-list>
      <n-list-item v-for="week in ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']">
        <n-grid :cols="12" x-gap="12">
          <n-grid-item :span="4">
            <n-form-item :label="week" label-placement="left">
              <n-switch v-model:value="active">
                <template #checked>Aberto</template>
                <template #unchecked>Fechado</template>
              </n-switch>
            </n-form-item>
          </n-grid-item>
          <n-grid-item v-if="active" :span="8">
            <n-space>
              <n-time-picker
                v-model:value="time"
                :hours="hours"
                :minutes="15"
                format="HH:mm"
                placeholder="Tempo de início"
              />
              <n-time-picker v-model:value="time" format="HH:mm" placeholder="Tempo de fim" />
            </n-space>
          </n-grid-item>
        </n-grid>
      </n-list-item>
    </n-list>
  </n-card>
</template>
<script setup>
import { ref } from 'vue'
import { getTime, eachHourOfInterval } from 'date-fns'

const newTime = new Date()
const active = ref(false)
hours = []
const allowHours = eachHourOfInterval({
  start: newTime.setHours(8),
  end: newTime.setHours(20)
})

allowHours.foreach(hours => {
  hours.push(hours.getHours())
})
console.log(hours)
const time = ref(getTime(new Date()))
</script>

<style>
</style>