<script>
  import Table from "../components/Table.svelte";
  import Stat from "../components/Stat.svelte";
</script>

<style>
  @media (min-width: 480px) {
    h1 {
      font-size: 4em;
    }
  }
</style>

<svelte:head>
  <title>Sapper project template</title>
</svelte:head>

<!--h1>Great success!</h1-->

<Table />
<br />
<Stat />