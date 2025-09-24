<template>
    <div id="weekError" style="height: 90%;"></div>
</template>
<script>
import * as echarts from "echarts"
export default {
    mounted() {
        this.drawchart()
    },
    methods: {
        drawchart() {
            var chartDom = document.getElementById('weekError');
            var myChart = echarts.init(chartDom);
            var option = {
                xAxis: {
                    type: 'category',
                    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                        data: [3, 6, 9, 12, 5, 18, 4],
                        type: 'line'
                    }
                ]
            };
            myChart.setOption(option);
        }
    },
    data() {
        return{
            option:{}
        }
    }
}
</script>