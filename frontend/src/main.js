import { createApp } from "vue";
import App from "./App.vue";
import ElementPlus from "element-plus";
import "./element-variables.scss";
import router from "./router";
import "animate.css";

const app = createApp(App);
app.use(ElementPlus);
app.use(router);
app.mount("#app");
