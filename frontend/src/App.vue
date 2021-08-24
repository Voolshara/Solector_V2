<template>
  <div class="wrapper">
    <nav-el />
    <router-view />
    <Footer/>
  </div>
</template>

<script>
import NavEl from "./components/nav.vue";
import Footer from "./components/footer.vue";

export default {
  name: "App",
  components: {
    NavEl,
    Footer
  },
};
</script>

<style>
.wrapper {
  display: flex;
  flex-direction: column;
}
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
