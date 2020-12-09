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
    }
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
