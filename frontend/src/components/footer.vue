<template>
    <div class="footer_back">
        <div class="footer_back_adress">
            <div class="footer_back_adress_company_name">Solector</div>
            <div class="footer_back_adress_contacts">г.Чебоксары <br>+7 (961) 339 24 00 <br>solector59948@gmail.com</div>
        </div>

        <div class="footer_back_developers">
            <div class="footer_back_developers_title">Разработчики<br><hr class="footer_line"></div>
            <div class="footer_back_developers_names">
                <div class="footer_back_developers_names_participant"><img src="/img/Telegram App.svg" alt="" class="footer_icone"> Тунгулов Станислав</div>
                
                <div class="footer_back_developers_names_participant"><img src="/img/Telegram App.svg" alt="" class="footer_icone"> Кадилов Михаил</div>
            </div>
        </div>

        <div class="footer_back_social_networks">
            <div class="footer_back_social_networks_title">Социальные сети<br><hr class="footer_line"></div>
            <div class="footer_back_social_networks_blocks">
                <div class="footer_back_social_networks_block_1">
                    <div class="footer_back_some_social_network"><img src="/img/Instagram.svg" alt="" class="footer_icone">Instagram</div>
                    <div class="footer_back_some_social_network"><img src="/img/VK.com.svg" alt="" class="footer_icone">VK</div>
                    <div class="footer_back_some_social_network"><img src="/img/Telegram App.svg" alt="" class="footer_icone">Telegram</div>
                </div>
                
                <div class="footer_back_social_networks_block_2">
                    <div class="footer_back_some_social_network"><img src="/img/gmail.svg" alt="" class="footer_icone">Вопросы</div>
                    <div class="footer_back_some_social_network"><img src="/img/forms.svg" alt="" class="footer_icone">FeedBack</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200&display=swap');

.footer_back{
    min-width: 100%;
    height: 100px;
    background: #151B38;
    display: flex;
    justify-content: space-around;
    color: #FFFFFF;
    font-family: 'Montserrat', sans-serif;

}

.footer_back_adress{
    display: flex;
    flex-direction: column;
    /* justify-content: space-around; */
    justify-content: center;
}

.footer_back_adress_company_name{
    font-size: 14pt;
    text-align: left;
    margin: 2px;
}

.footer_back_adress_contacts{
    text-align: left;
    font-size: 5pt;   
    margin: 2px;
}

.footer_back_developers_title{
    font-size: 10pt;
    margin: 10px;
}

.footer_back_social_networks_title{
    font-size: 10pt;
    margin: 10px;
}

.footer_back_developers_names{
    font-size: 6pt;
    
}

.footer_back_developers_names_participant{
    text-align: left;
    margin: 5px;
}

.footer_back_social_networks_blocks{
    font-size: 6pt;
    display: flex;
}

.footer_back_some_social_network{
    text-align: left;
    margin: 5px;
}

.footer_icone{
    width: 9px;
    height: 9px;
    margin-right: 5px;
}

.footer_line{
    /* size: 0 px; */
    border-style: inset;
}
</style>