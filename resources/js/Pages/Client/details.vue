<template>
  <section>
    <n-grid :x-gap="12" :cols="12">
      <n-grid-item :span="4" class="bg-white shadow-lg px-4 py-5 rounded-md">
        <n-thing>
          <template #avatar>
            <n-avatar size="large" class="text-lg">{{ client.name[0] }}</n-avatar>
          </template>
          <template #header>{{ client.name }}</template>
          <template #description>{{ client.email }}</template>
          <n-space justify="center">
            <n-button class="my-4" type="info">Nova Marcação</n-button>
          </n-space>
          <n-form :model="client" ref="formRef" label-placement="top">
            <n-form-item label="Nome" path="client_name">
              <n-input placeholder="Nome" v-model:value="client.name" />
            </n-form-item>
            <n-form-item label="Email" path="client_email">
              <n-input type="email" placeholder="Email" v-model:value="client.email" />
            </n-form-item>
            <n-form-item label="Nº tlemovel" path="client_phone">
              <n-input
                type="tel"
                placeholder="Nº Telemovel"
                v-model:value="client.phone"
              />
            </n-form-item>
          </n-form>
          <template #action>
            <n-space>
              <n-button
                @click="updateClient"
                :disabled="loading"
                :loading="loading"
                type="primary"
                >Guardar Alteração</n-button
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
  client: Object,
});

const { route } = useRoute();
const loading = ref(false);
const errors = ref([]);

const updateClient = () => {
  loading.value = true;
  Inertia.post(route("client.update", props.client.id), client, {
    onSuccess: (successMessage) => {
      (loading.value = false), console.log(successMessage);
    },
    onError: (errorsMessage) => {
      errors.value = errorsMessage;
      loading.value = false;
    },
  });
};
</script>

<style></style>
