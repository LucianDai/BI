<!-- 热销商品图表 -->
<template>
  <div class='com-container'>
    <div class="title" :style="comStyle">

      <span @click="changeBarflag('year')">{{ '▎ 年专利数量对比' }}</span>
      <span class="iconfont title-icon" :style="comStyle" @click="showChoice = !showChoice">&#xe6eb;</span>
      <div class="select-con" v-show="showChoice" :style="marginStyle">
        <div @click="changeBarflag('month')" class="select-item">
          月专利数量对比
        </div>

      </div>
    </div>
    <div class='com-chart' ref='hot_ref'></div>

  </div>
</template>
<script>
import { mapState } from 'vuex'
import { getThemeValue } from '@/utils/theme_utils'

export default {
  data() {
    return {
      chartInstance: null,
      showChoice: false,
      allData: [],
      // currentIndex: 0, // 当前所展示出的一级分类数据
      titleFontSize: 0,
      barFlag: 'year',
      company1: '',
      company2: '',

    }
  },
  // created () {
  //   // 在组件创建完成之后 进行回调函数的注册
  //   this.$socket.registerCallBack('hotData', this.getData)
  // },
  computed: {
    catName() {
      if (!this.allData) {
        return ''
      } else {
        return this.allData[this.currentIndex].name
      }
    },
    comStyle() {
      return {
        fontSize: this.titleFontSize + 'px',
        color: getThemeValue(this.theme).titleColor
      }
    },
    marginStyle() {
      return {
        marginLeft: this.titleFontSize + 'px'
      }
    },
    ...mapState(['theme'])
  },
  mounted() {
    this.company1 = this.$route.query.company1
    this.company2 = this.$route.query.company2
    console.log(this.company1)
    console.log(this.company2)
    this.initChart()
    this.getData()
    window.addEventListener('resize', this.screenAdapter)
    this.screenAdapter()

  },
  destroyed() {
    window.removeEventListener('resize', this.screenAdapter)
    // this.$socket.unRegisterCallBack('hotData')
  },
  methods: {
    changeBarflag(flag) {
      console.log('this.barFlag', this.barFlag)
      this.barFlag = flag;
      this.updateChart()
    },
    calculateSum(arr) {
      let sum = 0;

      for (let i = 0; i < arr.length; i++) {
        if (typeof arr[i] === 'number') { // 确保当前元素是数字
          sum += arr[i];
        }
      }

      return sum;
    },
    initChart() {
      this.chartInstance = this.$echarts.init(this.$refs.hot_ref, this.theme)
      const initOption = {
        legend: {
          top: '15%',
          icon: 'circle'
        },
        tooltip: {

          trigger: 'axis'
        },
        toolbox: {
          show: true,
          feature: {
            dataView: { show: true, readOnly: false },
            magicType: { show: true, type: ['line', 'bar'] },
            restore: { show: true },
            saveAsImage: { show: true }
          }
        },
        calculable: true,
        xAxis: [
          {
            type: 'category',
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
        ]
      }
      this.chartInstance.setOption(initOption)
    },

    getData() {
      let that = this
      this.$axios({
        method: 'GET',
        url: "http://127.0.0.1:8000/api/keshihua/keshihua/",
        params: {
          company1: this.company1,
          company2: this.company2
        }
      }).then(res => {
        this.allData = res.data.data
        console.log("this.allData", this.allData)
        that.updateChart()
      })
    },
    updateChart() {
      let nameList = [];
      let monthlyTotals1 = [];
      let monthlyTotals2 = [];
      let yearTotals1 = [];
      let yearTotals2 = [];
      for (let index = 0; index < 2; index++) {
        nameList.push(this.allData[index].name);
      }
      monthlyTotals1 = this.allData[0].value
      monthlyTotals2 = this.allData[1].value
      for (let index1 = 2; index1 < 26; index1 += 2) {
        yearTotals1.push(this.allData[index1].value)
      }
      for (let index1 = 3; index1 < 26; index1 += 2) {
        yearTotals2.push(this.allData[index1].value)
      }

      const dataOption2 = {
        legend: {
          data: nameList
        },
        xAxis: [
          {
            data: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
          }
        ],
        series: [
          {
            name: nameList[0],
            type: 'bar',
            data: monthlyTotals1,
            markPoint: {
              data: [
                { type: 'max', name: 'Max' },
                { type: 'min', name: 'Min' }
              ]
            },
            markLine: {
              data: [{ type: 'average', name: 'Avg' }]
            }
          },
          {
            name: nameList[1],
            type: 'bar',
            data: monthlyTotals2,
            markPoint: {
              data: [
                { type: 'max', name: 'Max' },
                { type: 'min', name: 'Min' }
              ]
            },
            markLine: {
              data: [{ type: 'average', name: 'Avg' }]
            }
          }
        ]
      }
      const dataOption1 = {
        legend: {
          data: nameList
        },
        xAxis: [
          {
            data: ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
          }
        ],
        series: [
          {
            name: nameList[0],
            type: 'bar',
            data: yearTotals1,
            markPoint: {
              data: [
                { type: 'max', name: 'Max' },
                { type: 'min', name: 'Min' }
              ]
            },
            markLine: {
              data: [{ type: 'average', name: 'Avg' }]
            }
          },
          {
            name: nameList[1],
            type: 'bar',
            data: yearTotals2,
            markPoint: {
              data: [
                { type: 'max', name: 'Max' },
                { type: 'min', name: 'Min' }
              ]
            },
            markLine: {
              data: [{ type: 'average', name: 'Avg' }]
            }
          }
        ]
      }
      if (this.barFlag == 'year') {
        this.chartInstance.setOption(dataOption1)
      } else {
        this.chartInstance.setOption(dataOption2)
      }
    },
    screenAdapter() {
      this.titleFontSize = this.$refs.hot_ref.offsetWidth / 100 * 3.6
      const adapterOption = {
        title: {
          textStyle: {
            fontSize: this.titleFontSize
          }
        },
        legend: {
          itemWidth: this.titleFontSize,
          itemHeight: this.titleFontSize,
          itemGap: this.titleFontSize / 2,
          textStyle: {
            fontSize: this.titleFontSize / 2
          }
        },
        series: [
          {
            radius: this.titleFontSize * 4.5,
            center: ['50%', '60%']
          }
        ]
      }
      this.chartInstance.setOption(adapterOption)
      this.chartInstance.resize()
    },

  },
  watch: {
    theme() {
      console.log('主题切换了')
      this.chartInstance.dispose() // 销毁当前的图表
      this.initChart() // 重新以最新的主题名称初始化图表对象
      this.screenAdapter() // 完成屏幕的适配
      this.updateChart() // 更新图表的展示
    }
  }
}
</script>

<style lang='less' scoped>
.arr-left {
  position: absolute;
  left: 10%;
  top: 50%;
  transform: translateY(-50%);
  cursor: pointer;
  color: white;
}

.arr-right {
  position: absolute;
  right: 10%;
  top: 50%;
  transform: translateY(-50%);
  cursor: pointer;
  color: white;
}

.cat-name {
  position: absolute;
  left: 80%;
  bottom: 20px;
  color: white;
}

.title {
  position: absolute;
  left: 20px;
  top: 20px;
  z-index: 10; //层级关系
  color: white;

  .title-icon {
    margin-left: 10px;
    cursor: pointer;
  }

  .select-con {
    background-color: #222733;
  }
}
</style>
