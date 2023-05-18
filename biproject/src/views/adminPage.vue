<template>
  <el-container style="height:100vh; border: 1px solid #eee">
    <el-aside width="200px">
      <div class="headPicture">
        <el-avatar shape="circle" :size="80" :fit="contain" :src="imgUrl">
        </el-avatar>
        <span style="padding-top: 15px; display: block; font-size: 15px; color: #333;">{{ userInfo.username }}</span>
      </div>
      <el-menu>
        <el-submenu index="1" @click.native="changeActiveIndex('initFlag')">
          <template slot="title"><i class="el-icon-s-home"></i>首页</template>
        </el-submenu>

        <el-submenu index="2">
          <template slot="title">
            <div @click="changeActiveIndex('userInfo')"><i class="el-icon-s-custom"></i>用户中心</div>
          </template>
          <el-menu-item-group>
            <template slot="title">个人信息</template>
            <el-menu-item index="2-1" @click="changeActiveIndex('updatePWD')">修改密码</el-menu-item>
            <el-menu-item index="2-2" @click="AddorUpdate('Update1', userInfo)">修改信息</el-menu-item>
          </el-menu-item-group>
        </el-submenu>

        <el-submenu index="3">
          <template slot="title"><i class="el-icon-s-opportunity"></i>功能</template>
          <el-menu-item-group>
            <template slot="title">分组一</template>
            <el-menu-item index="3-1" @click="changeActiveIndex('userManage')">用户管理</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <el-submenu index="4" @click.native="changeActiveIndex('undeveloped')">
          <template slot="title"><i class="el-icon-help"></i>帮助</template>
          <el-menu-item-group>
            <template slot="title">指导手册</template>
            <el-menu-item index="4-1">问题1</el-menu-item>
            <el-menu-item index="4-2">问题2</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
      </el-menu>
    </el-aside>

    <el-container>
      <el-header style="text-align: right; font-size: 15px">
        <span style="margin-right: 15px;">{{ userInfo.username }}</span>
        <el-dropdown>
          <i class="el-icon-arrow-down" style="margin-right: 10px">
          </i>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item @click.native="exit()">退出登录</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </el-header>

      <el-main>
        <div class="bg">
          <template v-if="activeIndex == 'initFlag'">
            <el-calendar v-model="calendar">
            </el-calendar>
          </template>

          <template v-if="activeIndex == 'userInfo'">
            <el-descriptions class="margin-top" title="用户信息" :column="3" border>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-user"></i>
                  用户名
                </template>
                {{ userInfo.username }}
              </el-descriptions-item>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-mobile-phone"></i>
                  手机号
                </template>
                {{ userInfo.phoneNumber }}
              </el-descriptions-item>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-location-outline"></i>
                  居住地
                </template>
                {{ userInfo.city }}
              </el-descriptions-item>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-tickets"></i>
                  备注
                </template>
                <el-tag size="small">{{ userInfo.remark }}</el-tag>
              </el-descriptions-item>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-message"></i>
                  邮箱
                </template>
                {{ userInfo.mailAddress }}
              </el-descriptions-item>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-office-building"></i>
                  通讯地址
                </template>
                {{ userInfo.Address }}
              </el-descriptions-item>
            </el-descriptions>
          </template>

          <template v-if="activeIndex == 'userManage'">
            <el-button size="mini" type="primary" icon="el-icon-plus" @click="AddorUpdate('Add', {})"
              style="margin-bottom: 10px;">新增
            </el-button>
            <el-table :data="userList" border style="width: 100% ；text-align: center">
              <el-table-column label="序号" type="index" width="80px" align="center">
                <template slot-scope="scope">
                  <span>{{ scope.$index + 1 }}</span>
                </template>
              </el-table-column>
              <el-table-column prop="username" label="用户名" width="100">
              </el-table-column>
              <el-table-column prop="city" label="居住地" width="120">
              </el-table-column>
              <el-table-column prop="mailAddress" label="邮箱" width="150">
              </el-table-column>
              <el-table-column prop="Address" label="地址" width="300">
              </el-table-column>
              <el-table-column prop="phoneNumber" label="手机号" width="120">
              </el-table-column>
              <el-table-column prop="remark" label="备注" width="120">
              </el-table-column>
              <el-table-column fixed="right" label="操作" width="180">
                <template slot-scope="scope">
                  <el-button size="mini" type="primary" icon="el-icon-edit"
                    @click="handleEdit(scope.$index)">编辑</el-button>
                  <el-button size="mini" type="danger" icon="el-icon-delete"
                    @click="handleDelete(scope.$index)">删除</el-button>
                </template>
              </el-table-column>
            </el-table>
          </template>

          <template v-if="activeIndex == 'undeveloped'">

          </template>

          <template v-if="activeIndex == 'Update1'">
            <AddorUpdate :parents="this" @ActiveIndex="ActiveIndex($event)"></AddorUpdate>
          </template>
          <template v-if="activeIndex == 'Update2'">
            <AddorUpdate :parents="this" @ActiveIndex="ActiveIndex($event)"></AddorUpdate>
          </template>

          <template v-if="activeIndex == 'Add'">
            <AddorUpdate :parents="this" @ActiveIndex="ActiveIndex($event)"></AddorUpdate>
          </template>

          <template v-if="activeIndex == 'updatePWD'">
            <UpdatePWD :parents="this" @ActiveIndex="ActiveIndex($event)"></UpdatePWD>
          </template>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import imgUrl from "../assets/admin.jpg"
