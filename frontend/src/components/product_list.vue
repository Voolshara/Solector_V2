<template>
  <div class="element">
    <img class="img" :src="data['img']" />
    <div class="info">
      <div>Солнечная панель {{ data["producer"] }}</div>
      <div class="data-power">
        <div>{{ data["name"] }}</div>
        <div>
          <strong> {{ data["power"] }} W </strong>
        </div>
      </div>
      <div class="cost">
        <strong>{{ data["cost"] }}р.</strong>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    data: JSON,
  },
};
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@300&display=swap");

.element {
  width: 255px;
  height: 350px;
  box-shadow: 0 2px 12px 0 rgba(116, 116, 116, 0.5);
  border-radius: 1em;
  margin: 20px auto;

  display: flex;
  align-items: center;
  flex-direction: column;

  .img {
    margin-top: 10px;
    width: 200px;
    height: 230px;
  }

  .info {
    font-family: "Montserrat", sans-serif;
    font-weight: 500;
    font-size: 14px;
    line-height: 20px;

    margin-top: 15px;
    height: 218px;
    display: flex;
    flex-direction: column;

    color: #2f3032;

    .data-power {
      display: flex;
      flex-direction: row;
      justify-content: space-between;
    }

    .cost {
      margin-top: 13px;
    }
  }
}
</style>
