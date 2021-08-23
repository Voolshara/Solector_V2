<template>
  <div>
    <nav-el />
    <router-view />
  </div>
</template>

<script>
import NavEl from "./components/nav.vue";

export default {
  name: "App",
  components: {
    NavEl,
  },
};
</script>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  display: flex;
  flex-direction: column;
  color: #2c3e50;
  margin: 0 auto;
  padding: 0;
}
</style>
