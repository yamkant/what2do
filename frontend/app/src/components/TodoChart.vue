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
        // alternatingRowStyle: false
        hAxis: {
          format: 'HH:mm', // 시간 형식 지정
          // ticks: [
          //   new Date(0, 0, 0, 0, 0, ),
          //   new Date(0, 0, 0, 6, 0, 0),
          //   new Date(0, 0, 0, 12, 0, 0),
          //   new Date(0, 0, 0, 18, 0, 0),
          // ],
          // gridlines: {
          //   count: -1, // 수평 그리드 라인 수
          //   units: {
          //     hours: {format: ['HH:mm']}
          //   }
          // }
        },
        // vAxis: {
        //   format: 'MMM dd, yyyy', // 날짜 형식 지정
        // },
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