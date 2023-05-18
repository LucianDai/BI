<template>
  <div>
    <div class="container signUp">
      <div class="systemName">行业企业竞争对手分析系统</div>
      <div :class="'left center'" style="backgroundColor: rgba(15, 35, 35, 0.2)">
        <el-form class="register-form" :model="rgsForm" label-position="left">
          <div class="title-container">
            <h3 class="title" style="color: rgba(24, 144, 255, 1)">用户注册</h3>
          </div>
          <el-form-item :label="''" :class="'style' + 2">
            <el-row :gutter="20">
              <el-col :span="5">
                <el-button type="primary" icon="el-icon-user">
                </el-button>
              </el-col>
              <el-col :span="18">
                <el-input v-model="rulesForm.username" placeholder="请输入用户名" type="text" />
              </el-col>
            </el-row>
          </el-form-item>
          <el-form-item :label="''" :class="'style' + 2">
            <el-row :gutter="20">
              <el-col :span="5">
                <el-button type="primary" icon="el-icon-lock"></el-button>
              </el-col>
              <el-col :span="18">
                <el-input v-model="rulesForm.password1" placeholder="请输入密码" @blur="changemsgText" type="password" />
              </el-col>
            </el-row>
            <el-form-item>
              <div class="input_span">
                <span
                  :style="{ 'background-color': (msgText > 1 || msgText == 1) ? '#FC5F76' : '#BBBBBB', 'color': (msgText > 1 || msgText == 1) ? '#FC5F76' : '#BBBBBB' }">弱</span>
                <span
                  :style="{ 'background-color': (msgText > 2 || msgText == 2) ? '#FF9900' : '#BBBBBB', 'color': (msgText > 2 || msgText == 2) ? '#FF9900' : '#BBBBBB' }">中</span>
                <span
                  :style="{ 'background-color': (msgText > 3 || msgText == 3) ? '#33CC00' : '#BBBBBB', 'color': (msgText > 3 || msgText == 3) ? '#33CC00' : '#BBBBBB' }">强</span>
              </div>
            </el-form-item>
          </el-form-item>
          <el-form-item :label="''" :class="'style' + 2">
            <el-row :gutter="20">
              <el-col :span="5">
                <el-button type="primary" icon="el-icon-lock">
                </el-button>
              </el-col>
              <el-col :span="18">
                <el-input v-model="rulesForm.password2" placeholder="请确认密码" type="password" />
              </el-col>
            </el-row>
          </el-form-item>
          <el-form-item :label="''" :class="'style' + 2">
            <el-row :gutter="20">
              <el-col :span="5">
                <el-button type="primary" icon="el-icon-message">
                </el-button>
              </el-col>
              <el-col :span="18">
                <el-input v-model="rulesForm.mailAdress" autocomplete="off" placeholder="请输入邮箱地址" />
              </el-col>
            </el-row>
          </el-form-item>
          <el-form-item :label="''" :class="'style' + 2">
            <el-row :gutter="20">
              <el-col :span="5">
                <el-button type="primary" icon="el-icon-phone">
                </el-button>
              </el-col>
              <el-col :span="18">
                <el-input v-model="rulesForm.phoneNumber" autocomplete="off" placeholder="请输入手机号" />
              </el-col>
            </el-row>
          </el-form-item>
          <div style="display: flex;flex-wrap: wrap;width: 100%;justify-content: center;">
            <el-button class="btn" type="primary" @click="register()">注册</el-button>
            <el-button class="btn close" type="primary" @click="close()">取消</el-button>
          </div>
        </el-form>
      </div>

    </div>
  </div>
</template>


<script>

import { isEmail, isMobile, checkPassword } from '../utils/validate'
import storage from '@/utils/storage'

