<template>
   <div class="login-container dis-h">
      <div class="login-form  dis-h">
         <div class="dis-v left">
            <span> 欢迎~ </span>
            <span>井盖隐患展板</span>
         </div>
         <div class="dis-v right">
            <div class="username dis-h">
               <el-input placeholder="请输入用户名" v-model="username"/>
            </div>
            <div class="pwd dis-h">
               <el-input type="password" placeholder="请输入密码" v-model="password"/>
            </div>
            <div class="btn dis-h">
               <el-button @click="login" size="large"
                  style="width:220px;background-color:#626aef;color:#fff;font-weight:bold; ">登录</el-button>
            </div>

         </div>
      </div>
   </div>
</template>
<script>
// import axios from 'axios'
import {userLog} from './api/user'
export default {
   data(){
      return {
         username:"",
         password:""
      }
   },
   methods: {
      login(){
         userLog({
            username:this.username,
            password:this.password
         }).then(res=>{
            // console.log(res.data)
            if(res.data==2){
               this.$message.error('用户名或密码错误')
            }
            else if(res.data==1){
               document.cookie = `username=${this.username}`
               // cookie.set('username',this.username)
               this.$router.push('/manager')
            }
            else if(res.data==0){
               document.cookie = `username=${this.username}`
               // cookie.set('username',this.username)
               this.$router.push('/fix')
            }

         })
      }
   }

}
</script>
<style>
.login-container {
   width: 100vw;
   height: 100vh;
   background-image: url('../assets/background.jpeg');

   align-items: center;
   justify-content: center;
   background-repeat: no-repeat;
   /* 背景图片不重复 */
   background-size: cover;
   /* 背景图片覆盖整个div区域 */
   background-position: center;
   /* 背景图片居中显示 */
}

.login-form {
   width: 600px;
   height: 300px;
   /* background-color: red; */

}

.login-form .left {
   width: 50%;
   height: 100%;
   align-items: left;
   justify-content: center;
   font-size: 1.6rem;
   font-weight: bold;
   background: linear-gradient(to right bottom, rgba(136, 209, 234, 0.80) 5%, rgba(215, 193, 187, 0.80) 100%);
   color: #fff;
   text-indent: 1rem;
}

.login-form .right {
   width: 50%;
   height: 100%;
   background-color: rgba(255, 255, 255, 0.90);
   align-items: center;
   justify-content: center;
}

.login-form .username,
.pwd,
.btn {
   padding: 0.5rem 0;

}

/*水平排列子元素*/
.dis-h {
   display: flex;
}

/*垂直排列子元素*/
.dis-v {
   display: flex;
   flex-direction: column;
}
</style>