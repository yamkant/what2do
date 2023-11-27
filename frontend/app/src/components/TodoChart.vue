<template>
  <div>
    <GChart :type="type" :data="chart_data" :options="options" :settings="settings" />
  </div>
</template>

<script>
import { GChart } from 'vue-google-charts'

export default {
  components: {
    GChart
  },
  props: {
    chart_data: Array,
  },
  data() {
    return {
      type: 'Timeline',
      options: {
        width: "60%",
        height: 800,
        timeline: { colorByRowLabel: true },
        hAxis: {
          format: 'HH:mm', // 시간 형식 지정
        },
      },
      timeline: {
          showRowLabels: false
        },
      settings: {
        packages: ['timeline'],
      },
    }
  },
};
</script>