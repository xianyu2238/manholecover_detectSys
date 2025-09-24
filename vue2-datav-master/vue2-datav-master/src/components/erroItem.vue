<template>
    <div class="erroItem">
        <dv-scroll-board :config="config"  />
    </div>
</template>
<script>


// import * as echarts from "echarts";

export default {
    data() {
        return {
            config: {
                header: ['区域', '编号', '异常状态'],
                data: [
                    ['西湖区', '0001', 'broke'],
                    ['西湖区', '0002', 'circle'],
                    ['西湖区', '0013', 'loss'],
                    ['西湖区', '0066', 'broke'],
                    ['临平区', '6001', 'broke'],
                    ['临平区', '6022', 'broke'],
                    ['临平区', '6024', 'loss'],
                    ['临平区', '6022', 'loss'],
                    ['钱塘区', '1004', 'loss'],
                    ['钱塘区', '1034', 'broke'],
                ],
                index: true,
                columnWidth: [50],
                align: ['center'],
                carousel: 'page'
            }
        }
    }

}
</script>
<style scoped>
.erroItem {
    height: 90%;
    padding: 5%;
}
</style>