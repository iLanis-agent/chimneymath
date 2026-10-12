(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function round1(x) { return Math.round(x * 10) / 10; }

  function sweepPlan(firesPerWeek, weeks, rateG) {
    if (!(firesPerWeek > 0) || !(weeks > 0) || !(rateG > 0)) return { error: "fires, weeks and rate must be positive" };
    var fires = firesPerWeek * weeks;
    var grams = fires * rateG;
    var verdict;
    if (grams < 100) verdict = "light buildup on the labeled scale";
    else if (grams < 250) verdict = "time for a routine sweep on the labeled scale";
    else verdict = "book a sweep soon on the labeled scale";
    return { fires: fires, grams: grams, verdict: verdict };
  }

  function draftPlan(heightM, insideC, outsideC) {
    if (!(heightM > 0)) return { error: "height must be positive" };
    if (!(insideC > outsideC)) return { error: "inside must be warmer than outside" };
    var inK = insideC + 273.15;
    var outK = outsideC + 273.15;
    var pa = 3460 * heightM * (1 / outK - 1 / inK);
    var pa1 = round1(pa);
    var verdict;
    if (pa1 < 5) verdict = "a weak pull on the labeled scale";
    else if (pa1 < 15) verdict = "a workable pull on the labeled scale";
    else verdict = "a strong pull on the labeled scale";
    return { pa: pa1, verdict: verdict };
  }

  function fluePlan(widthCm, heightCm) {
    if (!(widthCm > 0) || !(heightCm > 0)) return { error: "width and height must be positive" };
    var openA = widthCm * heightCm;
    var flueA = openA / 10;
    var dia = 2 * Math.sqrt(flueA / Math.PI);
    var dia1 = round1(dia);
    var verdict;
    if (dia1 <= 15) verdict = "a common round size on the labeled rule";
    else if (dia1 <= 25) verdict = "a larger liner on the labeled rule";
    else verdict = "an uncommon size on the labeled rule";
    return { area: openA, diameter: dia1, verdict: verdict };
  }

  function renderSweep(r, firesPerWeek, weeks, rateG) {
    return plural(firesPerWeek, "fire") + " a week for " + plural(weeks, "week") + " at a labeled " + rateG + " g a fire: " + plural(r.fires, "fire") + ", about " + plural(r.grams, "gram") + " of creosote - " + r.verdict + ".";
  }

  function renderDraft(r, heightM, insideC, outsideC) {
    return "A flue " + heightM + " m tall, " + insideC + " C inside and " + outsideC + " C outside: about " + r.pa + " Pa of stack pull - " + r.verdict + ".";
  }

  function renderFlue(r, widthCm, heightCm) {
    return "A " + widthCm + " x " + heightCm + " cm opening (" + r.area + " sq cm) takes a labeled tenth in the flue: about " + r.diameter + " cm round - " + r.verdict + ".";
  }

  var api = { sweepPlan: sweepPlan, draftPlan: draftPlan, fluePlan: fluePlan, renderSweep: renderSweep, renderDraft: renderDraft, renderFlue: renderFlue };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.ChimneyMath = api;
})(this);
