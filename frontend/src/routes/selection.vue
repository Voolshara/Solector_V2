<template>
  <div class="container">
    <div class="input">
      <div class="calculate-type">
        <a v-on:click="set_device()" href="#"
          ><div :class="device_css">По электроприборам</div></a
        >
        /
        <a v-on:click="set_energy()" href="#">
          <div :class="energy_css">По энергопотреблению</div>
        </a>
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
        <Energy v-if="energy_css === 'active'" />
        <Devices v-else />
      </div>
      <Map class="yandex-map" />
    </div>

    <div class="output">output</div>
  </div>
</template>

<script>
import Map from "@/components/selection/map";
import Energy from "@/components/selection/energy";
import Devices from "@/components/selection/devices";
export default {
  components: { Map, Energy, Devices },
  data() {
    return {
      device_css: "",
      energy_css: "",
      search: "",
      coords: [],
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
</style>
