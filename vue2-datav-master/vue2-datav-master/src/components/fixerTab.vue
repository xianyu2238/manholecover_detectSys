<template>
    <div class="fixer-tab">
        <div class="header">
            <h2 class="title">{{username}}，你好</h2>
            <el-button size="big" @click="dialogVisible = true">异常提交</el-button>
        </div>
        <div class="time">{{ datetimeStr }}</div>

        <!-- 异常提交对话框 -->
        <el-dialog
            title="异常提交"
            :visible.sync="dialogVisible"
            width="50%"
            :modal="false">
            <el-form :model="form" label-width="80px">
                <el-form-item label="地区">
                    <el-input v-model="form.region" placeholder="请输入地区"></el-input>
                </el-form-item>
                <el-form-item label="经度">
                    <el-input v-model="form.longitude" placeholder="请输入经度"></el-input>
                </el-form-item>
                <el-form-item label="纬度">
                    <el-input v-model="form.latitude" placeholder="请输入纬度"></el-input>
                </el-form-item>
                <el-form-item label="状态">
                    <el-input v-model="form.state" placeholder="请输入状态"></el-input>
                </el-form-item>
                <el-form-item label="图片">
                    <el-upload
                        class="upload-demo"
                        action="#"
                        :auto-upload="false"
                        :on-change="handleChange"
                        list-type="picture-card">
                        <i class="el-icon-plus"></i>
                    </el-upload>
                </el-form-item>
                <el-form-item v-if="uploadResult" label="检测结果">
                    <div class="result-image">
                        <img :src="'data:image/jpeg;base64,' + uploadResult" alt="检测结果">
                    </div>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="submitForm">确 定</el-button>
                <el-button type="success" @click="detectImage">检 测</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
import { detect, submitPoint } from '../views/api/fixer'
export default {
    props:['username'],
    data() {
        return {
            selectedFile: null,
            previewUrl: '',
            uploadResult: null,
            datetimeStr: '', // 显示当前时间
            formatDate: null, // 定时器
            dialogVisible: false,
            form: {
                region: '',
                longitude: '',
                latitude: '',
                state: '',
                pic: ''
            },
            imageUrl: ''
        }
    },
    mounted() {
      this.updateDateTime();
      this.formatDate = setInterval(() => {
        this.updateDateTime();
      }, 1000);
    },
    unmounted() { // 在Vue实例销毁前，清除时间定时器
      if (this.formatDate) {
        clearInterval(this.formatDate);
      }
    },
    methods: {
      updateDateTime() { // 格式化需要展示的时间格式
        const now = new Date();
        const year = now.getFullYear();
        let month = now.getMonth() + 1;
        let day = now.getDate();
        const weekday = now.getDay();
        let hours = now.getHours();
        let minutes = now.getMinutes();
        let seconds = now.getSeconds();
        
        // 将月份和日期补零
        month = month < 10 ? '0' + month : month;
        day = day < 10 ? '0' + day : day;
        hours = hours < 10 ? '0' + hours : hours;
        minutes = minutes < 10 ? '0' + minutes : minutes;
        seconds = seconds < 10 ? '0' + seconds : seconds;
        
        // 星期数组
        const weekdays = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'];
    
        // 格式化日期时间
        this.datetimeStr = year + "年" + month + "月" + day + "日 " + weekdays[weekday] + " " + hours + ":" + minutes + ":" + seconds;
      },
      handleChange(file) {
        this.selectedFile = file.raw
        this.previewUrl = URL.createObjectURL(file.raw)
        this.uploadResult = null  // 清除上次结果
        
        // 将图片转换为base64
        const reader = new FileReader()
        reader.readAsDataURL(file.raw)
        reader.onload = (e) => {
            // 获取base64字符串，去掉前缀
            const base64 = e.target.result.split(',')[1]
            this.form.pic = base64
        }
      },
      async detectImage() {
        if (!this.selectedFile) return
        const formData = new FormData()
        formData.append('file', this.selectedFile)
        detect(formData).then(res => {
            console.log(res)
            if (res.status === 'success') {
                this.uploadResult = res.detect_res
            } else {
                this.$message.error('检测失败')
            }
        }).catch(error => {
            console.error('检测出错:', error)
            this.$message.error('检测失败，请重试')
        })
      },
      submitForm() {
        if (!this.form.region || !this.form.longitude || !this.form.latitude || !this.form.state || !this.form.pic) {
            this.$message.warning('请填写完整信息并上传图片');
            return;
        }
        submitPoint(this.form).then(res => {
            if(res.data === 'update success' || res.data === 'insert success') {
                this.$message.success('提交成功');
                this.dialogVisible = false;
                // 清空表单
                this.form = {
                    region: '',
                    longitude: '',
                    latitude: '',
                    state: '',
                    pic: ''
                };
                this.selectedFile = null;
                this.previewUrl = '';
                this.uploadResult = null;
                
                // 触发地图重新加载
                this.$emit('reload-map');
            } else {
                this.$message.error('提交失败');
            }
        })
      }
    }
}
</script>

<style scoped>
.fixer-tab {
    height: 100%;
    /* padding: 20px; */
}

.header {
    padding: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.title {
    color:aliceblue;
    font-size: 30px;
}
.time {
    color:aliceblue;
    font-size: 25px;
    padding: 20px;
}

.upload-demo {
    width: 100%;
}

/* 暗色主题样式 */
:deep(.el-dialog) {
    background-color: #1e1e1e;
    border: 1px solid #333;
}

:deep(.el-dialog__title) {
    color: #fff;
}

:deep(.el-dialog__header) {
    border-bottom: 1px solid #333;
}

:deep(.el-dialog__body) {
    color: #fff;
}

:deep(.el-form-item__label) {
    color: #fff;
}

:deep(.el-input__inner) {
    background-color: #2d2d2d;
    border: 1px solid #333;
    color: #fff;
}

:deep(.el-upload-dragger) {
    background-color: #2d2d2d;
    border: 1px solid #333;
}

:deep(.el-upload__tip) {
    color: #999;
}

:deep(.el-button--default) {
    background-color: #2d2d2d;
    border-color: #333;
    color: #fff;
}

:deep(.el-button--default:hover) {
    background-color: #3d3d3d;
    border-color: #444;
}

:deep(.el-button--primary) {
    background-color: #409EFF;
    border-color: #409EFF;
}

:deep(.el-button--primary:hover) {
    background-color: #66b1ff;
    border-color: #66b1ff;
}

.result-image {
    margin-top: 20px;

}

.result-image img {
    max-width: 100%;
    max-height: 300px;
    border: 1px solid #333;
    border-radius: 4px;
}

:deep(.el-upload--picture-card) {
    background-color: #2d2d2d;
    border: 1px solid #333;
}

:deep(.el-upload--picture-card:hover) {
    border-color: #409EFF;
}
</style>