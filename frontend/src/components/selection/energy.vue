<template>
  <div class="energy">
    <div class="value">
      Энергопотребление
      <el-input
        class="number"
        v-model="energy_value"
        placeholder="Type something"
        prefix-icon="el-icon-eleme"
        :type="'number'"
        v-on:change="new_value"
      >
        <template #append>
          <el-select
            v-model="energy_type"
            placeholder="кВт"
            style="width: 100px"
          >
            <el-option label="кВт/ч" value="1"></el-option>
            <!-- <el-option label="Вт" value="2"></el-option> -->
          </el-select>
        </template>
      </el-input>
    </div>
    <div class="stock">
      Запас при подборе
      <div class="min-max">
        <div>
          1.0
        </div>
        <div class="slider-demo-block">
          <el-slider
            class="slider"
            v-model="stock_value"
            :min="10"
            :max="20"
            :format-tooltip="formatTooltip"
            v-on:change="new_value"
          >
          </el-slider>
        </div>
        <div>
          2.0
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      energy_value: 2,
      energy_type: "кВт",
      stock_value: 12,
    };
  },
  methods: {
    formatTooltip(val) {
      return val / 10;
    },
    new_value: function() {
      this.$emit("new_value", {
        type: "energy",
        energy: this.energy_value,
        stock_value: this.stock_value / 10,
      });
    },
  },
};
</script>

<style lang="scss">
.energy {
  width: 40vw;
  height: 350px;
  background-color: var(--elements-background);
  border-radius: 15px;

  display: flex;
  justify-content: space-evenly;
  align-items: center;
  flex-direction: column;

  font-family: Lato;
  font-style: normal;
  font-weight: 600;
  font-size: 24px;
  line-height: 22px;
  color: #000;

  .value {
    height: 100px;
    width: 100%;

    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-direction: row;

    .number {
      width: 50%;
      text-align: center;
    }
  }

  .stock {
    display: flex;
    justify-content: space-around;
    align-items: center;
    text-align: center;
    flex-direction: row;
    height: 80px;
    width: 100%;

    .min-max {
      font-size: 60%;
      display: flex;
      flex-direction: row;
      align-items: center;

      .slider {
        width: 325px;
        margin-left: 15px;
        margin-right: 15px;
        --el-slider-height: 4px;
        --el-slider-button-wrapper-offset: -17px;
        --el-slider-main-background-color: var(--main-color);
      }
    }
  }
}
</style>
