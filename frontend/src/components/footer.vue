<template>
  <div class="footer_back">
    <div class="footer_back_adress">
      <div class="footer_back_adress_company_name">Solector</div>
      <div class="footer_back_adress_contacts">
        г.Чебоксары <br />+7 (996) 949 83 08 <br />sta-tun-slav@yandex.ru
      </div>
    </div>

    <div class="footer_back_developers">
      <div class="title">
        Разработчики
        <hr class="footer_line" />
      </div>
      <div class="participant">
        <a href="https://t.me/Sta_Tun_slav" target="_blank">
          <img src="/img/Telegram App.svg" alt="" class="icone" />
          Тунгулов Станислав
        </a>
      </div>

      <div class="participant">
        <a href="https://t.me/Mike_Kad" target="_blank">
          <img src="/img/Telegram App.svg" alt="" class="icone" />
          Кадилов Михаил
        </a>
      </div>
    </div>

    <div class="footer_back_social_networks">
      <div class="footer_back_social_networks_title">
        Социальные сети<br />
        <hr class="footer_line" />
      </div>
      <div class="footer_back_social_networks_blocks">
        <div class="footer_back_social_networks_block_1">
          <a href="https://instagram.com/solector_group/">
            <div class="footer_back_some_social_network">
              <img src="/img/Instagram.svg" alt="" class="icone" />Instagram
            </div>
          </a>

          <a href="https://vk.com/solector">
            <div class="footer_back_some_social_network">
              <img src="/img/VK.com.svg" alt="" class="icone" />VK
            </div>
          </a>

          <a href="https://t.me/Solector_bot/">
            <div class="footer_back_some_social_network">
              <img src="/img/Telegram App.svg" alt="" class="icone" />Telegram
            </div>
          </a>
        </div>

        <div class="footer_back_social_networks_block_2">
          <a href="https://instagram.com/solector_group/">
            <div class="footer_back_some_social_network">
              <img src="/img/gmail.svg" alt="" class="icone" />Вопросы
            </div>
          </a>

          <router-link to="/feedback">
            <div class="footer_back_some_social_network">
              <img src="/img/forms.svg" alt="" class="icone" />FeedBack
            </div>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@200&display=swap");

.footer_back {
  display: flex;
  flex-direction: row;
  justify-content: center;

  min-width: 100%;
  height: 260px;
  background: #151b38;

  color: #ffffff;
  font-family: "Montserrat", sans-serif;

  a {
    color: #ffffff;
    text-decoration: none;
  }

  .icone {
    width: 25px;
    height: 25px;
    margin-right: 15px;
  }
}

.footer_back_adress {
  display: flex;
  flex-direction: column;
  width: 260px;
  margin: 30px;
  margin-top: 60px;
}

.footer_back_adress_company_name {
  font-size: 45px;
  line-height: 44px;
  letter-spacing: 0.1em;
  text-align: left;
  margin-bottom: 5px;
}

.footer_back_adress_contacts {
  text-align: left;
  font-size: 18px;
  margin: 2px;
}

.footer_back_developers {
  width: 260px;
  margin: 30px;
  line-height: 210%;
  display: flex;
  flex-direction: column;

  .title {
    font-weight: 500;
    font-size: 24px;
    line-height: 29px;
    margin-top: 10px;
  }

  .participant,
  a {
    text-align: left;
    display: flex;
    align-items: center;
    margin: 2px;
    font-size: 18px;
    text-decoration: none;
    color: #ffffff;
  }
}

.footer_back_social_networks {
  width: 380px;
  margin: 30px;
}

.footer_back_social_networks_title {
  font-weight: 500;
  font-size: 24px;
  line-height: 29px;
  margin: 10px;
}

.footer_back_social_networks_blocks {
  font-size: 18px;
  line-height: 210%;
  display: flex;
  justify-content: space-around;
}

.footer_back_some_social_network {
  text-align: left;
  margin: 5px;
  display: flex;
  align-items: center;
}
</style>
