<template>
  <el-container style="height:100vh; border: 1px solid #eee">
    <el-aside width="200px">
      <div class="headPicture">
        <el-avatar shape="circle" :size="80" :fit="contain" :src="headUrl">
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
            <el-menu-item index="3-1" @click="changeActiveIndex('getcompany')">搜索竞争对手</el-menu-item>
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

          <template v-if="activeIndex == 'getcompany'">
            <el-form label-width="100px" class="demo-ruleForm">
              <el-form-item label="竞争对手：" style="font-size: 30px;">
                <el-input class="company" v-model="company" autocomplete="off" placeholder="请输入您要搜索的竞争对手名称"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="submitForm1()">提交</el-button>
                <el-button @click="resetForm1()">重置</el-button>
              </el-form-item>
            </el-form>
          </template>



          <template v-if="activeIndex == 'getResult'">
            <div class="module1">
              <el-card class="box-card">
                <div slot="header" class="clearfix">
                  <span>下游公司</span>
                </div>
                <div class="text item">
                  <div class="box1">
                    <div class="card" v-for="item in DataForm.data.n1">
                      <el-tag @click="inputTag(item)">
                        {{ item }}
                      </el-tag>
                    </div>
                  </div>
                </div>
              </el-card>
              <el-card class="box-card">
                <div slot="header" class="clearfix">
                  <span>同业公司</span>
                </div>
                <div class="text item">
                  <div class="box1">
                    <div class="card" v-for="item in DataForm.data.n2">
                      <el-tag @click="inputTag(item)">
                        {{ item }}
                      </el-tag>
                    </div>
                  </div>
                </div>
              </el-card>
              <el-card class="box-card">
                <div slot="header" class="clearfix">
                  <span>上游公司</span>
                </div>
                <div class="text item">
                  <div class="box1">
                    <div class="card" v-for="item in DataForm.data.n3">
                      <el-tag @click="inputTag(item)">
                        {{ item }}
                      </el-tag>
                    </div>
                  </div>
                </div>
              </el-card>


              <el-form label-width="100px" class="demo-ruleForm">
                <el-form-item label="竞争对手：" style="font-size: 30px;">
                  <el-input class="company" v-model="company2" autocomplete="off" placeholder="请输入您要搜索的竞争对手名称"></el-input>
                </el-form-item>
                <el-form-item>
                  <el-button type="primary" @click="submitForm2()">提交</el-button>
                  <el-button @click="resetForm2()">重置</el-button>
                </el-form-item>
              </el-form>
            </div>
          </template>

          <template v-if="activeIndex == 'getResult2'">  
            <div class="m50">
              <el-table border style="margin-top: 50px;" :data="transData" :show-header="false" :cell-style="changeCellStyle" stripe>
                <el-table-column v-for="(item, index) in transTitle" :label="item" :key="index" align="center">
                    <template slot-scope="scope">
                        {{scope.row[index]}}
                    </template>
                </el-table-column>
              </el-table>
            </div>
            <div class="visual" style="margin-top: 10px;">
              <el-button icon="el-icon-search" type="success" @click="getVisual()" plain>点此访问可视化结果</el-button>
            </div>
          </template>

          <template v-if="activeIndex == 'Update1'">
            <AddorUpdate :parents="this" @ActiveIndex="ActiveIndex($event)"></AddorUpdate>
          </template>

          <template v-if="activeIndex == 'updatePWD'">
            <UpdatePWD :parents="this" @ActiveIndex="ActiveIndex($event)"></UpdatePWD>
          </template>


          <template v-if="activeIndex == 'undeveloped'">
          </template>

        </div>
      </el-main>
    </el-container>
  </el-container>
</template>



