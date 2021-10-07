<template>
  <div class="container">
    <div class="input">
      <div class="calculate-type">
        <a v-on:click="set_energy()" href="#">
          <div :class="energy_css">По энергопотреблению</div>
        </a>
        /
        <a v-on:click="set_device()" href="#"
          ><div :class="device_css">По электроприборам</div></a
        >
      </div>
      <div>
        <el-input
          class="search"
          v-model="search"
          placeholder="Поиск Адреса"
          prefix-icon="el-icon-search"
        />
      </div>
      <div>
        <Energy v-on:new_value="new_settings" v-if="energy_css === 'active'" />
        <Devices v-else />
      </div>
      <Map class="yandex-map" />
    </div>
    <div class="selection-text">Выберите вариант подбора</div>
    <el-carousel
      class="selection-type"
      height="500px"
      trigger="click"
      :autoplay="false"
    >
      <el-carousel-item v-for="item in 2" :key="item">
        <FreeSelection :settings="settings" v-if="item === 1" />
        <NormalSelection :settings="settings" v-if="item === 2" />
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
import Map from "@/components/selection/map";
import Energy from "@/components/selection/energy";
import Devices from "@/components/selection/devices";
import FreeSelection from "@/components/selection/free_selection";
import NormalSelection from "@/components/selection/normal_selection";
export default {
  components: { Map, Energy, Devices, FreeSelection, NormalSelection },
  data() {
    return {
      device_css: "",
      energy_css: "",
      search: "",
      selection_free: true,
      coords: [],
      settings: {},
    };
  },
  methods: {
    set_device() {
      this.device_css = "active";
      this.energy_css = "";
      this.$router.push("/calculate/devices");
    },
    set_energy() {
      this.energy_css = "active";
      this.device_css = "";
      this.$router.push("/calculate/energy");
    },
    new_settings(val) {
      this.settings = val;
    },
  },
  mounted() {
    if (this.$route.params.type === "devices") {
      this.set_device();
    } else {
      this.set_energy();
    }
  },
  updated() {
    this.coords = document.getElementById("coords").value;
  },
  // updated() {
  //   if (this.$route.params.type === "devices") {
  //     this.set_device();
  //   } else {
  //     this.set_energy();
  //   }
  // },
};
</script>

<style lang="scss" scoped>
.container {
  margin: 40px auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.input {
  display: grid;
  grid-template-columns: 40vw 25vw;
  grid-column-gap: 3vw;
  grid-row-gap: 1em;
  align-items: center;
}
.calculate-type {
  display: flex;
  justify-content: space-evenly;
  font-family: Montserrat;
  font-style: normal;
  font-weight: 500;
  font-size: 1.5vw;
  line-height: 20px;

  a {
    text-decoration: none;
    color: #000;
    position: relative;
  }

  .active {
    border-bottom: 2px solid var(--main-color);
    position: relative;
    padding-bottom: 7px;
  }
}
.search {
  --el-input-background-color: var(--elements-background);
  --el-input-border-color: var(--elements-background);
  --el-input-focus-border: var(--elements-background);
}

.selection-type {
  margin: 40px;
  width: 70vw;
  height: 500px;

  border-radius: 30px;
}

.selection-text {
  font-family: Montserrat;

  padding: 10px;
  border-radius: 15px;
  margin: 40px;
  font-style: normal;
  font-weight: 500;
  font-size: 30px;
  line-height: 37px;
  display: flex;
  align-items: center;
}
</style>
