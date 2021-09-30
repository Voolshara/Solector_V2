<template>
  <div class="promo">
    <div class="text">
      <p class="animate__animated animate__fadeInUp animate__delay-1s">
        Solector
      </p>
      <p class="animate__animated animate__fadeInUp animate__delay-2s">
        Сервис для удобного выбора солнечных модулей и сопутствующего
        оборудования
      </p>
      <a class="animate__animated animate__fadeInUp animate__delay-3s"
        ><p>Попробовать</p></a
      >
      <img
        src="/img/social_network.svg"
        class="animate__animated animate__fadeInUp animate__delay-3s"
      />
    </div>
    <img
      class="img animate__animated animate__fadeInRight"
      src="/img/promo.svg"
    />
  </div>
</template>

<style lang="scss">
:root {
  --global-background: #faf6f3;
}
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@400&display=swap");
.promo {
  margin-top: 40px;
  margin-bottom: 40px;
  display: flex;
  text-align: center;
  @media (max-width: 720px) {
    flex-direction: column;
  }

  .text {
    flex-grow: 2;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    :nth-child(1) {
      font-family: "Montserrat", sans-serif;
      font-size: 108px;
      letter-spacing: 0.1em;
      font-weight: 400;
      color: black;
      margin: 20px;
    }
    :nth-child(2) {
      font-family: "Montserrat", sans-serif;
      width: 500px;
      font-size: 22px;
      line-height: 22px;
      letter-spacing: 0.05em;
      color: black;
    }
    :nth-child(3) {
      p {
        font-family: "Montserrat", sans-serif;
        font-size: 18px;
        padding: 20px;
        width: 200px;

        border: 3px solid #fc7061;
        border-radius: 20px;
      }
      p:hover {
        background-color: #fc7061;
      }
    }
  }

  .img {
    flex-grow: 1;
  }
}
</style>
