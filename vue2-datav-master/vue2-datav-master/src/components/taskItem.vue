<template>
    <div class="taskItem">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <h2 style="color: #fff;margin-top: 10px;margin-left: 15px;">任务信息</h2>
            <el-button style="margin-right: 15px;margin-top: 10px;" type="primary" @click="openDialog">发布任务</el-button>
        </div>
        <!-- <dv-scroll-board :config="config"  /> -->
        <el-table :data="tableData" border 
        style="width: 90%;position: relative;left: 5%;top: 5%;height: calc(100% - 60px);"
        :header-cell-style="{
            background:'#1a1a1a',
            color: '#fff',
            fontWeight: 'bold',
            fontSize: '14px'
        }"
        :row-style="{
            background:'#000',
            color: '#fff',
            transition: 'all 0.3s'
        }"
        :cell-style="{
            background:'#000',
            color: '#fff'
        }"
        :row-class-name="tableRowClassName">
            <el-table-column prop="taskId" label="#" width="40">
                <template slot-scope="scope">
                    <span class="cell-content">{{ scope.row.taskId }}</span>
                </template>
            </el-table-column>
            <el-table-column prop="area" label="区域" width="80">
                <template slot-scope="scope">
                    <span class="cell-content">{{ scope.row.area }}</span>
                </template>
            </el-table-column>
            <el-table-column prop="hole" label="井盖编号" width="80">
                <template slot-scope="scope">
                    <span class="cell-content">{{ scope.row.hole }}</span>
                </template>
            </el-table-column>
            <el-table-column prop="taskType" label="任务类型" width="80">
                <template slot-scope="scope">
                    <span class="cell-content">{{ scope.row.taskType }}</span>
                </template>
            </el-table-column>
            <el-table-column label="状态查看" width="200">
                <template slot-scope="scope">
                    <el-button-group>
                        <el-button size="mini" @click="showProgress(scope.row)">进度</el-button>
                        <el-button size="mini" type="success" @click="handlePass(scope.row)">通过</el-button>
                    </el-button-group>
                </template>
            </el-table-column>
        </el-table>
        
        <!-- 添加发布任务对话框 -->
        <el-dialog
            title="发布任务"
            :visible.sync="dialogVisible"
            width="30%"
            :close-on-click-modal="false"
            :modal-append-to-body="false"
            :append-to-body="true"
            :modal="false"
            custom-class="task-dialog">
            <el-form :model="taskForm" :rules="rules" ref="taskForm" label-width="100px">
                <el-form-item label="区域" prop="area">
                    <el-select v-model="taskForm.area" placeholder="请选择区域">
                        <el-option label="上城区" value="上城区"></el-option>
                        <el-option label="下城区" value="下城区"></el-option>
                        <el-option label="江干区" value="江干区"></el-option>
                        <el-option label="拱墅区" value="拱墅区"></el-option>
                        <el-option label="西湖区" value="西湖区"></el-option>
                        <el-option label="滨江区" value="滨江区"></el-option>
                        <el-option label="萧山区" value="萧山区"></el-option>
                        <el-option label="余杭区" value="余杭区"></el-option>
                        <el-option label="富阳区" value="富阳区"></el-option>
                        <el-option label="临安区" value="临安区"></el-option>
                        <el-option label="钱塘区" value="钱塘区"></el-option>
                        <el-option label="临平区" value="临平区"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="井盖编号" prop="hole">
                    <el-input v-model="taskForm.hole" placeholder="请输入井盖编号"></el-input>
                </el-form-item>
                <el-form-item label="任务类型" prop="taskType">
                    <el-select v-model="taskForm.taskType" placeholder="请选择任务类型">
                        <el-option label="维修任务" value="维修任务"></el-option>
                        <el-option label="巡检任务" value="巡检任务"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="详细说明" prop="description">
                    <el-input type="textarea" v-model="taskForm.description" placeholder="请输入详细说明"></el-input>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="submitForm">确 定</el-button>
            </span>
        </el-dialog>

        <!-- 添加进度图片对话框 -->
        <el-dialog
            title="任务进度"
            :visible.sync="progressDialogVisible"
            width="50%"
            :close-on-click-modal="false"
            :modal-append-to-body="false"
            :append-to-body="true"
            :modal="false"
            custom-class="task-dialog">
            <div class="progress-image-container">
                <img v-if="progressImage" :src="progressImage" class="progress-image" />
                <div v-else class="no-image">暂无进度图片</div>
            </div>
        </el-dialog>
    </div>
</template>
<script>

import { getAllTask,publishTask,getTaskProgress,checkTask} from '@/views/api/manager'
// import * as echarts from "echarts";

