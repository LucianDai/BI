<template>
  <div id="app" class="">
    <router-view></router-view>
  </div>
</template>

<script>
import { RouterView } from 'vue-router';

export default {
  name: 'app',
  components: {
    RouterView
}
}
</script>


<style>

*{
  padding: 0;
  margin:0;
}
html,body{
  width: 100%;
  height: 100%;
}
#app{
  height:100%;
}
body {
  padding: 0;
  margin: 0;
  
}
</style>
