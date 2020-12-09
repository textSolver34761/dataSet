<script>
import { scaleLinear } from 'd3-scale';

const points = [
    { shoe:8.0, sales: 5363 },
    { shoe:8.5, sales: 5300 },
    { shoe:9.0, sales: 9706 },
    { shoe:9.5, sales: 8685 },
    { shoe:10.0, sales: 11093 },
    { shoe:10.5, sales: 8784 },
    { shoe:11.0, sales: 9251 },
    { shoe:11.5, sales: 4502 },
    { shoe:12.0, sales: 7297 },
    { shoe:13.0, sales: 4602 },
];

const Xabsc = points.map(pts => pts.shoe);
const Yordn = points.map(pts => pts.sales);
const padding = { top: 20, right: 15, bottom: 20, left: 25 };

let width = 500;
let height = 300;

function formatMobile(tick) {
    return "'" + tick % 100;
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
    font-size: .725em;
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

<h2> États les moins acheteurs</h2> <br>

<div class="chart" bind:clientWidth={width} bind:clientHeight={height}>
<svg>
    <!-- y axis -->
    <g class="axis y-axis" transform="translate(0,{padding.top})">
        {#each Yordn as tick}
            <g class="tick tick-{tick}" transform="translate(0, {yScale(tick) - padding.bottom})">
                <line x2="100%"></line>
                <text y="-4">{tick} {tick === 20 ? ' per 1,000 population' : ''}</text>
            </g>
        {/each}
    </g>

    <!-- x axis -->
    <g class="axis x-axis">
        {#each points as point, i}
            <g class="tick" transform="translate({xScale(i)},{height})">
                <text x="{barWidth/2}" y="-4">{width > 380 ? point.shoe : formatMobile(point.shoe)}</text>
            </g>
        {/each}
    </g>

    <g class='bars'>
        {#each points as point, i}
            <rect
                x="{xScale(i) + 2}"
                y="{yScale(point.sales)}"
                width="{barWidth - 4}"
                height="{height - padding.bottom - yScale(point.sales)}"
            ></rect>
        {/each}
    </g>
</svg>
</div>