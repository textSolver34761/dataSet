<script>
  import GraphData from "./GraphData.svelte";

  let data = {
    message: [
      "Taille la plus acheter",
      "Etat les plus acheteurs",
      "Model les plus acheter",
      "Taille les mois acheter",
      "Etat les moins acheteurs",
      "Model les moins acheter",
    ],

    shoeMostSold: [
      { x: "8.0", y: 5363 },
      { x: "8.5", y: 5300 },
      { x: "9.0", y: 9706 },
      { x: "9.5", y: 8685 },
      { x: "10.0", y: 11093 },
      { x: "10.5", y: 8784 },
      { x: "11.0", y: 9251 },
      { x: "11.5", y: 4502 },
      { x: "12.0", y: 7297 },
      { x: "13.0", y: 4602 },
    ],

    statsMostB: [
      { x: "California", y: 19349 },
      { x: "NewYork", y: 16525 },
      { x: "Oregon", y: 7681 },
      { x: "Florida", y: 6376 },
      { x: "Texas", y: 5876 },
      { x: "NewJersey", y: 4720 },
      { x: "Illinois", y: 3782 },
      { x: "Pennsylvania", y: 3109 },
      { x: "Massachusetts", y: 2903 },
      { x: "Michigan", y: 2762 },
    ],

    modelMostSold: [
      { x: "Yz Butter", y: 11423 },
      { x: "Yz Beluga2.0", y: 10395 },
      { x: "Yz Zebra", y: 10110 },
      { x: "Yz Blue-Tint", y: 9297 },
      { x: "Yz CreamWhite", y: 9097 },
      { x: "Yz Sesame", y: 5553 },
      { x: "Yz Static", y: 4983 },
      { x: "Yz SemiFrozen", y: 4854 },
      { x: "AJ1 OW UniversityBlue", y: 4635 },
      { x: "Yz Static Reflective", y: 3184 },
    ],

    statsLessB: [
      { x: "WestVirginia", y: 166 },
      { x: "Mississippi", y: 163 },
      { x: "Maine", y: 132 },
      { x: "Idaho", y: 107 },
      { x: "Vermont", y: 84 },
      { x: "NorthDakota", y: 64 },
      { x: "Alaska", y: 61 },
      { x: "SouthDakota", y: 55 },
      { x: "Montana", y: 49 },
      { x: "Wyoming", y: 40 },
    ],

    sizeLessSold: [
      { x: "3.5", y: 4 },
      { x: "4.5", y: 1304 },
      { x: "6.5", y: 2219 },
      { x: "12.5", y: 628 },
      { x: "13.5", y: 147 },
      { x: "14.0", y: 1791 },
      { x: "14.5", y: 84 },
      { x: "15.0", y: 130 },
      { x: "16.0", y: 79 },
      { x: "17.0", y: 4 },
    ],

    modelLessSold: [
      { x: "Blazer OW WolfGrey", y: 288 },
      { x: "Yz Copper", y: 225 },
      { x: "AM97 OW Elemental", y: 216 },
      { x: "Yz Green", y: 196 },
      { x: "Yz PirateBlack2016", y: 122 },
      { x: "Yz Moonrock", y: 100 },
      { x: "Yz PirateBlack2015", y: 95 },
      { x: "Yz OxfordTan", y: 70 },
      { x: "Yz Turtledove", y: 68 },
      { x: "AF1 OW", y: 31 },
    ],
  };
</script>

<style>
</style>

<GraphData msg={data.message[0]} data={data.shoeMostSold} />
<br />
<GraphData msg={data.message[1]} data={data.statsMostB} />
<br />
<GraphData msg={data.message[2]} data={data.modelMostSold} />
<br />
<GraphData msg={data.message[3]} data={data.statsLessB} />
<br />
<GraphData msg={data.message[4]} data={data.sizeLessSold} />
<br />
<GraphData msg={data.message[5]} data={data.modelLessSold} />
