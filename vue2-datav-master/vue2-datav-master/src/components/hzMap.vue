<template>
  <dv-border-box-9 style="height: 610px;">
    <div class="hzMap" v-if="!showDetail">
      <div class="search-box">
        <el-input
          v-model="searchDistrict"
          placeholder="请输入区域名称"
          class="search-input"
          @keyup.enter.native="handleSearch"
        ></el-input>
        <el-button type="primary" @click="handleSearch">查询</el-button>
      </div>
      <div ref="chartsDOM" class="map-container"></div>
    </div>
    <div v-else class="detail-container">
      <el-button type="primary" class="back-btn" @click="handleBack">返回</el-button>
      <detail-map :district="selectedDistrict" class="detail-map" @reload-map="handleReloadMap"></detail-map>
    </div>
  </dv-border-box-9>
</template>
<script>
import * as echarts from "echarts";
import getMap from "@/views/api/getmap.js"
import DetailMap from './detailMap.vue'

export default {
  components: {
    DetailMap
  },
  data() {
    return {
      searchDistrict: '',
      selectedDistrict: '',
      showDetail: false,
      myChart: null
    }
  },
  mounted() {
    this.initMap();
  },
  methods: {
    initMap() {
      // 初始化统计图对象
      this.myChart = echarts.init(this.$refs["chartsDOM"]);
      // 显示 loading 动画
      this.myChart.showLoading();
      // 再得到数据的基础上，进行地图绘制
      getMap.then(res => {
        // 得到结果后，关闭动画
        this.myChart.hideLoading();
        // 注册地图(数据放在axios返回对象的data中哦)
        echarts.registerMap('hz', res.data);
        
        // 模拟数据，实际项目中应该从后端获取
        const areaData = [
          { name: '西湖区', value: { circle: 1, broke: 2, loss: 3, good: 4, uncover: 5 } },
          { name: '上城区', value: { circle: 1, broke: 0, loss: 2, good: 8, uncover: 0 } },
          { name: '下城区', value: { circle: 3, broke: 2, loss: 1, good: 5, uncover: 1 } },
          { name: '江干区', value: { circle: 1, broke: 3, loss: 2, good: 4, uncover: 3 } },
          { name: '拱墅区', value: { circle: 2, broke: 1, loss: 3, good: 3, uncover: 4 } },
          { name: '滨江区', value: { circle: 3, broke: 2, loss: 1, good: 5, uncover: 2 } },
          { name: '萧山区', value: { circle: 4, broke: 1, loss: 2, good: 3, uncover: 3 } },
          { name: '余杭区', value: { circle: 2, broke: 3, loss: 1, good: 4, uncover: 2 } }
        ];

        var option = {
          backgroundColor: '#1a1a1a',
          tooltip: {
            trigger: 'item',
            formatter: function(params) {
              const data = areaData.find(item => item.name === params.name);
              if (!data) return params.name;
              
              return `
                <div style="font-size: 14px; font-weight: bold; margin-bottom: 8px;">${params.name}</div>
                <div style="display: flex; flex-direction: column; gap: 4px;">
                  <div style="display: flex; justify-content: space-between;">
                    <span style="color: #fff;">边缘残缺井盖：</span>
                    <span style="color: #fff; margin-left: 20px;">${data.value.circle}</span>
                  </div>
                  <div style="display: flex; justify-content: space-between;">
                    <span style="color: #fff;">破损井盖：</span>
                    <span style="color: #fff; margin-left: 20px;">${data.value.broke}</span>
                  </div>
                  <div style="display: flex; justify-content: space-between;">
                    <span style="color: #fff;">丢失井盖：</span>
                    <span style="color: #fff; margin-left: 20px;">${data.value.loss}</span>
                  </div>
                  <div style="display: flex; justify-content: space-between;">
                    <span style="color: #fff;">完好井盖：</span>
                    <span style="color: #fff; margin-left: 20px;">${data.value.good}</span>
                  </div>
                  <div style="display: flex; justify-content: space-between;">
                    <span style="color: #fff;">未覆盖井盖：</span>
                    <span style="color: #fff; margin-left: 20px;">${data.value.uncover}</span>
                  </div>
                </div>
              `;
            },
            backgroundColor: 'rgba(0, 0, 0, 0.8)',
            borderColor: '#666',
            borderWidth: 1,
            textStyle: {
              color: '#fff'
            },
            padding: [12, 16]
          },
          series: [
            {
              name: '杭州地图',
              type: 'map',
              map: 'hz',
              data: areaData,
              label: {
                show: true,
                color: '#fff',
                fontSize: 12
              },
              itemStyle: {
                areaColor: '#2c2c2c',
                borderColor: '#666',
                borderWidth: 1
              },
              emphasis: {
                itemStyle: {
                  areaColor: '#4a4a4a',
                  borderColor: '#fff',
                  borderWidth: 2,
                  shadowColor: 'rgba(255, 255, 255, 0.3)',
                  shadowBlur: 10
                },
                label: {
                  color: '#fff',
                  fontSize: 14
                }
              }
            }
          ]
        };
        this.myChart.setOption(option);
      })
    },
    handleSearch() {
      if (this.searchDistrict) {
        this.selectedDistrict = this.searchDistrict;
        this.showDetail = true;
      } else {
        this.$message.warning('请输入区域名称');
      }
    },
    handleBack() {
      this.showDetail = false;
      this.searchDistrict = '';
      this.selectedDistrict = '';
      // 返回时重新初始化地图
      this.$nextTick(() => {
        this.initMap();
      });
    },
    handleReloadMap() {
        // 重新加载地图数据
        this.$refs.detailMap.reloadMap();
    }
  }
}
</script>
<style>
.hzMap{
    height: 575px;
    padding: 15px;
    position: relative;
}
.map-container {
    height: 100%;
    width: 100%;
}
.search-box {
    position: absolute;
    right: 20px;
    bottom: 20px;
    display: flex;
    gap: 10px;
    z-index: 100;
    background: rgba(0, 0, 0, 0.5);
    padding: 10px;
    border-radius: 4px;
}
.search-input {
    width: 200px;
}
.detail-container {
    height: 100%;
    position: relative;
}
.detail-map {
    height: 540px;
    overflow: hidden;
}
.back-btn {
    position: absolute;
    top: 20px;
    right: 20px;
    z-index: 100;
}
</style>