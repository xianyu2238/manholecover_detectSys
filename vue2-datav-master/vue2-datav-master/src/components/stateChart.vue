<template>
    <div class="stateChart">
        <dv-active-ring-chart :config="config" style="width:100%;height:90%" />
    </div>
</template>
<script>


// import * as echarts from "echarts";

export default {
    data() {
        return {
            config: {
                radius:"75%",
                activeRadius:"80%",
                data: [
                    {
                        name: 'good',
                        value: 73
                    },
                    {
                        name: 'broke',
                        value: 10
                    },
                    {
                        name: 'circle',
                        value: 6
                    },
                    {
                        name: 'loss',
                        value: 9
                    },
                    {
                        name: 'uncover',
                        value: 6
                    }
                ]
            }
        }
    }

}
</script>
<style scoped>
.stateChart {
    height: 90%;
}
</style>