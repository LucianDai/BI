# biproject
本系统主要页面代码在views文件夹下，

1.登录页面 => login.vue
用户需要输入正确的用户名和密码，并选择相应的角色，分为两个角色：（普通）用户和管理员，
从而进入相应的系统功能页面。

2.用户功能页面 => indexStatic.vue
整体分为侧边栏，顶部栏和中心主要板块，部分组件在components文件夹下，分别是add-or-update.vue(对应修改用户信息)和update_pwd.vue（对应修改密码）
核心功能为搜索竞争对手，通过分两次输入公司名称调用后端分析结果展示在前端呈现一个对比表格。

3.管理员功能页面 => adminPage.vue
整体分为侧边栏，顶部栏和中心主要板块，部分组件在components文件夹下，分别是add-or-update.vue(对应修改用户信息)和update_pwd.vue（对应修改密码）

4.页面的跳转通过router文件夹下的index.js，将相应的路径（path）与页面的vue对应上

5.部分重复使用的使用类方法在utils文件夹下，如用户输入的校验（validate.js）、存储方法（storage.js)。

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
