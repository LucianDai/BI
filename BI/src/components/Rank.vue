<!-- 地区销售排行 -->
<template>
  <div class='com-container'>
    <div class='com-chart' ref='rank_ref'></div>
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
      company2: ''

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
    this.initChart()
    this.getData()
    // this.$socket.send({
    //   action: 'getData',
    //   socketType: 'hotData',
    //   chartName: 'hot',
    //   value: ''
    // })
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
        // title: {
        //   text: '▎ 专利数量占比',
        //   left: 20,
        //   top: 20
        // },
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
            // 是否x轴间隔显示 加上以后就是不间隔显示 不加的话 会自动间隔显示
            // axisLabel: {
            //   interval: 0
            // }
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
      // this.$http.get('/keshihua/keshihua/').then(res => {
      //   this.allData = res.data.data
      //   console.log("this.allData", this.allData)
      //   that.updateChart()
      // })
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
        // console.log(nameList)
      }
      //0
      // for (let index1 = 0; index1 < 12; index1+=2) {
      //   // if(index1)
      //   let sum = this.calculateSum(this.allData[0].value[index1])
      //   monthlyTotals1.push(sum);
      //   // console.log(monthlyTotals1)
      // }
      monthlyTotals1 = this.allData[0].value


      //1
      // for (let index1 = 0; index1 < 12; index1++) {
      //   // if(index1)
      //   let sum = this.calculateSum(this.allData[1].value[index1])
      //   monthlyTotals2.push(sum);
      // }
      //data需要是数组类型
      monthlyTotals2 = this.allData[1].value
      // const arr = monthlyTotals2.map(item => /^\d+$/.test(item) ? parseInt(item) : NaN).filter(item => !isNaN(item));
      // console.log(arr);


      //year
      //0
      for (let index1 = 2; index1 < 26; index1 += 2) {
        yearTotals1.push(this.allData[index1].value)
      }
      console.log('yearTotals1', yearTotals1)
      //1
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
            // data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 2],
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
            // data: [0, 0, 0, 0, 0, 0, 0, 5, 4, 1, 0, 0],
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
    // toLeft() {
    //   this.currentIndex--
    //   if (this.currentIndex < 0) {
    //     this.currentIndex = this.allData.length - 1
    //   }
    //   this.updateChart()
    // },
    // toRight() {
    //   this.currentIndex++
    //   if (this.currentIndex > this.allData.length - 1) {
    //     this.currentIndex = 0
    //   }
    //   this.updateChart()
    // }
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



