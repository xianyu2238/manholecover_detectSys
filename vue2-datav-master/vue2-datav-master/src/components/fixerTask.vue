<template>
    <div style="height: 100%;">
        <dv-border-box-9>
            <div class="table-container">
                <table class="task-table">
                    <thead>
                        <tr>
                            <th>编号</th>
                            <th>任务类型</th>
                            <th>井盖编号</th>
                            <th>任务详情</th>
                            <th>任务处理</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(task, index) in taskList" :key="index">
                            <td>{{ task.id }}</td>
                            <td>{{ task.type }}</td>
                            <td>{{ task.hole }}</td>
                            <td>{{ task.description }}</td>
                            <td>
                                <button class="view-btn" @click="viewTaskDetail(task)">提交处理</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </dv-border-box-9>
        <el-dialog title="处理提交" :visible.sync="dialogFormVisible" :modal="false">
            <el-form :model="form">
                <el-form-item label="过程图片上传" :label-width="formLabelWidth">
                    <el-upload 
                        class="upload-demo" 
                        drag 
                        :action="null"
                        :http-request="handleUpload"
                        :before-upload="beforeUpload"
                        multiple>
                        <i class="el-icon-upload"></i>
                        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                        <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过50kb</div>
                    </el-upload>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogFormVisible = false">取 消</el-button>
                <el-button type="primary" @click="submitImages">确 定</el-button>
            </div>
        </el-dialog>
    </div>
</template>
<script>
import { getFixTask, submitTask } from '@/views/api/fixer'
export default {
    props: ['district'],
    data() {
        return {
            taskList: [],
            dialogFormVisible: false,
            currentTask: null,
            form: {
                name: '',
                region: '',
                date1: '',
                date2: '',
                images: []
            }
        }
    },
    watch: {
        district: {
            handler(newVal) {
                getFixTask({
                    district: newVal
                }).then(res => {
                    this.taskList = res.data.map((item) => ({
                        id: item.id,
                        type: item.taskType,
                        hole: item.hole || ' ',
                        description: item.taskDetail
                    }))
                })
            }
        }
    },
    methods: {
        viewTaskDetail(task) {
            this.currentTask = task
            this.dialogFormVisible = true
        },
        beforeUpload(file) {
            const isJPG = file.type === 'image/jpeg' || file.type === 'image/png'
            const isLt500K = file.size / 1024 < 500

            if (!isJPG) {
                this.$message.error('上传图片只能是 JPG/PNG 格式!')
                return false
            }
            if (!isLt500K) {
                this.$message.error('上传图片大小不能超过 500KB!')
                return false
            }
            return true
        },

        async handleUpload(options) {
            try {
                const compressedImage = await this.compressImage(options.file)
                this.form.images.push(compressedImage)
                this.$message.success('图片上传成功')
            } catch (error) {
                this.$message.error('图片处理失败')
                console.error(error)
            }
        },

        compressImage(file) {
            return new Promise((resolve, reject) => {
                const reader = new FileReader()
                reader.readAsDataURL(file)
                reader.onload = (e) => {
                    const img = new Image()
                    img.src = e.target.result
                    img.onload = () => {
                        const canvas = document.createElement('canvas')
                        let width = img.width
                        let height = img.height
                        
                        // 计算压缩比例
                        let ratio = 1
                        if (file.size > 50 * 1024) {
                            ratio = Math.sqrt(50 * 1024 / file.size)
                        }
                        
                        width *= ratio
                        height *= ratio
                        
                        canvas.width = width
                        canvas.height = height
                        
                        const ctx = canvas.getContext('2d')
                        ctx.drawImage(img, 0, 0, width, height)
                        
                        // 转换为base64，使用较低的质量
                        const base64 = canvas.toDataURL('image/jpeg', 0.6)
                        resolve(base64)
                    }
                    img.onerror = reject
                }
                reader.onerror = reject
            })
        },

        async submitImages() {
            try {
                const submitData = {
                    taskId: this.currentTask.id,
                    image: this.form.images[0] || ''  // 只取第一张图片
                }
                console.log(submitData)
                const res = await submitTask(submitData)
                if (res.code === 200) {
                    this.$message.success('提交成功')
                    this.dialogFormVisible = false
                    this.form.images = []
                } else {
                    this.$message.error(res.message || '提交失败')
                }
            } catch (error) {
                console.error(error)
                this.$message.error('提交失败')
            }
        }
    }
}
</script>
<style scoped>
:deep(.el-textarea) {
    background-color: #2d2d2d;
}
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
.table-container {
    padding: 20px;
    color: #fff;
}

.task-table {
    width: 100%;
    border-collapse: collapse;
    background-color: rgba(0, 0, 0, 0.3);
}

.task-table th,
.task-table td {
    padding: 12px;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.1);
}

.task-table th {
    background-color: rgba(0, 0, 0, 0.5);
    color: #00ffff;
}

.task-table tr:hover {
    background-color: rgba(0, 0, 0, 0.4);
}

.view-btn {
    background-color: #00a1ff;
    color: white;
    border: none;
    padding: 5px 15px;
    border-radius: 4px;
    cursor: pointer;
}

.view-btn:hover {
    background-color: #0084d1;
}
</style>