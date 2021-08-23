<template>
  <div class="nav">
    <ul>
      <li><router-link to="/">О нас</router-link></li>
      <li><router-link to="/marketplace">MarketPlace</router-link></li>
      <li><a href="#">Форум</a></li>
      <li><a href="#">Инструкция</a></li>
      <li><a href="#">Подбор</a></li>
      <li>
        <a href="#">
          <el-row
            ><el-button type="warning" plain round class="lk-button"
              >Войти</el-button
            ></el-row
          >
        </a>
      </li>
    </ul>
  </div>
</template>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap");
.nav {
  font-family: "Montserrat", sans-serif;
  display: flex;
  justify-content: flex-end;

  ul {
    display: flex;
    justify-content: center;
    flex-direction: row;
    align-items: baseline;
    // border-right: 0.5px black solid;
    padding-top: 5px;
    padding-bottom: 5px;
    list-style-type: none;
    margin-right: 40px;

    li a {
      margin-right: 40px;
      color: #2c3e50;
      text-decoration: none;
      font-size: 20px;
    }
    li a:hover {
      border-bottom: 2px rgba(252, 112, 97, 0.8) solid;
    }
  }
}
.lk-button {
  width: 150px;
  height: 50px;
  position: relative;
}
</style>
