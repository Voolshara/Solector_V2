<template>
  <nav>
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      v-on:select="handleSelect"
      background-color="var(--global-background)"
      text-color="#2c3e50"
      active-text-color="#FC7061"
      style="border-bottom: 0 solid black;"
    >
      <el-menu-item index="/">О нас</el-menu-item>
      <el-menu-item index="/marketplace">MarketPlace</el-menu-item>
      <el-menu-item index="/forum">Форум</el-menu-item>
      <el-menu-item index="/instruction">Инструкция</el-menu-item>
      <el-submenu index="/calculate">
        <template #title>Подбор</template>
        <el-menu-item index="/calculate/devices"
          >По электроприборам</el-menu-item
        >
        <el-menu-item index="/calculate/energy"
          >По энергопотреблению</el-menu-item
        >
      </el-submenu>
      <el-menu-item index="6"
        ><router-link to="/lk">Войти</router-link></el-menu-item
      >
    </el-menu>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      activeIndex: "/",
    };
  },
  methods: {
    handleSelect(key) {
      this.$router.push(key);
    },
  },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap");
nav {
  font-family: "Montserrat", sans-serif;
  display: flex;
  justify-content: flex-end;
  box-shadow: 0 1px 0 0 rgba(0, 0, 0, 0.2);
  width: 80%;
  align-self: center;

  .el-menu-demo {
    margin: 0;
    margin-top: 30px;
    color: #2c3e50;

    a {
      margin-right: 40px;

      text-decoration: none;
      font-size: 25px;
    }
  }
}
.lk-button {
  width: 150px;
  height: 50px;
}
</style>
