<template>
  <div class="marketplace">
    <Filters class="filters" v-on:updateValue="get_data" />
    <div class="main_space">
      <div class="container">
        <div v-for="(item, index) in marketplace_data" :key="index">
          <router-link
            class="routes-link"
            :to="'/product/panel/' + item['link_name']"
          >
            <ProductList :data="item" />
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Filters from "@/components/filter/marketplace_filters.vue";
import ProductList from "@/components/product_list";
export default {
  components: {
    Filters,
    ProductList,
  },
  data() {
    return {
      marketplace_data: [],
    };
  },
  methods: {
    get_data(variable) {
      this.marketplace_data = variable;
    },
  },
};
</script>

<style lang="scss">
.routes-link {
  text-decoration: none;
}
.container {
  width: 1000px;
  margin-top: 40px;
  margin-left: 70px;

  display: grid;
  grid-template-columns: 320px 320px 320px;
  align-items: center;
}
.marketplace {
  display: flex;
  flex-direction: row;
  align-self: center;
  margin-bottom: 40px;
}
</style>
