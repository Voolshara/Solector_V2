<template>
  <div class="wrapper">
    <NavEl />
    <router-view />
    <Footer />
  </div>
</template>

<script>
import NavEl from "./components/nav.vue";
import Footer from "./components/footer.vue";

export default {
  name: "App",
  components: {
    NavEl,
    Footer,
  },
};
</script>

<style>
.wrapper {
  display: flex;
  flex-direction: column;
}

:root {
  --global-background: rgb(255, 255, 255);
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  background-color: var(--global-background);
  /* background-color: #faf6f3; */
  flex-direction: column;
  color: #2c3e50;
  margin: 0 auto;
  padding: 0;
}
</style>
