<!-- 商家销量统计的横向柱状图 -->
<template>
  <div class="com-container">
    <div class="com-chart" ref="seller_ref"></div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  data() {
    return {
      chartInstance: null,
      allData: null, // 服务器返回的数据
      company1: '',
      company2: ''
    }
  },

  mounted() {
    this.company1 = this.$route.query.company1
    this.company2 = this.$route.query.company2
    this.initChart()
    this.getData()
    window.addEventListener('resize', this.screenAdapter)
    // 在页面加载完成的时候, 主动进行屏幕的适配
    this.screenAdapter()
  },
  destroyed() {
    clearInterval(this.timerId)
    // 在组件销毁的时候, 需要将监听器取消掉

  },
  methods: {
    // 初始化echartInstance对象
    initChart() {
      this.chartInstance = this.$echarts.init(this.$refs.seller_ref, this.theme)
      // 对图表初始化配置的控制
      const initOption = {
        title: {
          text: '▎综合指标对比',
          left: 20,
          top: 20
        },

        color: ['red', 'yellow'],
        legend: {
          top: '15%',
          icon: 'circle'
        },
        grid: {
          top: '20%',
          left: '3%',
          right: '6%',
          bottom: '3%',
          containLabel: true // 距离是包含坐标轴上的文字
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'line',
            z: 0,
            lineStyle: {
              color: '#2D3443'
            }
          }
        },
        series: [
          {
            type: 'radar',
            label: {
              show: true,
              position: 'right',
              textStyle: {
                color: 'white'
              }
            },
          }
        ]
      }
      this.chartInstance.setOption(initOption)
      // 对图表对象进行鼠标事件的监听
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
    // 更新图表
    updateChart() {
      let nameList = [];
      let value1 = [];//雷达公司一数据
      let value2 = [];//雷达公司二数据
      for (let index = 0; index < 2; index++) {
        nameList.push(this.allData[index].name);
      }

      for (let index = 22; index < 30; index += 2) {
        value1.push(this.allData[index].value);
      }
      // console.log('value1', Array.from(value1))
      for (let index = 23; index < 30; index += 2) {
        value2.push(this.allData[index].value);
      }
      console.log('value1', value1)
      console.log('value2', value2)

      const dataOption = {
        legend: {
          data: nameList
        },
        radar: {
          // shape: 'circle',
          indicator: [
            { name: '专利数量', max: 100 },
            { name: '项目数量', max: 20 },
            { name: '支持资金数量', max: 200000 },
            { name: '项目收入', max: 280000 },

          ]
        },
        series: [
          {
            data: [
              {
                value: value1,
                // value: [72, 5, 33000, 53678],
                name: nameList[0]
              },
              {
                value: value2,
                // value: [52, 5, 186500, 250414],
                name: nameList[1]
              }
            ]
          }
        ]
      }
      this.chartInstance.setOption(dataOption)
    },
    startInterval() {
      if (this.timerId) {
        clearInterval(this.timerId)
      }
      this.timerId = setInterval(() => {
        this.currentPage++
        if (this.currentPage > this.totalPage) {
          this.currentPage = 1
        }
        this.updateChart()
      }, 3000)
    },
    // 当浏览器的大小发生变化的时候, 会调用的方法, 来完成屏幕的适配
    screenAdapter() {
      // console.log(this.$refs.seller_ref.offsetWidth)
      const titleFontSize = this.$refs.seller_ref.offsetWidth / 100 * 3.6
      // 和分辨率大小相关的配置项
      const adapterOption = {
        title: {
          textStyle: {
            fontSize: titleFontSize
          }
        },
        tooltip: {
          axisPointer: {
            lineStyle: {
              width: titleFontSize
            }
          }
        },
        legend: {

          textStyle: {
            fontSize: this.titleFontSize / 2
          }
        },
        series: [
          {
            barWidth: titleFontSize,
            itemStyle: {
              barBorderRadius: [0, titleFontSize / 2, titleFontSize / 2, 0]
            }
          }
        ]
      }
      this.chartInstance.setOption(adapterOption)
      // 手动的调用图表对象的resize 才能产生效果
      this.chartInstance.resize()
    }
  },
  computed: {
    ...mapState(['theme'])
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

<style lang="less" scoped></style>
