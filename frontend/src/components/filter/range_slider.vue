<template>
  <div class="slider">
    <el-slider
      class="ranger"
      v-model="power_slider"
      :step="range"
      :min="mi"
      :max="ma"
      range
      v-on:change="updateValue"
      show-input
      show-input-controls
      :debounce="1"
    >
    </el-slider>
    <div class="power-status">
      От
      <el-input-number
        v-model="power_slider[0]"
        :controls="false"
        v-on:change="updateValue"
        :min="mi"
        :max="ma - 1"
        size="mini"
        class="slider-num"
      >
      </el-input-number>
      До
      <el-input-number
        v-model="power_slider[1]"
        :controls="false"
        v-on:change="updateValue"
        :min="mi + 1"
        :max="ma"
        size="mini"
        class="slider-num"
      >
      </el-input-number>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    mi: Number,
    ma: Number,
    range: Number,
    slider_type: String,
  },
  data() {
    return {
      power_slider: [this.mi, this.ma],
    };
  },

  methods: {
    updateValue: function() {
      this.$emit("updateValue", {
        type: this.slider_type,
        data: this.power_slider,
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.slider {
  width: 80%;
  margin-left: 15px;
}

.power-status {
  display: flex;
  justify-content: space-between;
}

.slider-num {
  width: 70px;
}

.ranger {
  --el-slider-height: 4px;
}
</style>