import AddorUpdate from "@/components/add-or-update"
import UpdatePWD from "@/components/update_pwd"

export default {
  components: {
    'AddorUpdate': AddorUpdate,
    'UpdatePWD': UpdatePWD,
  },
  data() {
    return {
      activeIndex: '',
      userInfo: {
        username: '',
        phoneNumber: '',
        mailAddress: '',
        city: '',
        Address: '',
        remark: '',
      },
      userList: [], //用户信息表
      imgUrl: imgUrl,
      calendar: new Date(),
      response: {},
      obj: {},
      opt: ''
    };
  },
  created() {
    this.activeIndex = 'InitFlag'
  },
  mounted() {
    let res1 = this.$route.query.username
    this.$axios({
      method: 'GET',
      url: 'http://127.0.0.1:8000/api/get_information/',
      params: {
        username: res1
      }
    }).then(
      res => {
        console.log(res.data.data)
        this.response = res.data.data
        this.userInfo.username = this.response[1]
        this.userInfo.phoneNumber = this.response[5]
        this.userInfo.mailAddress = this.response[3]
        this.userInfo.city = this.response[2]
        this.userInfo.Address = this.response[4]
        this.userInfo.remark = this.response[6]
      })


    this.$axios({
      method: 'GET',
      url: 'http://127.0.0.1:8000/api/fillInForm/',
    }).then(
      res => {
        console.log(res.data.message)
        let res2 = res.data.message
        console.log(res2.length)
        for (let i = 0; i < res2.length; i++) {
          let res3 = res2[i]
          let obj1={}
          obj1.username = res3[1]
          obj1.phoneNumber = res3[5]
          obj1.mailAddress = res3[3]
          obj1.city = res3[2]
          obj1.Address = res3[4]
          obj1.remark = res3[6]
          console.log(obj1)
          this.userList.push(obj1)
        }

      }
    )
  },

  methods: {
    changeActiveIndex(s) {
      /*
      通过参数s改变activeIndex改变页面内容
      */

      this.activeIndex = s
      console.log(this.activeIndex)

    },

    exit() {
      this.$router.push({ path: '/login' })
    },
    ActiveIndex(msg) {
      this.activeIndex = msg
    },
    AddorUpdate(opt, obj) {
      //把第二个参数传递给相应的组件进行渲染
      this.changeActiveIndex(opt)
      this.opt = opt
      this.obj = obj

    },
    handleEdit(index) {
      let obj = this.userList[index]
      console.log(obj)
      this.AddorUpdate('Update2', obj)
    },

    handleDelete(index) {
      this.$confirm('此操作将永久删除该用户, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$axios({
          method: 'GET',
          url: 'http://127.0.0.1:8000/api/modify_information',
          params: {
            username: this.userList[index].username,
            phoneNumber: !this.userList[index].phoneNumber?'':this.userList[index].phoneNumber,
            mailAddress: !this.userList[index].mailAddress?'':this.userList[index].mailAddress,
            city: !this.userList[index].city?'':this.userList[index].city,
            Address: !this.userList[index].Address?'':this.userList[index].Address,
            remark: !this.userList[index].remark?'':this.userList[index].remark,
            action: 'del'

          }
        }).then(
          res => {
            console.log(res)
            if(res.data.status==1){
              this.$message(
                {
                  type:'success',
                  message:res.data.message
                }
              )
            }else{
              this.$message(
                {
                  message:res.data.message
                }
              )
            }
          }
        )
        
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        });
      });

    },
  }
};
</script>
  
<style>
.el-header {
  background-color: rgba(208, 235, 245, 0.8);
  color: #333;
  line-height: 60px;
}

.el-menu {
  background-color: rgba(208, 235, 245, 0.1);
}

.el-aside {
  background-color: rgba(208, 235, 245, 0.8);
  color: #333;
  height: 100vh;
}

.headPicture {
  padding: 60px 45px;
}

.el-main {
  height: 100vh;
  background: url("../assets/bg2.jpg") center center no-repeat;
  background-size: 100% 100%;
  position: relative;
}

.bg {
  opacity: 0.8;
}
</style>
  
  
    