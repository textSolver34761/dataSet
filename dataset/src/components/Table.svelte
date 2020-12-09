<script>
	let searchTerm = "";
	let list = [
		{
			"id": 1,
			"order_date": "2/13/19",
			"brand": "Yeezy",
			"sneaker": "adidas-Yeezy-Boost-350-V2-Static-Reflective",
			"sale_price": "$699",
			"retail_price": "$220",
			"release_date": "12/26/18",
			"size": "11.0",
			"region": "New Jersey",
		},
		{
			"id": 99946,
			"order_date": "2/13/19",
			"brand": "Yeezy",
			"sneaker": "adidas-Yeezy-Boost-350-V2-Static-Reflective",
			"sale_price": "$699",
			"retail_price": "$220",
			"release_date": "12/26/18",
			"size": "11.0",
			"region": "New Jersey",
		},
		{
			"id": 99947,
			"order_date": "2/13/19",
			"brand": "Yeezy",
			"sneaker": "adidas-Yeezy-Boost-350-V2-Static-Reflective",
			"sale_price": "$618",
			"retail_price": "$220",
			"release_date": "12/26/18",
			"size": "9.5",
			"region": "California",
		},
		{
			"id": 99948,
			"order_date": "2/13/19",
			"brand": "Yeezy",
			"sneaker": "adidas-Yeezy-Boost-350-V2-Static-Reflective",
			"sale_price": "$581",
			"retail_price": "$220",
			"release_date": "12/26/18",
			"size": "9.0",
			"region": "Oregon",
		},
		{
			"id": 99949,
			"order_date": "2/13/19",
			"brand": "Yeezy",
			"sneaker": "adidas-Yeezy-Boost-350-V2-Static-Reflective",
			"sale_price": "$594",
			"retail_price": "$220",
			"release_date": "12/26/18",
			"size": "8.5",
			"region": "Oregon",
		},
		{
			"id": 99950,
			"order_date": "2/13/19",
			"brand": " Yeezy",
			"sneaker": "adidas-Yeezy-Boost-350-V2-Static-Reflective",
			"sale_price": "$582",
			"retail_price": "$220",
			"release_date": "12/26/18",
			"size": "10.0",
			"region": "New Jersey",
		},
		{
			"id": 99951,
			"order_date": "2/13/19",
			"brand": " Yeezy",
			"sneaker": "adidas-Yeezy-Boost-350-V2-Static-Reflective",
			"sale_price": "$565",
			"retail_price": "$220",
			"release_date": "12/26/18",
			"size": "8.0",
			"region": "Oregon",
		},
		{
			"id": 99952,
			"order_date": "2/13/19",
			"brand": " Yeezy",
			"sneaker": "adidas-Yeezy-Boost-350-V2-Static-Reflective",
			"sale_price": "$598",
			"retail_price": "$220",
			"release_date": "12/26/18",
			"size": "8.5",
			"region": "California",
		},
		{
			"id": 99953,
			"order_date": "2/13/19",
			"brand": " Yeezy",
			"sneaker": "adidas-Yeezy-Boost-350-V2-Static-Reflective",
			"sale_price": "$605",
			"retail_price": "$220",
			"release_date": "12/26/18",
			"size": "5.5",
			"region": "New York",
		},
		{
			"id": 99954,
			"order_date": "2/13/19",
			"brand": " Yeezy",
			"sneaker": "adidas-Yeezy-Boost-350-V2-Static-Reflective",
			"sale_price": "$650",
			"retail_price": "$220",
			"release_date": "12/26/18",
			"size": "11.0",
			"region": "California",
		},
		{
			"id": 99955,
			"order_date": "2/13/19",
			"brand": " Yeezy",
			"sneaker": "adidas-Yeezy-Boost-350-V2-Static-Reflective",
			"sale_price": "$640",
			"retail_price": "$220",
			"release_date": "12/26/18",
			"size": "11.5",
			"region": "Texas",
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

<h1>Les {list.length} dernières ventes </h1>
<p> sur 100'000 </p>
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
			<th>Région</th>
		</tr>
	</thead>
	<tbody>
		{#each list as data}
			<tr>
				<td>{data.order_date}</td>
				<td>{data.brand}</td>
				<td>{data.sneaker}</td>
				<td>{data.sale_price}</td>
				<td>{data.retail_price}</td>
				<td>{data.release_date}</td>
				<td>{data.size}</td>
				<td>{data.region}</td>
			</tr>
		{/each}
	</tbody>
</table>
