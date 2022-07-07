<template>
  <div class="landing">
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
  <div class="dialog">
    <div class="user_bubble message_1">Зачем мне солнечные панели?</div>
    <div class="solector_bubble message_2">На данный момент целесообразно <br>использовать солненчые панели для следующих целей:</div>
    <div class="solector_bubble message_3">1) Автономное бесперебойное энергоснабжение объектов.</div>
    <div class="solector_bubble message_4">Это актуально для 70% территорий России, имеющих проблемы с энергоснабжением.</div>
    <div class="solector_bubble message_5">2) Заработок на микрогенерации или экономия средств для физическими лицами.</div>
    <div class="solector_bubble message_6">Заработать на продаже лишней электроэнергии в сеть возможно в 33 регионах России.</div>
    <div class="solector_bubble message_7">3) Экономия средств на счетах за электроэнергию для организаций.</div>
    <div class="solector_bubble message_8">Использование солненчых панелей для эконмии средств возможно во всех регионов России, кроме Иркутской области.</div>
    <div class="user_bubble message_9">Насколько целесообразно покупать солненчые панели с экологической точки зрения? Многие источники утверждают, что солнечные панели загрязняю природу сильнее, чем традиционные источники энергии.</div>
    <div class="solector_bubble message_10">Это было верно лишь на ранних этапах производства солненчх панелей. Современные солнечные панели намного более экологичны, чем их предшественники.</div>
  </div>
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

    .text {
      flex-grow: 1;
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

.dialog{
  margin: 100px;

  .user_bubble {
    margin: 40px;
    padding: 10px;
    position: relative;
    background: #6678ff;
    color: #FFFFFF;
    font-family: "Montserrat", sans-serif;
    font-size: 25px;
    // line-height: 120px;
    text-align: left;
    // width: 410px;
    // height: 129px;
    border-radius: 10px;
  } 
  
  .user_bubble:after {
    content: '';
    position: absolute;
    display: block;
    width: 0;
    z-index: 1;
    border-style: solid;
    border-width: 31px 26px 0 0;
    border-color: #6678ff transparent transparent transparent;
    bottom: -31px;
    left: 25%;
    margin-left: -13px;
  }
   
  .solector_bubble {
    margin: 40px;
    padding: 10px;
    position: relative;
    background: #84eb92;
    color: #FFFFFF;
    font-family: Arial;
    font-size: 25px;
    // line-height: 120px;
    text-align: left;
    // width: 487px;
    // height: 129px;
    border-radius: 10px;
    // padding: 0px;
    margin-left: 600px;
  }
  .solector_bubble:after {
      content: '';
      position: absolute;
      display: block;
      width: 0;
      z-index: 1;
      border-style: solid;
      border-width: 0 26px 31px 0;
      border-color: transparent #84eb92 transparent transparent;
      bottom: -31px;
      left: 75%;
      margin-left: -13px;
  }
  .message_1{
      height: 40px;
      width: 410px;
  }
  .message_2{
      height: 90px;
      width: 410px;
  }
  .message_3{
      height: 60px;
      width: 410px;
  }
  .message_4{
      height: 90px;
      width: 410px;
  }
  .message_5{
      height: 90px;
      width: 410px;
  }
  .message_6{
      height: 90px;
      width: 410px;
  }
  .message_7{
      height: 60px;
      width: 410px;
  }
  .message_8{
      height: 120px;
      width: 410px;
  }
  .message_9{
      height: 250px;
      width: 410px;
  }
  .message_10{
      height: 150px;
      width: 410px;
  }
}
}

</style>
