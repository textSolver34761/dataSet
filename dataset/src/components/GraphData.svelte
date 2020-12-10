<script>
  import { scaleLinear } from "d3-scale";
  export let msg;
  export let data;

  const points = data;

  const Xabsc = points.map((pts) => pts.x);
  const Yordn = points.map((pts) => pts.y);

  const padding = { top: 20, right: 10, bottom: 20, left: 10 };

  let width = 500;
  let height = 200;

  function formatMobile(tick) {
    return "'" + (tick % 100);
  }

  $: xScale = scaleLinear()
    .domain([0, Yordn.length])
    .range([padding.left, width - padding.right]);

  $: yScale = scaleLinear()
    .domain([0, Math.max.apply(null, Yordn)])
    .range([height - padding.bottom, padding.top]);

  $: innerWidth = width - (padding.left + padding.right);
  $: barWidth = innerWidth / Xabsc.length;
</script>

<style>
  h2 {
    text-align: center;
  }

  .chart {
    width: 100%;
    max-width: 500px;
    margin: 0 auto;
  }

  svg {
    position: relative;
    width: 100%;
    height: 200px;
  }

  .tick {
    font-family: Helvetica, Arial;
    font-size: 0.725em;
    font-weight: 200;
  }

  .tick line {
    stroke: #e2e2e2;
    stroke-dasharray: 2;
  }

  .tick text {
    fill: #ccc;
    text-anchor: start;
  }

  .tick.tick-0 line {
    stroke-dasharray: 0;
  }

  .x-axis .tick text {
    text-anchor: middle;
  }

  .bars rect {
    fill: #a11;
    stroke: none;
    opacity: 0.65;
  }
</style>

<h2>{msg}</h2>
<br />

<div class="chart" bind:clientWidth={width} bind:clientHeight={height}>
  <svg>
    <!-- y axis -->
    <g class="axis y-axis" transform="translate(0,{padding.top})">
      {#each Yordn as tick}
        <g
          class="tick tick-{tick}"
          transform="translate(0, {yScale(tick) - padding.bottom})">
          <line x2="100%" />
          <text y="-4">
            {tick}
            {tick === 20 ? ' per 1,000 population' : ''}
          </text>
        </g>
      {/each}
    </g>

    <!-- x axis -->
    <g class="axis x-axis">
      {#each points as point, i}
        <g class="tick" transform="translate({xScale(i)},{height})">
          <text x={barWidth / 2} y="-4">
            {width > 380 ? point.x : formatMobile(point.x)}
          </text>
        </g>
      {/each}
    </g>

    <g class="bars">
      {#each points as point, i}
        <rect
          x={xScale(i) + 2}
          y={yScale(point.y)}
          width={barWidth - 4}
          height={height - padding.bottom - yScale(point.y)} />
      {/each}
    </g>
  </svg>
</div>
