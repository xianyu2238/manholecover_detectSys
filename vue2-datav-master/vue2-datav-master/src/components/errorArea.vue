<template>
  <div style="height: 90%;">
    <dv-capsule-chart :config="config" class="erroArea" />
  </div>
</template>
<script>
import { getErrorArea } from "../views/api/manager";
export default {
  created() {
    this.fetchData();
  },
  data() {
    return {
      config: {
        data: [],
        colors: ['#e062ae', '#fb7293', '#e690d1', '#32c5e9', '#96bfff'],
        unit: '数量'
      }
    }
  },
  methods: {
    fetchData() {
      getErrorArea().then(res => {
        if (res && res.data) {
          // console.log('处理后的数据:', res.data);
          this.config = {
            ...this.config,
            data: res.data
          };
        } else {
          console.error('数据格式错误:', res);
        }
      }).catch(error => {
        console.error('获取数据失败:', error);
      });
    }
  },
}
</script>
<style scoped>
.erroArea {
  height: 100%;
  padding: 5%
}
</style>