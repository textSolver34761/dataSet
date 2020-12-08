<script>
  import { goto } from "@sapper/app";

  let search = "";
  let keyCode;

  function redirect() {
    if (search !== "") {
      search = { search };
    }
  }
  function handleKeydown(event) {
    if (search !== "") {
      keyCode = event.keyCode;
      if (keyCode === 13) {
        redirect();
      }
    }
  }
</script>

<style>
  .search {
    display: block;
    float: right;
    border: none;
    outline: none;
    border-radius: 0.5rem;
    margin-right: 1rem;
  }
  button,
  input[type="text"] {
    float: right;
    border: none;
    outline: none;
    padding: 1em 0.5em;
    margin-top: 0.1rem;
    font-size: 1rem;
    font-weight: 300;
  }

  input {
    border-radius: 0.5rem 0 0 0.5rem;
  }
  button {
    cursor: pointer;
    border-radius: 0 0.5rem 0.5rem 0;
  }
</style>

<svelte:window on:keydown={handleKeydown} />

<div class="search">
  <button on:click={redirect}>search</button>
  <input type="text" bind:value={search} placeholder="Recherche..." />
</div>
