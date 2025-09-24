<template>
    <div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <h2 style="color: #fff;margin-top: 30px;margin-left: 20px;">巡检人员信息</h2>
            <el-button style="margin-right: 15px;margin-top: 30px;" type="primary" @click="openDialog">注册巡检人员</el-button>
        </div>
        <el-table :data="tableData" height="250" border 
        style="width: 90%;position: relative;left: 5%;top: 5%;"
        :header-cell-style="{
            background:'#1a1a1a',
            color: '#fff',
            fontWeight: 'bold',
            fontSize: '14px'
        }"
        :row-style="{
            background:'#000',
            transition: 'all 0.3s'
        }"
        :row-class-name="tableRowClassName">
            <el-table-column prop="name" label="姓名" width="120">
                <template slot-scope="scope">
                    <span class="cell-content">{{ scope.row.name }}</span>
                </template>
            </el-table-column>
            <el-table-column prop="area" label="分管区域" width="120">
                <template slot-scope="scope">
                    <span class="cell-content">{{ scope.row.area }}</span>
                </template>
            </el-table-column>
            <el-table-column prop="phonenum" label="联系方式" min-width="200">
                <template slot-scope="scope">
                    <span class="cell-content">{{ scope.row.phonenum }}</span>
                </template>
            </el-table-column>
        </el-table>

        <el-dialog title="注册巡检人员" :visible.sync="dialogVisible" :modal="false">
            <el-form :model="form">
                <el-form-item label="姓名">
                    <el-input v-model="form.name"></el-input>
                </el-form-item>
                <el-form-item label="密码">
                    <el-input v-model="form.password"></el-input>
                </el-form-item>
                <el-form-item label="分管区域">
                    <el-input v-model="form.area"></el-input>
                </el-form-item>
                <el-form-item label="联系方式">
                    <el-input v-model="form.phonenum"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">取消</el-button>
                <el-button type="primary" @click="register">注册</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>


// import * as echarts from "echarts";
import { getAllfixer,registerPerson } from '@/views/api/manager'
export default {
    data() {
        return {
           tableData: [],
           dialogVisible: false,
           form: {
               name: '',
               area: '',
               phonenum: '',
               password: ''
           }
        }
    },
    
    created() {
        this.fetchFixerData();
    },

    methods: {
        register() {
            registerPerson(this.form).then(res=>{
                console.log(res);
                if(res.data == "success"){
                    this.$message({
                        message: '注册成功',
                        type: 'success'
                    });
                    this.dialogVisible = false;
                    this.fetchFixerData(); // 刷新表格数据
                    // 清空表单
                    this.form = {
                        name: '',
                        area: '',
                        phonenum: '',
                        password: ''
                    };
                } else {
                    this.$message.error('注册失败：' + res.msg);
                }
            }).catch(error => {
                this.$message.error('注册失败：' + error.message);
            });
        },
        async fetchFixerData() {
            try {
                const response = await getAllfixer();
                // console.log('获取到的巡检人员数据:', response);
                this.tableData = response.data;
            } catch (error) {
                console.error('获取巡检人员数据失败:', error);
            }
        },
        tableRowClassName({rowIndex}) {
            if (rowIndex % 2 === 0) {
                return 'even-row'
            } else {
                return 'odd-row'
            }
        },
        openDialog() {
            this.dialogVisible = true;
        },
        registerPerson() {
            // 注册逻辑
            console.log('注册信息:', this.form);
            this.dialogVisible = false;
        }
    }
}
</script>

<style scoped>
.el-table {
    background-color: #000;
    color: #fff;
    border-radius: 4px;
    overflow: hidden;
}

.el-table--border::after, 
.el-table--group::after, 
.el-table::before {
    background-color: #1a1a1a;
}

.el-table--border {
    border: 1px solid #1a1a1a;
}

.el-table th {
    background-color: #1a1a1a !important;
    border-bottom: 1px solid #333;
}

.el-table td {
    border-bottom: 1px solid #333;
}

.cell-content {
    display: inline-block;
    padding: 0 5px;
}

.even-row {
    background-color: rgba(0, 0, 0, 0.5) !important;
}

.odd-row {
    background-color: rgba(0, 0, 0, 0.3) !important;
}

.el-table__row:hover > td {
    background-color: rgba(0, 51, 102, 0.5) !important;
    transition: all 0.3s;
}

.el-table__header th {
    background-color: #1a1a1a !important;
    /* color: #fff; */
    font-weight: bold;
}

/* 添加暗色主题对话框样式 */
:deep(.el-dialog) {
    background-color: #1a1a1a;
    border: 1px solid #333;
}

:deep(.el-dialog__title) {
    color: #fff;
}

:deep(.el-dialog__body) {
    color: #fff;
}

:deep(.el-form-item__label) {
    color: #fff;
}

:deep(.el-input__inner) {
    background-color: #000;
    border: 1px solid #333;
    color: #fff;
}

:deep(.el-input__inner:focus) {
    border-color: #409EFF;
}

:deep(.el-button--default) {
    background-color: #333;
    border-color: #444;
    color: #fff;
}

:deep(.el-button--default:hover) {
    background-color: #444;
    border-color: #555;
    color: #fff;
}
</style>