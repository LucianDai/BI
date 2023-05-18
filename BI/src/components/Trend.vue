<!-- 库存销量分析 -->
<template>
  <div class='com-container'>
    <div class="title" :style="comStyle">
      <!-- <span>{{ '▎ ' + showTitle }}</span> -->
      <span>{{ '▎ 项目数量对比' }}</span>
    </div>
    <div class='com-chart' ref='stock_ref'></div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  data() {
    return {
      chartInstance: null,
      allData: null,
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
    this.screenAdapter()
  },
  destroyed() {
    window.removeEventListener('resize', this.screenAdapter)
  },
  methods: {
    initChart() {
      this.chartInstance = this.$echarts.init(this.$refs.stock_ref, this.theme)
      const initOption = {
        title: {
          left: 20,
          top: 20
        },
        tooltip: {
          trigger: 'item'
        },
        color: ['green', 'blue'],
        legend: {
          top: '15%',
          icon: 'circle'
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        series: [
          {
            name: '公司项目数量对比',
            type: 'pie',
            radius: '50%',
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
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
      // this.$http.get('/keshihua/keshihua/').then(res => {
      //   this.allData = res.data.data
      //   console.log("this.allData", this.allData)
      //   that.updateChart()
      // })
    },
    updateChart() {
      const dataOption = {
        series: [
          {
            data: [
              { value: this.allData[24].value, name: this.allData[24].name },
              { value: this.allData[25].value, name: this.allData[25].name },

            ]
          }
        ]
      }
      this.chartInstance.setOption(dataOption)
    },
    screenAdapter() {
      this.titleFontSize = this.$refs.stock_ref.offsetWidth / 100 * 3.6
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
  computed: {

    comStyle() {

    },
    marginStyle() {
      return {
        marginLeft: this.titleFontSize + 'px'
      }
    },
    handleSelect(currentType) {
      this.choiceType = currentType
      this.updateChart()
      this.showChoice = false
    },
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

<style lang="less" scoped>
.title {
  position: absolute;
  left: 20px;
  top: 20px;
  z-index: 10;
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