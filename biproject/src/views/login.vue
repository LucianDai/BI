<template>
  <div>
    <div class="container loginIn">
      <div class="systemName">行业企业竞争对手分析系统</div>
      <div :class="'left center'" style="backgroundColor: rgba(15, 35, 35, 0.2)">
        <el-form class="login-form" label-position="left">
          <div class="title-container">
            <h3 class="title" style="color: rgba(24, 144, 255, 1)">用户登录</h3>
          </div>
          <el-form-item>
            <el-row :gutter="20">
              <el-col :span="5"><el-button type="primary" icon="el-icon-user"></el-button></el-col>
              <el-col :span="18"><el-input placeholder="请输入用户名" name="username" type="text"
                  v-model="rulesForm.username" /></el-col>
            </el-row>
          </el-form-item>
          <el-form-item>
            <el-row :gutter="20">
              <el-col :span="5"><el-button type="primary" icon="el-icon-lock"></el-button></el-col>
              <el-col :span="18"><el-input placeholder="请输入密码" name="password" type="password"
                  v-model="rulesForm.password" /></el-col>
            </el-row>
          </el-form-item>
          <el-form-item prop="loginInRole" class="role">
            <el-radio v-for="item in menus" v-if="item.hasBackLogin == '是'" v-bind:key="item.roleName"
              v-model="rulesForm.role" :label="item.roleName">{{ item.roleName }}</el-radio>
          </el-form-item>
          <el-button type="primary" @click="login()" class="loginInBt"
            style="padding:0;font-size:20px ;border-radius:40px;height:35px;line-height:35px;width:100%;backgroundColor:rgba(24, 144, 255, 1); borderColor:rgba(24, 144, 255, 1); color:rgba(252, 251, 249, 1)">{{
              '登录' }}</el-button>
          <el-form-item class="setting">
            <div style="color:rgba(24, 144, 255, 1)" class="register" @click="register()">注册用户</div>
          </el-form-item>
        </el-form>
      </div>

    </div>
  </div>
</template>

<script>
import menu from "@/utils/menu";
export default {
  data() {
    return {
      rulesForm: {
        username: "",
        password: "",
        role: "",
      },
      menus: [],
      response: {}

    };
  },
  mounted() {
    let menus = menu.list();
    this.menus = menus;
  },
  created() {
    this.setInputColor()
  },
  methods: {
    setInputColor() {
      this.$nextTick(() => {
        document.querySelectorAll('.loginIn .el-input__inner').forEach(el => {
          el.style.backgroundColor = "rgba(249, 248, 248, 1)"
          el.style.color = "rgba(7, 7, 7, 1)"
          el.style.height = "35px"
          el.style.lineHeight = "35px"
          el.style.borderRadius = "10px"
        })
        document.querySelectorAll('.loginIn .style3 .el-form-item__label').forEach(el => {
          el.style.height = "35px"
          el.style.lineHeight = "35px"
        })
        document.querySelectorAll('.loginIn .el-form-item__label').forEach(el => {
          el.style.color = "rgba(24,144,255, 1)"
        })
        setTimeout(() => {
          document.querySelectorAll('.loginIn .role .el-radio__label').forEach(el => {
            el.style.color = "rgba(252, 252, 252, 1)"
          })
        }, 350)
      })

    },

    register() {
      this.$router.push({ path: '/register' })
    },

    login() {

      if (!this.rulesForm.username) {
        this.$message.error("请输入用户名");
        return;
      }
      if (!this.rulesForm.password) {
        this.$message.error("请输入密码");
        return;
      }
      if (!this.rulesForm.role) {
        this.$message.error("请选择角色");
        return;
      }

      let menus = this.menus;
      for (let i = 0; i < menus.length; i++) {
        if (menus[i].roleName == this.rulesForm.role) {
          this.tableName = menus[i].tableName;
        }
      }

      this.$axios({
        method: 'GET',
        url: "http://127.0.0.1:8000/api/login/",
        params: {
          username: this.rulesForm.username,
          password: this.rulesForm.password
        }
      })
        .then(res => {
          console.log(res);
          this.response = res.data;
          console.log(this.response.status);
          if (this.response.status == 1) { //如果用户名与密码匹配正确

            if (this.rulesForm.role == '管理员') {

              this.$router.replace({ path: "/admin/", query: { username: this.rulesForm.username } });
            } else if (this.rulesForm.role == '用户') {

              this.$router.replace({ path: "/user/", query: { username: this.rulesForm.username } });
            }
          } else if (this.response.status == 2) {
            this.$message.error("密码错误或用户不存在！");
          }
        })


    },


  }
};
</script>


<style>
.loginIn {
  background-image: url("../assets/bg1.jpg");
  min-height: 100vh;
  position: relative;
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
}

.login-form {
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

.role {

  padding: 0 80px;
}

.register {
  text-decoration: underline;
  float: left;
  width: 20%;
}
</style>