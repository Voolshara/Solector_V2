<template>
  <div>
    <div id="map" style="width: 25vw; height: 350px"></div>
    <input id="coords" />
  </div>
</template>

<script>
import { loadYmap } from "vue-yandex-maps";
export default {
  name: "Map",
  async mounted() {
    const map_settings = {
      apiKey: "49ba2530-8257-44cb-b1cb-a19fb39e046c",
      lang: "ru_RU",
      coordorder: "latlong",
      version: "2.1",
    };
    await loadYmap({ map_settings, debug: true });
    ymaps.ready(init);
    function init() {
      var myPlacemark,
        myMap = new ymaps.Map(
          "map",
          {
            center: [55.753994, 37.622093],
            zoom: 7,
          },
          {
            searchControlProvider: "yandex#search",
          }
        );
      // Слушаем клик на карте.
      myMap.events.add("click", function(e) {
        var coords = e.get("coords");
        document.getElementById("coords").value = coords;
        // Если метка уже создана – просто передвигаем ее.
        if (myPlacemark) {
          myPlacemark.geometry.setCoordinates(coords);
        }
        // Если нет – создаем.
        else {
          myPlacemark = createPlacemark(coords);
          myMap.geoObjects.add(myPlacemark);
          // Слушаем событие окончания перетаскивания на метке.
          myPlacemark.events.add("dragend", function() {
            getAddress(myPlacemark.geometry.getCoordinates());
          });
        }
        getAddress(coords);
      });
      // Создание метки.
      function createPlacemark(coords) {
        return new ymaps.Placemark(
          coords,
          {
            iconCaption: "здесь солнечная электростаниця",
          },
          {
            preset: "islands#violetDotIconWithCaption",
            draggable: true,
          }
        );
      }
      // Определяем адрес по координатам (обратное геокодирование).
      function getAddress(coords) {
        myPlacemark.properties.set("iconCaption", "солнечная электростанция");
        /*  ymaps.geocode(coords).then(function (res) {
            myPlacemark.properties
                .set({
                  "sfdgfhgjk":"sfdgfhg"
                });
          });*/
      }
    }
  },
};
</script>

<style>
#coords {
  display: none;
}
</style>
