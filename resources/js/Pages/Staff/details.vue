<template>
  <section>
    <n-grid :x-gap="12" :cols="12">
      <n-grid-item :span="4" class="bg-white shadow-lg px-4 py-5 rounded-md">
        <n-thing>
          <template #avatar>
            <n-avatar size="large" class="text-lg">{{ staff.name[0] }}</n-avatar>
          </template>
          <template #header>{{ staff.name }}</template>
          <template #description>{{ staff.email }}</template>
          <n-form :model="staff" ref="formRef" label-placement="top">
            <n-form-item label="Nome" path="staff_name">
              <n-input placeholder="Nome" v-model:value="staff.name" />
            </n-form-item>
            <n-form-item label="Email" path="staff_email">
              <n-input type="email" placeholder="Email" v-model:value="staff.email" />
            </n-form-item>
            <n-form-item label="Nº tlemovel" path="staff_phone">
              <n-input
                type="phone"
                placeholder="Nº Telemovel"
                v-model:value="staff.phone"
              />
            </n-form-item>
            <n-form-item label="Servoços" path="service_duration">
              <n-select
                v-model:value="staff.services"
                :options="services"
                placeholder="Atribuir serviço ao novo membro"
                multiple
                :max-tag-count="3"
              />
            </n-form-item>
          </n-form>
          <template #action>
            <n-space>
              <n-button
                @click="updateStaff"
                :disabled="loading"
                type="primary"
                :loading="loading"
                >Guardar membro</n-button
              >
            </n-space>
          </template>
        </n-thing>
      </n-grid-item>
      <n-grid-item :span="8" class="px-4">
        <n-grid :x-gap="12" :y-gap="12" :cols="3" class="mb-6">
          <n-grid-item class="bg-white shadow-md p-4 rounded-md">
            <n-statistic label="Statistic" :value="99">
              <template #suffix>/ 100</template>
            </n-statistic>
          </n-grid-item>
          <n-grid-item class="bg-white shadow-md p-4 rounded-md">
            <n-statistic label="Active Users">1,234,123</n-statistic>
          </n-grid-item>
          <n-grid-item class="bg-white shadow-md p-4 rounded-md">
            <n-statistic label="Active Users">1,234,123</n-statistic>
          </n-grid-item>
        </n-grid>
        <div class="bg-white shadow-lg px-4 py-5 rounded-md">
          <n-tabs type="card" size="large" justify-content="center">
            <n-tab-pane name="appointment" tab="Marcações">
              <n-timeline item-placement="left">
                <n-timeline-item content="Oops" />
                <n-timeline-item
                  type="success"
                  title="Success"
                  content="success content"
                  time="2018-04-03 20:46"
                />
                <n-timeline-item
                  type="error"
                  content="Error content"
                  time="2018-04-03 20:46"
                />
                <n-timeline-item
                  type="warning"
                  title="Warning"
                  content="warning content"
                  time="2018-04-03 20:46"
                />
                <n-timeline-item
                  type="info"
                  title="Info"
                  content="info content"
                  time="2018-04-03 20:46"
                />
              </n-timeline>
            </n-tab-pane>
            <n-tab-pane name="schedule" tab="Horário">
              <n-timeline item-placement="left">
                <n-timeline-item content="Oops" />
                <n-timeline-item
                  type="success"
                  title="Success"
                  content="success content"
                  time="2018-04-03 20:46"
                />
                <n-timeline-item
                  type="error"
                  content="Error content"
                  time="2018-04-03 20:46"
                />
                <n-timeline-item
                  type="warning"
                  title="Warning"
                  content="warning content"
                  time="2018-04-03 20:46"
                />
                <n-timeline-item
                  type="info"
                  title="Info"
                  content="info content"
                  time="2018-04-03 20:46"
                />
              </n-timeline>
            </n-tab-pane>
          </n-tabs>
        </div>
      </n-grid-item>
    </n-grid>
  </section>
</template>

<script setup>
import { ref } from "vue";
import { Inertia } from "@inertiajs/inertia";
import { useRoute } from "@/composables";

const props = defineProps({
  staff: Object,
  services: Array,
});

const errors = ref([]);
const loading = ref(false);
const { route } = useRoute();

const updateStaff = () => {
  loading.value = true;
  Inertia.post(route("staff.update", props.staff.id), props.staff, {
    onSuccess: () => (loading.value = false),
    onError: (e) => {
      errors.value = e;
      loading.value = false;
    },
  });
};
</script>

<style></style>