export default {
  data() {
    return {
      rulesForm: {
      },
      rules: {},
      msgText: 0,
      response: {}
    };
  },
  mounted() {
    let data1 = storage.get("sessionTable")
    console.log(data1)
  },
  created() {
    this.setInputColor();
  },
  methods: {
    setInputColor() {
      this.$nextTick(() => {
        document.querySelectorAll('.signUp .el-input__inner').forEach(el => {
          el.style.backgroundColor = "rgba(249, 248, 248, 1)"
          el.style.color = "rgba(7, 7, 7, 1)"
          el.style.height = "35px"
          el.style.lineHeight = "35px"
          el.style.borderRadius = "10px"
        })
        document.querySelectorAll('.signUp .style3 .el-form-item__label').forEach(el => {
          el.style.height = "35px"
          el.style.lineHeight = "35px"
        })
        document.querySelectorAll('.signUp .el-form-item__label').forEach(el => {
          el.style.color = "rgba(24,144,255, 1)"
        })
        setTimeout(() => {
          document.querySelectorAll('.signUp .role .el-radio__label').forEach(el => {
            el.style.color = "rgba(252, 252, 252, 1)"
          })
        }, 350)
      })
    },

    close() {
      this.$router.push({ path: "/login" });
    },
    changemsgText() {
      this.msgText = checkPassword(this.rulesForm.password1)
    },

    // 注册
    register() {
      /*
         对用户输入的信息进行校验
       */
      if (!this.rulesForm.username) {
        this.$message.error(`用户名不能为空`);
        return;
      }
      if (!this.rulesForm.password1) {
        this.$message.error(`密码不能为空`);
        return;
      }
      if (!this.rulesForm.password2) {
        this.$message.error(`请再次输入密码确认`);
        return;
      }
      if ((this.rulesForm.password2 && this.rulesForm.password1) && (this.rulesForm.password2 != this.rulesForm.password1)) {
        this.$message.error(`密码输入不一致，请重新输入`);
        return;
      }
      if (this.rulesForm.mailAdress && (!isEmail(this.rulesForm.mailAdress))) {
        this.$message.error(`邮箱应输入邮件格式`);
        return;
      }
      if (this.rulesForm.phoneNumber && (!isMobile(this.rulesForm.phoneNumber))) {
        this.$message.error(`手机应输入手机格式`);
        return;
      }
      /*
        如果输入无误，则上传信息，并跳转到登录界面
      */
      this.$axios({
        method: 'GET',
        url: "http://127.0.0.1:8000/api/register/",
        params: {
          username: this.rulesForm.username,
          password: this.rulesForm.password1
        }
      })
        .then(res => {
          // console.log(res);
          this.response = res.data;
          // console.log(this.response);
          // console.log(this.response.status);
          if (this.response.status == 1) {
            this.$message({
              message: "注册成功",
              type: "success",
              duration: 1500,
              onClose: () => {
                this.$router.replace({ path: "/login" });
              }
            });
          } else {
            this.$message.error(`用户名已存在`);
          }
        })


    }
  },

};
</script>

<style>
.signUp {
  background-image: url("../assets/bg1.jpg");
  min-height: 100vh;
  position: relative;
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
}

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
  left: 50%;
  top: 55%;
  width: 400px;
  transform: translate3d(-50%, -50%, 0);
  height: 450px;
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

.title-container {
  text-align: center;
  font-size: 30px;
}

.title {
  margin: 20px 0;
}

.systemName {
  padding-top: 40px;
  text-align: center;
  font-size: 50px;
  color: white;
  letter-spacing: 0;
  text-shadow: 0px 1px 0px #999, 0px 2px 0px #888, 0px 3px 0px #777, 0px 4px 0px #666, 0px 5px 0px #555, 0px 6px 0px #444, 0px 7px 0px #333, 0px 8px 7px #001135
}

.btn {
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

.input_span {
  height: 8px;
  display: flex;
  float: right;
  width: 20%;
}

.input_span_span {
  display: inline-block;
  width: 30%;
  border-radius: 8px;
  margin-right: 3px;
  text-align: center;
  margin-top: 3px;
}
</style>