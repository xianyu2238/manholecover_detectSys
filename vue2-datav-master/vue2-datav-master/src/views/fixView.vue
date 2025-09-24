<template>
    <!-- 全屏容器 -->
    <IndexShipei>  <!-- 通过调用适配组件，通过插槽的方式将整个大屏传入做适配 -->
            <dv-border-box-11 title="井盖隐患展板" style="background-color: black;" class="container">
                <!-- 我这里将页面分为上中下三块，这是第一块 -->
                <div class="box1">
                    <div class="box3">
                        <fixerTab :username="username"></fixerTab>
                    </div>
                    <div class="box4">
                        <fixerTask :district="district"></fixerTask>
                    </div>
                </div>
                <!-- 第二块 -->
                <div class="box2">
                    <div style="width: 98%;height: 100%;">
                    <dv-border-box-8>
                        <detailMap :district="district"></detailMap>
                    </dv-border-box-8>
                    </div>
                </div>
               
            </dv-border-box-11>
    </IndexShipei>
</template>
<script>
import IndexShipei from "./IndexShipei.vue"
import detailMap from "@/components/detailMap.vue"
import fixerTask from "@/components/fixerTask.vue"
import fixerTab from "@/components/fixerTab.vue"
import {getArea} from "./api/user"
export default {
    data() {

        return {
           username:"",
           district:""
        }


    },
    methods: {



    },

    mounted() {

    },
    created(){
        this.username=document.cookie.split('=')[1]
        getArea({
            name:this.username
        }).then(res=>{
            this.district=res.data
        })
    },
    components: {
        // IndexData1, IndexData2, IndexData3, IndexData4, IndexData5, IndexData6, IndexData7, IndexData8, IndexData9, 
        IndexShipei,detailMap,fixerTask,fixerTab
    }
}
</script>
<style scoped>
.container{
    display: flex !important;
    flex-direction: row;
    width: 100%;
    height: 100%;
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}
.box1 {
    margin-top: 40px;
    width: 40%;
    height: 95%;
 
    float: left;
}
.box2 {
    margin-top: 55px;
    width: 60%;
    height: 94%;
    float: right;
}
.box3 {
    float: right;
    width: 98%;
    height: 20%;
}
.box4 {
    float: right;
    width: 98%;
    height: 80%;
    /* background-color: red */
}


</style>