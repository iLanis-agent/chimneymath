import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

def sweep_plan(firesPerWeek, weeks, rateG):
    if not (firesPerWeek > 0) or not (weeks > 0) or not (rateG > 0):
        return {"error": "fires, weeks and rate must be positive"}
    fires = firesPerWeek * weeks
    grams = fires * rateG
    if grams < 100: verdict = "light buildup on the labeled scale"
    elif grams < 250: verdict = "time for a routine sweep on the labeled scale"
    else: verdict = "book a sweep soon on the labeled scale"
    return {"fires": fires, "grams": grams, "verdict": verdict}

def draft_plan(heightM, insideC, outsideC):
    if not (heightM > 0): return {"error": "height must be positive"}
    if not (insideC > outsideC): return {"error": "inside must be warmer than outside"}
    inK = insideC + 273.15
    outK = outsideC + 273.15
    pa = round1(3460 * heightM * (1 / outK - 1 / inK))
    if pa < 5: verdict = "a weak pull on the labeled scale"
    elif pa < 15: verdict = "a workable pull on the labeled scale"
    else: verdict = "a strong pull on the labeled scale"
    return {"pa": pa, "verdict": verdict}

def flue_plan(widthCm, heightCm):
    if not (widthCm > 0) or not (heightCm > 0):
        return {"error": "width and height must be positive"}
    openA = widthCm * heightCm
    flueA = openA / 10
    dia = round1(2 * math.sqrt(flueA / math.pi))
    if dia <= 15: verdict = "a common round size on the labeled rule"
    elif dia <= 25: verdict = "a larger liner on the labeled rule"
    else: verdict = "an uncommon size on the labeled rule"
    return {"area": openA, "diameter": dia, "verdict": verdict}

def render_sweep(r, firesPerWeek, weeks, rateG):
    return (plural(firesPerWeek, "fire") + " a week for " + plural(weeks, "week") + " at a labeled " + fmt(rateG)
            + " g a fire: " + plural(r["fires"], "fire") + ", about " + plural(r["grams"], "gram")
            + " of creosote - " + r["verdict"] + ".")

def render_draft(r, heightM, insideC, outsideC):
    return ("A flue " + fmt(heightM) + " m tall, " + fmt(insideC) + " C inside and " + fmt(outsideC)
            + " C outside: about " + fmt(r["pa"]) + " Pa of stack pull - " + r["verdict"] + ".")

def render_flue(r, widthCm, heightCm):
    return ("A " + fmt(widthCm) + " x " + fmt(heightCm) + " cm opening (" + fmt(r["area"])
            + " sq cm) takes a labeled tenth in the flue: about " + fmt(r["diameter"]) + " cm round - "
            + r["verdict"] + ".")

cases = []
for a in [(5, 20, 2), (1, 10, 4), (7, 12, 4), (0, 10, 2)]:
    r = sweep_plan(*a)
    cases.append({"fn": "sweepPlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_sweep(r, *a)})
for a in [(8, 21, 0), (15, 24, -5), (3, 20, 10), (8, 15, 20), (0, 21, 0)]:
    r = draft_plan(*a)
    cases.append({"fn": "draftPlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_draft(r, *a)})
for a in [(90, 70), (60, 50), (40, 40), (0, 70)]:
    r = flue_plan(*a)
    cases.append({"fn": "fluePlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_flue(r, *a)})

with open("expected.json", "w") as f:
    f.write(json.dumps(cases, separators=(",", ":")) + "\n")
print("wrote", len(cases), "cases")
