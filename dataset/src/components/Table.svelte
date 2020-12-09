<script>
  let searchTerm = "";
  let list = [
    {
      id:"1",
      order:"2/13/19",
      brand:"Yeezy",
      Sneaker:"adidas-Yeezy-Boost-350-V2-Static-Reflective",
      Sale:"$699",
      Retail:"$220",
      Release:"12/26/18",
      Shoe: "11.0",
      Buyer:"New Jersey"
    },
    {
      id:"99946",
      order:"2/13/19",
      brand:"Yeezy",
      Sneaker:"adidas-Yeezy-Boost-350-V2-Static-Reflective",
      Sale:"$699",
      Retail:"$220",
      Release:"12/26/18",
      Shoe: "11.0",
      Buyer: "New Jersey"
    },
    {
      id:"99947",
      order:"2/13/19",
      brand:"Yeezy",
      Sneaker:"adidas-Yeezy-Boost-350-V2-Static-Reflective",
      Sale:"$618",
      Retail:"$220",
      Release: "12/26/18",
      Shoe:"9.5",
      Buyer:"California"
    },{
      id:"99948",
      order: "2/13/19",
      brand:"Yeezy",
      Sneaker: "adidas-Yeezy-Boost-350-V2-Static-Reflective",
      Sale: "$581",
      Retail:"$220",
      Release: "12/26/18",
      Shoe:"9.0",
      Buyer:"Oregon"
    },
    { 
      id: "99949",
      order:"2/13/19",
      brand:"Yeezy",
      Sneaker:"adidas-Yeezy-Boost-350-V2-Static-Reflective",
      Sale:"$594",
      Retail: "$220",
      Release:"12/26/18",
      Shoe: "8.5",
      Buyer:"Oregon",
    },    \"99950\": {        \"order\": \"2/13/19\",        \"brand\": \" Yeezy\",        Sneaker: \"adidas-Yeezy-Boost-350-V2-Static-Reflective\",        Sale: \"$582\",        \"Retail Price\": \"$220\",        \"Release Date\": \"12/26/18\",        \"Shoe Size\": 10.0,        \"Buyer Region\": \"New Jersey\"    },    \"99951\": {        \"order\": \"2/13/19\",        \"brand\": \" Yeezy\",        Sneaker: \"adidas-Yeezy-Boost-350-V2-Static-Reflective\",        Sale: \"$565\",        \"Retail Price\": \"$220\",        \"Release\": \"12/26/18\",        \"Shoe\": 8.0,        \"Buyer Region\": \"Oregon\"    },    \"99952\": {        \"order\": \"2/13/19\",        \"brand\": \" Yeezy\",        Sneaker: \"adidas-Yeezy-Boost-350-V2-Static-Reflective\",        Sale: \"$598\",        \"Retail Price\": \"$220\",        \"Release\": \"12/26/18\",        \"Shoe\": 8.5,        \"Buyer Region\": \"California\"    },    \"99953\": {        \"order\": \"2/13/19\",        \"brand\": \" Yeezy\",        Sneaker: \"adidas-Yeezy-Boost-350-V2-Static-Reflective\",        Sale: \"$605\",        \"Retail Price\": \"$220\",        \"Release\": \"12/26/18\",        \"Shoe\": 5.5,        \"Buyer Region\": \"New York\"    },    \"99954\": {        \"order\": \"2/13/19\",        \"brand\": \" Yeezy\",        Sneaker: \"adidas-Yeezy-Boost-350-V2-Static-Reflective\",        Sale: \"$650\",        \"Retail Price\": \"$220\",        \"Release\": \"12/26/18\",        \"Shoe\": 11.0,        \"Buyer Region\": \"California\"    },    \"99955\": {        \"order\": \"2/13/19\",        \"brand\": \" Yeezy\",        Sneaker: \"adidas-Yeezy-Boost-350-V2-Static-Reflective\",        Sale: \"$640\",        \"Retail Price\": \"$220\",        \"Release\": \"12/26/18\",        \"Shoe\": 11.5,        \"Buyer Region\": \"Texas\"    }}"}
];

</script>

<style>
  table {
    text-align: center;
  }
  table,
  td {
    border: 1px solid #333;
  }
  thead {
    background-color: #333;
    color: #fff;
  }
  h1 {
    text-align: center;
  }
</style>
<p> Il y a .... ventes dans le tableau. </p> <br>
<h1>Tableau</h1>
<table>
  <thead>
    <tr>
      <th>Order Date</th>
      <th>Brand</th>
      <th>Sneaker</th>
      <th>Sale Price</th>
      <th>Retail Price</th>
      <th>Release Date</th>
      <th>Shoe Size</th>
      <th>Buyer</th>
    </tr>
  </thead>
  <tbody>
    {#each list as data}
      <tr>
        <td>{data.order}</td>
        <td>{data.brand}</td>
        <td>{data.Sneaker}</td>
        <td>{data.Sale}</td>
        <td>{data.Retail}</td>
        <td>{data.Release}</td>
        <td>{data.Shoe}</td>
        <td>{data.Buyer}</td>
      </tr>
    {/each}
  </tbody>
</table>
