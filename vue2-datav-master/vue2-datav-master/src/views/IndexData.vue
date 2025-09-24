<template>
    <!-- 全屏容器 -->
    <IndexShipei>  <!-- 通过调用适配组件，通过插槽的方式将整个大屏传入做适配 -->
            <dv-border-box-11 title="井盖隐患展板" style="background-color: black;" class="container">
                <!-- 我这里将页面分为上中下三块，这是第一块 -->
                <div class="box">
                    <div class="box1" style="padding-top: 40px;">
                        <dv-border-box-10>
                            <weekError></weekError>
                            <div class="header">周内异常统计</div>
                        </dv-border-box-10>
                    </div>
                    <div class="box2" style="padding-top: 60px;">
                        <dv-border-box-10>
                            <fixerTab :username="username"></fixerTab>
                        </dv-border-box-10>
                    </div>
                    <div class="box1" style="padding-top: 40px;">
                        <dv-border-box-10>
                            <personList></personList>
                        </dv-border-box-10>
                    </div> 
                </div>
                <!-- 第二块 -->
                <div class="box">
        
                    <div class="box1">
                        <dv-border-box-10>
                            <errorArea></errorArea>
                            <div class="header">异常区域统计</div>
                        </dv-border-box-10>
                    </div>
                    <div class="box2" >
                            <hzMap style="position: relative;"></hzMap>
                        <!-- <div style="background-color: aqua;position: relative;height: 500px;">11</div> -->
                        
                    </div>
                    <div class="box1">
                        <dv-border-box-10>
                            <stateChart></stateChart>
                            <div class="header">井盖状态占比</div>
                        </dv-border-box-10>
                    </div>
                </div>
                <!-- 第三块 -->
                <div class="box">
              
                    <div class="box1">
                        <dv-border-box-10>
                            <h1 class="title">异常状态统计</h1>
                            <erroItem style="height: 75%;"></erroItem>
                        </dv-border-box-10>
                    </div>
                    <div class="box1">
                        <dv-border-box-10>
                            <taskItem style="height: 75%;"></taskItem>
                        </dv-border-box-10>
                    </div>
                </div>
            </dv-border-box-11>
    </IndexShipei>
</template>
<script>
import IndexShipei from "./IndexShipei.vue"
import errorArea from "@/components/errorArea.vue";
import weekError from "@/components/weekError.vue";
import erroItem from "@/components/erroItem.vue";
import personList from "@/components/personList.vue";
import stateChart from "@/components/stateChart.vue";
import taskItem from "@/components/taskItem.vue";
import hzMap from "@/components/hzMap.vue"
import fixerTab from "@/components/fixerTab.vue";

export default {
    data() {

        return {
            username: "张三"
        }


    },
    created(){
        this.username=document.cookie.split('=')[1]
    },

    mounted() {

    },
    components: {
        // IndexData1, IndexData2, IndexData3, IndexData4, IndexData5, IndexData6, IndexData7, IndexData8, IndexData9, 
        IndexShipei,errorArea,weekError,erroItem,personList,stateChart,taskItem,hzMap,fixerTab
    }
}
</script>
<style scoped>
.container{
    display: flex !important;
    flex-direction: row;
}
.box1 {
    /* background-color: aqua; */
    width: 27%;
    height: 340px;
}
.box2{
    /* background-color: blue; */
    width: 45%;
    height: 300px;
}
.box {
    /* background-color: blueviolet; */
    display: flex;
    justify-content: space-between;
    width: 98%;
    margin: auto;
}
.header{
    text-align: center;
    color: aliceblue;
    font-size: 25px;
    margin-top: -20px;
}
.title{
    color: aliceblue;
    text-align:center;
}
</style>