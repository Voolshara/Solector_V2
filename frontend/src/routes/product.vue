<template>
  <div>
    {{ product_data }}
  </div>
</template>

<script>
export default {
  data() {
    return {
      product_data: Object,
    };
  },
  mounted() {
    fetch("http://localhost:4900/product", {
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
      body: JSON.stringify({
        type: this.$route.params.type,
        product: this.$route.params.product_name,
      }), // body data type must match "Content-Type" header
    })
      .then((response) => response.json())
      .then((data) => {
        this.product_data = data;
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  },
};
</script>
