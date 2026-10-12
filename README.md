# Chimney math

Chimney math turns a season at the hearth into numbers: fires become grams of
creosote on a labeled scale, flue height and temperatures become pascals of
stack pull, and the fireplace opening becomes a round-liner size by the labeled
one-tenth rule.

Live site: https://ilanis-agent.github.io/chimneymath/

## The three tools

- **Sweep plan** - fires per week x weeks x a labeled creosote rate (grams a
  fire) become total fires, grams of buildup, and a labeled sweep verdict
  (light under 100 g, routine under 250 g, book soon above).
- **Draft plan** - flue height in meters plus inside and outside temperatures
  become stack pull in pascals, using a labeled sea-level constant of 3460:
  `pa = 3460 * h * (1 / (outsideC + 273.15) - 1 / (insideC + 273.15))`,
  rounded to one decimal.
- **Flue plan** - opening width x height in cm; the flue takes a labeled tenth
  of the opening area, and the round diameter is `2 * sqrt(area / 10 / pi)`,
  rounded to one decimal.

## Limits

Every norm is labeled and illustrative. These tools do not inspect a chimney
and never judge one safe: creosote, blockages and carbon monoxide belong to a
certified sweep.

## Files

- `index.html` - landing page with the labeled norms
- `app.html` - the three calculators
- `engine.js` - shared calculation and render logic (browser + node)
- `oracle.py` - python mirror of the engine, writes `expected.json`
- `test.js` - runs the engine against `expected.json` (13 cases, 59 checks)

Run the tests: `python3 oracle.py && node test.js`
