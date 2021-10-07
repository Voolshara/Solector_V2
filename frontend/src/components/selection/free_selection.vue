<template>
  <div class="free">
    <div class="free-input">
      <div class="selection-type">Базовый</div>
      <el-button class="main-button" type="primary" v-on:click="go()" round
        >Подобрать</el-button
      >
    </div>
    <div class="out">
      <div v-if="load_status" class="before-set">
        <el-skeleton :animated="loading" class="image">
          <template #template>
            <el-skeleton-item variant="image" class="image" />
          </template>
        </el-skeleton>
        <el-skeleton :rows="6" :animated="loading" />
      </div>
      <div v-if="!load_status">
        {{ back }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    settings: {},
  },
  data() {
    return {
      load_status: true,
      loading: false,
      back: {},
    };
  },
  methods: {
    go() {
      this.loading = true;
      if (!(this.settings && Object.keys(this.settings).length > 0)) {
        alert("Заполните поля выше");
        this.loading = false;
        return;
      }
      let data = this.settings;
      data["coords"] = document.getElementById("coords").value;

      fetch("http://192.168.43.163:4900/selection/free", {
        method: "POST", // *GET, POS  T, PUT, DELETE, etc.
        mode: "cors", // no-cors, *cors, same-origin
        cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
        credentials: "same-origin", // include, *same-origin, omit
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Private-Network": true,
          // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        redirect: "follow", // manual, *follow, error
        referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(data), // body data type must match "Content-Type" header
      })
        .then((response) => response.json())
        .then((data) => {
          this.back = data;
          this.load_status = false;
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
  },
};
</script>

<style lang="scss">
.free {
  height: 100%;

  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-direction: column;
}

.out {
  height: 300px;

  .before-set {
    display: grid;
    justify-items: center;
    grid-template-columns: 20vw 35vw;

    .image {
      width: 13vw;
      height: 13vw;
    }
  }
}

.free-input {
  display: grid;
  justify-items: center;
  grid-row-gap: 5px;

  .selection-type {
    font-family: Lato;
    font-style: normal;
    font-weight: 600;
    font-size: 32px;
    line-height: 0;
  }

  .main-button {
    width: 500px;
    height: 50px;
    margin: 40px;
  }
}
</style>
