
module.exports = {
  devServer: {
    port: 8999, //  端口号的配置
    open: false, // 自动打开浏览器
    proxy: {
      '/api': {
        target: 'http://localhost:8000/api',//代理地址，这里设置的地址会代替axios中设置的baseURL
        changeOrigin: true,// 如果接口跨域，需要进行这个参数配置
        ws: true, // proxy websockets
        secure: false, //忽略https安全提示
        //xfwd：false, //添加x-forward标头
        //pathRewrite方法重写url
        pathRewrite: {
          '^/api': ''//重写之后url为 http://localhost:8080/xxxx
        }
        //pathRewrite: {'^/api': '/api'} //重写之后url为 http://localhost:8080/api/xxxx
      }
    }

  }
}
