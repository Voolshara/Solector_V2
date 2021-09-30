<template>
  <div>
    <div v-for="(item, index) in this.brands" :key="index">
      <el-checkbox
        v-model="this.all_checkboxes[item]"
        v-on:change="updateValue"
        :label="item"
        border
        size="medium"
        class="brend-element"
      ></el-checkbox>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      all_checkboxes: {},
    };
  },
  props: {
    brands: Array,
  },
  methods: {
    updateValue: function() {
      this.$emit("updateValue", {
        type: "brands",
        data: this.all_checkboxes,
      });
    },
  },
};
</script>

<style lang="scss">
.brend-element {
  margin: 4px auto;
}
</style>
