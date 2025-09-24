<template>
    <div style="padding: 3%;">
        <div id="map" style="height:950px; width:100%"></div> 
    </div>
</template>
<script>
import BMap from 'BMap'
import {getMap,getPoints} from "../views/api/fixer"
export default {
    methods: {
        //地图初始化
        createMap() {
            // 创建Map实例
            this.map = new BMap.Map("map");
            let point = new BMap.Point(this.longitude, this.latitude)
            // 设定地图的中心点和坐标并将地图显示在地图容器中 
            this.map.centerAndZoom(point, 15)
            //添加地图类型控件
            this.map.addControl(
                new BMap.MapTypeControl({
                    mapTypes: [this.BMAP_NORMAL_MAP, this.BMAP_HYBRID_MAP],
                })
            );
            // 设置午夜主题
            this.map.setMapStyle({style:'midnight'});
            this.map.setCurrentCity("杭州市");  // 设置地图显示的城市 此项是必须设置的
            this.map.enableScrollWheelZoom(true); // 开启鼠标滚轮缩放
            // 添加标记点
            this.addMarkers()
        },
        // 重新加载地图数据
        reloadMap() {
            if (this.map) {
                this.map.clearOverlays();
                // 重新获取点位数据
                getPoints({
                    district: this.district
                }).then(res => {
                    if (res.data && res.data.length > 0) {
                        this.virData = res.data.map(item => ({
                            x: item.longitude,
                            y: item.latitude,
                            id: item.id,
                            state: item.state,
                            pic: item.pic
                        }))
                        this.addMarkers()
                    }
                })
            }
        },
        mounted() {
        // 等待百度地图API加载完成
        window.BMap = window.BMap || {};
        window.BMap.MapTypeId = window.BMap.MapTypeId || {};
        this.BMAP_NORMAL_MAP = window.BMap.MapTypeId.NORMAL;
        this.BMAP_HYBRID_MAP = window.BMap.MapTypeId.HYBRID;
    },
        
        // 添加标记点
        addMarkers() {
            this.map.clearOverlays();
            if (this.virData && this.virData.length >0 ){
                this.virData.forEach((item) => {
                    let point = new BMap.Point(item.x, item.y);
                    let icon = new BMap.Icon(require('@/assets/定位.png'), new BMap.Size(32, 32), {
                        imageSize: new BMap.Size(32, 32),
                        anchor: new BMap.Size(16, 32)
                    });
                    let marker = new BMap.Marker(point, {icon: icon});
                    let opts = {
                        width: 200,
                        height: 250,
                    }
                    let message = `
                        <div style="margin-bottom: 10px; margin-top: 10px;">
                            <span>设备ID：</span>
                            <span>${item.id}</span>
                        </div>
                        <div style="margin-bottom: 10px">
                            <span>设备状态：</span>
                            <span>${item.state}</span>
                        </div>
                        <div style="margin-bottom: 10px">
                            <span>设备图片：</span>
                            <div style="width: 180px; height: 150px; background: #f5f5f5; display: flex; align-items: center; justify-content: center;">
                                <img src="data:image/jpeg;base64,${item.pic || ''}" 
                                    onerror="this.style.display='none';this.parentElement.innerHTML='<span style=\\'color:#999\\'>无图片</span>'"
                                    style="max-width: 100%; max-height: 100%;" />`
                    
                    let infoWindow = new BMap.InfoWindow(message, opts);
                    this.map.addOverlay(marker);
                    
                    marker.addEventListener('click', () => {
                        this.map.openInfoWindow(infoWindow, point);
                    });
                });
            }
        }
    },

    props:['district'],
	name: 'baiduMap',
    data() {
        return {
            map: '', //地图实例
            virData: [], // 坐标数据 [{longitude: 116.958471, latitude: 39.785079, title: '标题'...}]
            BMAP_NORMAL_MAP: null,
            BMAP_HYBRID_MAP: null,
            longitude:0,
            latitude:0
        }
    },
    watch: {
        district: {
            immediate: true,
            handler(newVal) {
                if (newVal) {
                    // 获取地图中心点
                    getMap({
                        district: newVal
                    }).then(res => {
                        this.longitude = res.data.longitude
                        this.latitude = res.data.latitude
                        if (!this.map) {
                            this.createMap()
                        } else {
                            let point = new BMap.Point(this.longitude, this.latitude)
                            this.map.centerAndZoom(point, 15)
                            this.addMarkers()
                        }
                    })
                    
                    // 获取点位数据
                    getPoints({
                        district: newVal
                    }).then(res => {
                        // console.log(res)
                        if (res.data && res.data.length > 0) {
                            this.virData = res.data.map(item => ({
                                x: item.longitude,
                                y: item.latitude,
                                id: item.id,
                                state: item.state,
                                pic: item.pic
                            }))
                            this.addMarkers()
                        }
                    })
                }
            }
        }
    },
    
}
</script>
<style lang="scss" scoped>
.box-card {
        width: 100%;
        height: 100%;
        margin-bottom: 20px;
        margin-top: 10px;
    }
</style>