export default {
    data() {
        return {
            tableData: [],
            dialogVisible: false,
            progressDialogVisible: false,
            progressImage: '',
            taskForm: {
                area: '',
                hole: '',
                taskType: '',
                description: ''
            },
            rules: {
                area: [
                    { required: true, message: '请输入区域', trigger: 'blur' }
                ],
                hole: [
                    { required: false, message: '请输入井盖编号', trigger: 'blur' }
                ],
                taskType: [
                    { required: true, message: '请选择任务类型', trigger: 'change' }
                ],
                description: [
                    { required: true, message: '请输入详细说明', trigger: 'blur' }
                ]
            }
        }
    },
    created(){
        getAllTask().then(res=>{
            // console.log(res)
            this.tableData = res.data.map((item) => ({
                taskId: item.id,
                area: item.area,
                hole: item.hole,
                taskType: item.taskType
            }))
        })
    },
    methods: {
        getAllTask() {
            getAllTask().then(res => {
                this.tableData = res.data.map((item) => ({
                    taskId: item.id,
                    area: item.area,
                    hole: item.hole,
                    taskType: item.taskType
                }))
            })
        },
        openDialog() {
            this.dialogVisible = true;
            this.taskForm = {
                area: '',
                hole: '',
                taskType: '',
                description: ''
            };
        },
        submitForm() {
            publishTask(this.taskForm).then(res=>{
                if(res.data == "success"){
                    this.$message.success('任务发布成功');
                    this.dialogVisible = false;
                    this.getAllTask();
                }else{
                    this.$message.error('任务发布失败');
                }
            })
        },
        showProgress(row) {
            getTaskProgress({
                taskId: row.taskId
            }).then(res=>{
                if(res.data && res.status === 'success') {
                    this.progressImage = 'data:image/jpeg;base64,' + res.data;
                    this.progressDialogVisible = true;
                } else {
                    this.$message.info('暂无进度图片');
                }
            })
        },
        handlePass(row) {
            checkTask({
                taskId: row.taskId
            }).then(res=>{
                if(res.data == "success"){
                    this.$message.success('已通过审核：' + row.taskId);
                    this.getAllTask();
                }
            })
            // // 从tableData中删除对应的行
            // const index = this.tableData.findIndex(item => item.taskId === row.taskId);
            // if (index !== -1) {
            //     this.tableData.splice(index, 1);
            //     this.$message.success('已通过审核：' + row.taskId);
            // }
        },
        tableRowClassName() {
            return 'table-row';
        }
    }
}
</script>
<style scoped>
.taskItem {
    height: 90%;
    padding: 5%;
    overflow: hidden;
}
.cell-content {
    color: #fff;
}
.table-row:hover {
    background: #2a2a2a !important;
}
:deep(.el-table) {
    background-color: #000;
}
:deep(.el-table__body-wrapper) {
    overflow-y: auto;
    height: calc(100% - 40px);
}
:deep(.el-table__body-wrapper::-webkit-scrollbar) {
    width: 6px;
    background-color: #1a1a1a;
}
:deep(.el-table__body-wrapper::-webkit-scrollbar-thumb) {
    background-color: #3a3a3a;
    border-radius: 3px;
}
:deep(.el-table__body-wrapper::-webkit-scrollbar-thumb:hover) {
    background-color: #4a4a4a;
}
.task-dialog {
    background: #1a1a1a;
    color: #fff;
    border: 1px solid #3a3a3a;
}
:deep(.el-dialog__header) {
    background: #1a1a1a;
    border-bottom: 1px solid #3a3a3a;
    padding: 15px 20px;
}
:deep(.el-dialog__body) {
    background: #1a1a1a;
    padding: 20px;
}
:deep(.el-dialog__footer) {
    background: #1a1a1a;
    border-top: 1px solid #3a3a3a;
    padding: 15px 20px;
}
:deep(.el-dialog__title) {
    color: #fff;
    font-size: 16px;
    font-weight: bold;
}
:deep(.el-dialog__headerbtn .el-dialog__close) {
    color: #fff;
}
:deep(.el-dialog__headerbtn:hover .el-dialog__close) {
    color: #409EFF;
}
:deep(.el-form-item__label) {
    color: #fff;
}
:deep(.el-input__inner) {
    background: #2a2a2a;
    border: 1px solid #3a3a3a;
    color: #fff;
}
:deep(.el-textarea__inner) {
    background: #2a2a2a;
    border: 1px solid #3a3a3a;
    color: #fff;
}
:deep(.el-select .el-input__inner) {
    background: #2a2a2a;
    border: 1px solid #3a3a3a;
    color: #fff;
}
:deep(.el-select-dropdown) {
    background: #2a2a2a;
    border: 1px solid #3a3a3a;
}
:deep(.el-select-dropdown__item) {
    color: #fff;
}
:deep(.el-select-dropdown__item.hover, .el-select-dropdown__item:hover) {
    background: #3a3a3a;
}
:deep(.el-select-dropdown__item.selected) {
    color: #409EFF;
    background: #2a2a2a;
}

.progress-image-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 300px;
    background: #1a1a1a;
    border-radius: 4px;
}

.progress-image {
    max-width: 100%;
    max-height: 500px;
    object-fit: contain;
}

.no-image {
    color: #666;
    font-size: 16px;
}
</style>