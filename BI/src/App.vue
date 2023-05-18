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



