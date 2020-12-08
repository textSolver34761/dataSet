<script>
  let searchTerm = "";
  let list = [
    {
      order: "07/12/2020",
      brand: "Nike",
      Sneaker: "bof",
      Name: "Je ne sais pas",
      Sale: 155,
      Retail: 7550,
      Release: "05/11/2020",
      Shoe: 9,
      Buyer: "Ben",
    },
    {
      order: "08/12/2020",
      brand: "Nike",
      Sneaker: "bof",
      Name: "Je ne sais pas",
      Sale: 1550,
      Retail: 75500,
      Release: "12/11/2020",
      Shoe: 12,
      Buyer: "Sarah",
    },
  ];

  //   function handleClick() {
  //   filteredList = list.filter(item => item.name.indexOf(as searchTerm) !== -1);
  // }
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

<input bind:value={searchTerm} placeholder="filtrer" />
<!-- <button on:click|once={handleClick}> Valider </button> -->

<h1>Tableau</h1>
<table>
  <thead>
    <tr>
      <th>Order Date</th>
      <th>Brand</th>
      <th>Sneaker</th>
      <th>Name</th>
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
        <td>{data.Name}</td>
        <td>{data.Sale}</td>
        <td>{data.Retail}</td>
        <td>{data.Release}</td>
        <td>{data.Shoe}</td>
        <td>{data.Buyer}</td>
      </tr>
    {/each}
  </tbody>
</table>
