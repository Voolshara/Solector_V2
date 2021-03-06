import { createRouter, createWebHistory } from "vue-router";

const routes = [
  { path: "/", component: () => import("@/routes/main_page.vue") },
  { path: "/marketplace", component: () => import("@/routes/marketplace.vue") },
  {
    path: "/product/:type/:product_name",
    component: () => import("@/routes/product.vue"),
  },
  { path: "/feedback", component: () => import("@/routes/feedback_form.vue") },
  { path: "/lk", component: () => import("@/routes/feedback_form.vue") },
  {
    path: "/calculate/:type",
    component: () => import("@/routes/selection.vue"),
  },
];

// 3. Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
const router = createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: createWebHistory(),
  routes, // short for `routes: routes`
});

export default router;
