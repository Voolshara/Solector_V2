<template>
  <div>
    {{ this.brands }}
    <div v-for="(item, index) in this.brands" :key="index">
      <el-checkbox v-model="checked1" :label="item"></el-checkbox>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    brands: Array,
  },
};
</script>
