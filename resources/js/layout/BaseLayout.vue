<template>
  <provider>
    <slot />
  </provider>
</template>

<script setup>
import { Provider } from '@/components'
</script>
<script>
import { defineComponent, watch } from 'vue'
import { useMessage } from 'naive-ui'
import { usePage } from '@inertiajs/inertia-vue3'
import _ from 'lodash'


export default defineComponent({
  components: { Provider },
  setup () {

    const message = useMessage()
    const page = usePage()
    watch(() => _.cloneDeep(page.props.value.success), (nvl, ovl) => {
      const showSuccess = true && page.props.value.success
      if (nvl && showSuccess) {
        message.success(page.props.value.success)
      }
    })
  }
})

</script>

<style>
</style>