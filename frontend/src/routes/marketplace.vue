<template>
  <div class="marketplace">
    <Filters class="filters" />
    <div class="main_space">erhryt</div>
  </div>
</template>

<script>
import Filters from "@/components/marketplace_filters.vue";
export default {
  name: "App",
  components: {
    Filters,
  },
};
</script>

<style lang="scss">
.marketplace {
  display: flex;
  flex-direction: row;
  justify-content: center;
  margin-bottom: 40px;

  .filters {
    flex-grow: 1;
  }

  .main_space {
    flex-grow: 2;
  }
}
</style>
