<template>
  <div>
    <el-form class="detail-form-content" ref="ruleForm" :rules="rules" :model="ruleForm" label-width="80px">
      <el-form-item label="原密码" prop="password">
        <el-input v-model="ruleForm.password" show-password></el-input>
      </el-form-item>
      <el-form-item label="新密码" prop="newpassword">
        <el-input v-model="ruleForm.newpassword" show-password></el-input>
      </el-form-item>
      <el-form-item label="确认密码" prop="repassword">
        <el-input v-model="ruleForm.repassword" show-password></el-input>
      </el-form-item>
      <el-form-item>
        <el-button class="btn" type="primary" @click="addPost()">提交</el-button>
        <el-button class="btn close" type="primary" @click="cancel()">取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>

export default {
  props:["parents"],
  data() {
    return {
      dialogVisible: false,
      ruleForm: {},
      username: '',
      rules: {
        password: [
          {
            required: true,
            message: "密码不能为空",
            trigger: "blur"
          }
        ],
        newpassword: [
          {
            required: true,
            message: "新密码不能为空",
            trigger: "blur"
          }
        ],
        repassword: [
          {
            required: true,
            message: "确认密码不能为空",
            trigger: "blur"
          }
        ]
      }
    };
  },
  mounted() {
    let obj = this.parents.userInfo
    this.username = obj.username
    console.log(this.username)
  },
  methods: {
    // 修改密码
    addPost() {
      console.log(this.username)
      this.$refs["ruleForm"].validate(valid => {
        if (valid) {
          if (this.ruleForm.newpassword != this.ruleForm.repassword) {
            this.$message.error("两次密码输入不一致");
            return;
          }else{
        console.log(this.username,
             this.ruleForm.password,
         this.ruleForm.newpassword)
        this.$axios({
          method: 'GET',
          url: 'http://127.0.0.1:8000/api/modify_password/',
          params: {
            username: this.username,
            old_password: this.ruleForm.password,
            new_password: this.ruleForm.newpassword
          }
        }).then(
          res => {
            console.log(res.data)
            if(res.data.status==0){
              this.$message({
                type: 'error',
                message: res.data.message
            })}else if(res.data.status==1){
              this.$message({
                type: 'success',
                message: res.data.message
              })
            }else{
              this.$message(
                {
                  message: res.data.message
                }
              )
            }
          }

        )
          }

        }
      });

    },

    cancel() {
      this.$emit('ActiveIndex', "userInfo")
    }

  }
};
</script>

<style>
el-form {
  background-color: transparent;
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

.detail-form-content {
  position: absolute;
  left: 20%;
  top: 40%;
  width: 400px;
  transform: translate3d(-50%, -50%, 0);
  height: 400px;
  border-radius: 8px;
}
</style>