<script>
import headUrl from "../assets/coolRobot.jpg"
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
      company: '',
      DataForm: {
        code: 0,
        msg: '',
        data: {
          "n1": [],
          "n2": [],
          "n3": [],
          "company": ''
        }
      },
      DataForm2: {
        "code": 0,
        "msg": "",
        "data": ""
      },
      company2: '',
      companys: [],
      headUrl: headUrl,
      obj: '',
      opt:'',
      calendar: new Date(),
      originData: [],
      originTitle: ['公司名称', '机构类别', '国家名称', '详细地址', '主要产品', '英文名称', '员工数', '公司类型', '上市类型', '法定代表人', '经营范围', '成立日期', '公司网址', '战略合作', '发展历程', '公司简介', '领导'], // originTitle 该标题为 正常显示的标题, 数组中的顺序就是上面数据源对象中的字段标题对应的顺序
      transTitle: ['', '公司1', '公司2'], // transTitle 该标题为转化后的标题, 注意多一列,  因为原来的标题变成了竖着显示了, 所以多一列标题, 第一个为空即可
      transData: []
    };
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


  },

  methods: {
    changeActiveIndex(s) {
      /*
      通过参数s改变activeIndex改变页面内容
      */
      this.activeIndex = s
    },
    ActiveIndex(msg) {
      this.activeIndex = msg
    },
    AddorUpdate(opt, obj) {

      this.changeActiveIndex(opt)
      //把第二个参数传递给相应的组件进行渲染
      this.opt = opt
      this.obj = obj

    },
    getVisual() {
      let url = " http://localhost:8999/screen?" + "company1=" + this.company + "&" + "company2=" + this.company2
      console.log(url)
      window.location.href = url;
    },
    submitForm1() {
      /*
      根据传入相应的公司名称调取相应的接口
       */
      if (!this.company) { //非空校验
        this.$message.error("请输入公司名称！");
        return;
      }
      else {
        this.$axios({
          method: 'GET',
          url: `http://127.0.0.1:8000/api/duishou/chazhao/`,
          params: {
            company1: this.company
          }
        })
          .then(res => {

            this.DataForm = res.data

          })
        this.activeIndex = 'getResult';
      }
    },
    resetForm1() {
      /*
      清空用户输入的内容
       */

      this.company = '';


    },
    submitForm2() {
      if (!this.company2) { //非空校验
        this.$message.error("请输入竞争对手名称！");
        return;
      }
      else {
        this.$axios({
          method: 'GET',
          url: `http://127.0.0.1:8000/api/keshihua/get_list`,
          params: {
            company1: this.company,
            company2: this.company2
          }
        })
          .then(res => {
            this.DataForm2 = res.data
            console.log(this.DataForm2.data.company1, this.DataForm2.data.company2)
            console.log(this.companys)
            this.companys = [].concat(this.DataForm2.data.company1, this.DataForm2.data.company2)
            console.log(this.companys)
            this.originData = [].concat(this.DataForm2.data.company1, this.DataForm2.data.company2) //填充数据 
            let matrixData = this.originData.map((row) => {
              let arr = []
              for (let key in row) {
                arr.push(row[key])
              }
              return arr
            })
            // 加入标题拼接最终的数据
            this.transData = matrixData[0].map((col, i) => {
              return [this.originTitle[i], ...matrixData.map((row) => {
                return row[i]
              })]
            })
          })
      }
      this.changeActiveIndex('getResult2');
      this.$message({
        message: "提交成功，正在为您查询……",
        type: 'success'
      })

    },
    resetForm2() {
      /*
      清空用户输入的内容
       */

      this.company2 = '';


    },
    changeCellStyle({ row, column, rowIndex, columnIndex }) {
      if (columnIndex === 0) {
        /**
         * 通过columnIndex修改对应的列的样式,这里修改的是显示属性名的第一列（columnIndex === 0）
         */
        return "background-color: #d3dbec;color:#71898d; font-size: 15px;"
      }
    },
    inputTag(item) {
      this.company2 = item
    },
    exit() {
      this.$router.push({ path: '/login' })
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
  background-color: rgba(208, 235, 245, 0.8);
}

.el-aside {

  background-color: rgba(208, 235, 245, 0.8);
  color: #333;
  height: 100vh;
}

.headPicture {
  padding: 60px 45px;
}

.el-input.company {
  width: 300px;
}

.box1 {
  display: flex;
}

.card {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: space-between;
  margin-left: 5px;
}

.el-card {
  margin: 10px;
}

.content {
  width: 100%;
}

.yes-sir {
  width: 1000px;
  margin: 30px auto;
  border: solid 1px #eee;
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


  