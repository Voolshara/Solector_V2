<template>
  <div>
    <el-collapse class="filter">
      <el-collapse-item class="filter-element" title="Бренды" name="1">
        <div class="filter-content">
          <BrandFilter v-on:updateValue="new_filters" :brands="this.brands" />
        </div>
      </el-collapse-item>
      <el-collapse-item class="filter-element" title="Мощность, Вт" name="2">
        <div>
          <RangeSlider
            v-on:updateValue="new_filters"
            :mi="this.power[0]"
            :ma="this.power[1]"
            :range="2"
            :slider_type="'power'"
            :power_slider="power"
          />
        </div>
      </el-collapse-item>
      <el-collapse-item class="filter-element" title="Стоимость, руб" name="3">
        <div>
          <RangeSlider
            v-on:updateValue="new_filters"
            :mi="this.cost[0]"
            :ma="this.cost[1]"
            :range="100"
            :slider_type="'cost'"
          />
        </div>
      </el-collapse-item>
      <div class="return-filters">
        <button v-on:click="restoreFilters" class="button">
          Сбросить Фильтры
        </button>
      </div>
    </el-collapse>
  </div>
</template>

<script>
import BrandFilter from "@/components/filter/brand.vue";
import RangeSlider from "@/components/filter/range_slider.vue";
// import Loader from "@/components/filter/loader.vue";
export default {
  components: { BrandFilter, RangeSlider },
  data() {
    return {
      brands: ["Hevel Solar"],
      power: [0, 1000000],
      cost: [0, 10000000],
      all_filters: {
        brands: null,
        power: null,
        cost: null,
      },
    };
  },
  methods: {
    new_filters(variable) {
      if (variable !== null) {
        this.all_filters[variable["type"]] = variable["data"];
      }
      fetch("http://192.168.43.163:4900/marketplace/data", {
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
        body: JSON.stringify(this.all_filters), // body data type must match "Content-Type" header
      })
        .then((response) => response.json())
        .then((data) => {
          this.$emit("updateValue", data["data"]);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    restoreFilters() {
      let all_filters = {
        brands: null,
        power: null,
        cost: null,
      };
      this.all_filters = all_filters;
      this.$forceUpdate();
    },
  },
  beforeCreate() {
    fetch("http://192.168.43.163:4900/marketplace/get_filters", {
      method: "POST", // *GET, POST, PUT, DELETE, etc.
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
      body: "", // body data type must match "Content-Type" header
    })
      .then((response) => response.json())
      .then((data) => {
        this.brands = data["brands"];
        this.power = data["power"];
        this.cost = data["cost"];
        this.primary_brands = data["brands"];
        this.primary_power = data["power"];
        this.cost = data["cost"];
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  },
  mounted() {
    this.new_filters(null);
  },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@400&display=swap");
:root {
  --global-background: rgb(255, 255, 255);
}

.filter-element {
  margin-left: 20px;
}

.filter {
  width: 300px;
  background-color: var(--background-color);
  margin: 0 auto;
  margin-top: 40px;
  font-family: "Montserrat", sans-serif;
  font-weight: 500;
  border-radius: 1em;
  box-shadow: 0 2px 12px 0 rgba(116, 116, 116, 0.3);

  --el-collapse-header-background-color: rgba(0, 0, 0, 0);
  --el-collapse-content-background-color: rgba(0, 0, 0, 0);
  --el-collapse-header-font-size: 18px;
}

.return-filters {
  height: 40px;
  display: none;
  align-items: center;
  justify-content: center;
  color: var(--main-color);

  .button {
    background-color: rgba(0, 0, 0, 0);
    border: none;
    color: var(--main-color);
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
  }
  .button:hover {
    color: var(--main-hover);
  }
}
</style>
