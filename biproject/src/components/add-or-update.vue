<template>
  <div>
    <div class="container add" >
      <div :class="'left center'" style="backgroundColor: rgba(246,245,240,0.2)">
        <el-form class="register-form" :model="userInfo" label-position="left" >
          <el-form-item>
              <el-row :gutter="20">
                  <el-col :span="5">
                      <el-button type="primary" icon="el-icon-user">
                      </el-button>
                  </el-col>
                  <el-col :span="18">
                    <el-input v-model="userInfo.username" placeholder="请输入用户名" type="text"/>
                  </el-col>
              </el-row>
         </el-form-item>

         <el-form-item>
              <el-row :gutter="20">
                  <el-col :span="5">
                      <el-button type="primary" icon="el-icon-phone">
                      </el-button>
                  </el-col>
                  <el-col :span="18">
                    <el-input v-model="userInfo.phoneNumber" placeholder="请输入手机号" type="text"/>
                  </el-col>
              </el-row>
         </el-form-item>
       
          <el-form-item>
              <el-row :gutter="20">
                  <el-col :span="5">
                    <el-button type="primary" icon="el-icon-message">
                    </el-button>
                  </el-col>
                  <el-col :span="18">
                    <el-input v-model="userInfo.mailAddress" placeholder="请输入邮箱地址" type="text"/>
                  </el-col>
              </el-row>
          </el-form-item>
          <el-form-item>
            <el-row :gutter="20">
                <el-col :span="5">
                  <el-button type="primary" icon="el-icon-location-outline">
                  </el-button>
                </el-col>
                <el-col :span="18">
                  <el-input v-model="userInfo.city" placeholder="请输入居住地" type="text"/>
                </el-col>
            </el-row>
          </el-form-item>
          <el-form-item>
              <el-row :gutter="20">
                  <el-col :span="5">
                      <el-button type="primary" icon="el-icon-tickets">
                      </el-button>
                  </el-col>
                  <el-col :span="18">
                    <el-input v-model="userInfo.remark" placeholder="请输入备注" type="text"/>
                  </el-col>
              </el-row>
         </el-form-item>
         <el-form-item>
              <el-row :gutter="20">
                  <el-col :span="5">
                      <el-button type="primary" icon="el-icon-office-building">
                      </el-button>
                  </el-col>
                  <el-col :span="18">
                    <el-input v-model="userInfo.Address" placeholder="请输入通讯地址" type="text"/>
                  </el-col>
              </el-row>
         </el-form-item>
        </el-form>
        <div style="display: flex;flex-wrap: wrap;width: 100%;justify-content: center;">
          <el-button class="btn" type="primary" @click="addPost()">提交</el-button>
          <el-button class="btn close" type="primary" @click="cancel()">取消</el-button>
        </div>
      </div>
    
    </div>
  
  </div>
</template>


<script>
import {isEmail,isMobile} from '../utils/validate'
export default {
  props:["parents"],
  data() {
    return {
      userInfo:{
        username: '',
        phoneNumber: '',
        mailAddress: '',
        city: '',
        Address: '',
        remark: '',
      },
      response: {},
      opt:''
    };
  },
  mounted() {
   this.userInfo = this.parents.obj //修改信息的表单应该自动显示用户当前的信息
   this.opt = this.parents.opt
  },
  created() {
    this.setInputColor();
  },
  methods: {  
    setInputColor(){
      this.$nextTick(()=>{
        document.querySelectorAll('.signUp .el-input__inner').forEach(el=>{
          el.style.backgroundColor = "rgba(249, 248, 248, 1)"
          el.style.color = "rgba(7, 7, 7, 1)"
          el.style.height = "35px"
          el.style.lineHeight = "35px"
          el.style.borderRadius = "10px"
        })
        document.querySelectorAll('.signUp .style3 .el-form-item__label').forEach(el=>{
          el.style.height = "35px"
          el.style.lineHeight = "35px"
        })
        document.querySelectorAll('.signUp .el-form-item__label').forEach(el=>{
          el.style.color = "rgba(24,144,255, 1)"
        })
        setTimeout(()=>{
          document.querySelectorAll('.signUp .role .el-radio__label').forEach(el=>{
            el.style.color = "rgba(252, 252, 252, 1)"
          })
        },350)
      })
    },

    cancel(){
        if(this.opt=="Update1"){
          console.log(this.opt)
          this.$emit('ActiveIndex',"userInfo")
        }else if(this.opt=="Update2"){
          console.log(this.opt)
          this.$emit('ActiveIndex',"userManage")
        }
        else{
          console.log(this.opt)
          this.$emit('ActiveIndex',"userManage")
        } 
    },
    
  //修改用户信息
  addPost() {
    let self = this
    if(!this.userInfo.username){
      this.$message.error(`用户名不能为空`);
      return ;
    }
    if(this.userInfo.mailAddress&&(!isEmail(this.userInfo.mailAddress))){
      this.$message.error(`邮箱应输入邮件格式`);
      return ;
    }
    if(this.userInfo.phoneNumber&&(!isMobile(this.userInfo.phoneNumber))){
      this.$message.error(`手机应输入手机格式`);
      return ;
    }
    this.$axios({
          method: 'GET',
          url: 'http://127.0.0.1:8000/api/modify_information/',
          params: {
            username: this.userInfo.username,
            action: (this.opt=='Add'?'insert':'update'), //opt总共两种取值'Add'和'Update',传参时需注意与后端判断进行对应
            phoneNumber: !this.userInfo.phoneNumber?'':this.userInfo.phoneNumber,
            mailAddress: !this.userInfo.mailAddress?'':this.userInfo.mailAddress,
            city: !this.userInfo.city?'':this.userInfo.city,
            Address: !this.userInfo.Address?'':this.userInfo.Address,
            remark: !this.userInfo.remark?'':this.userInfo.remark,
            
          }
        }).then(
          res => {
            console.log(res)
            if(res.data.status==1){
              this.$message({
                type: 'success',
                message: res.data.message
            })}else{
              this.$message({
                type: 'error',
                message: res.data.message
            })
            }
          }  )
  
    },
  },
};
</script>
<style>

.register-form {
  background-color: transparent;
  width: 100%;
  right: inherit;
  padding: 0 20px;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  flex-direction: column;
}

.center {
  position: absolute;
  left: 20%;
  top: 40%;
  width: 400px;
  transform: translate3d(-50%,-50%,0);
  height: 400px;
  border-radius: 8px;
}

.right {
  position: absolute;
  left: inherit;
  right: 0;
  top: 0;
  width: 360px;
  height: 100%;
}

.btn{
margin: 0 10px;
width: 88px;
height: 45px;
color: #fff;
font-size: 14px;
border-width: 0px;
border-style: solid;
border-color: #409EFF;
border-radius: 4px;
background-color: rgba(24, 144, 255, 1);
}

.close {
margin: 0 10px;
width: 88px;
height: 44px;
color: #409EFF;
font-size: 14px;
border-width: 1px;
border-style: solid;
border-color: #409EFF;
border-radius: 4px;
background-color: #FFF;
}

.input_span{
  height: 8px;
  display: flex;
  float: right;
  width: 20%;
}
.input_span_span{
    display: inline-block;
    width: 30%;
    border-radius: 8px;
    margin-right: 3px;
    text-align: center;
    margin-top: 3px;
}
</style>