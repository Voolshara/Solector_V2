<template>
  <div>
    <el-collapse class="filter">
      <el-collapse-item class="filter-element" title="Бренды" name="1">
        <div class="filter-content">
          <BrandFilter :brands="this.brands" />
        </div>
      </el-collapse-item>
      <el-collapse-item class="filter-element" title="Напряжение" name="2">
        <div>к</div>
      </el-collapse-item>
    </el-collapse>
  </div>
</template>

<script>
import BrandFilter from "@/components/filter/brand.vue";
export default {
  components: { BrandFilter },
  data() {
    return {
      brands: ["r", "t"],
    };
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@400&display=swap");
:root {
  --global-background: rgb(255, 255, 255);
}

.filter-element {
  margin-left: 20px;
}

.filter {
  width: 270px;
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
</style>
