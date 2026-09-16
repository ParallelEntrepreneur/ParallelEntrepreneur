// Shared by every rendered image: theme switch and the signal-trace drawing.
if (location.hash === '#light') document.documentElement.dataset.theme = 'light';

const SVG_NS = 'http://www.w3.org/2000/svg';

function el(name, attrs, parent) {
  const node = document.createElementNS(SVG_NS, name);
  for (const [k, v] of Object.entries(attrs)) node.setAttribute(k, v);
  if (parent) parent.appendChild(node);
  return node;
}

// Deterministic, so a re-render produces the same traces.
function rng(seed) {
  let s = seed >>> 0;
  return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 4294967296);
}

// A square wave from x0 to x1 around baseline y. Pulses get denser towards
// x1, which reads as activity building up to the trace's current position.
function squareWave(x0, x1, y, amp, seed) {
  const r = rng(seed);
  let x = x0, high = false, d = `M${x0} ${y}`;
  while (x < x1) {
    const progress = (x - x0) / Math.max(1, x1 - x0);
    const step = (6 + r() * 34) * (1.15 - progress * .75);
    x = Math.min(x1, x + step);
    d += ` H${x.toFixed(1)}`;
    if (x < x1) { high = !high; d += ` V${(high ? y - amp : y).toFixed(1)}`; }
  }
  if (high) d += ` V${y}`;
  return d;
}
