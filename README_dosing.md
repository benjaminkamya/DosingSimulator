# 💊 Drug Half-Life & Dosing Simulator

A small simulator that visualizes how much of a drug remains in the
bloodstream over time, based on first-order elimination kinetics —
including what happens with repeated dosing (does the drug accumulate,
or clear out between doses?).

Built as a pharmacology-focused companion to my cheminformatics projects
([DrugLikenessEvaluator](https://github.com/benjaminkamya/DrugLikenessEvaluator),
[ChemSimilarity](https://github.com/benjaminkamya/ChemSimilarity)) — this one's
less about molecular structure, more about what happens once a drug is
actually in the body.

## The Pharmacology, Briefly

Most drugs are cleared from the body following **first-order kinetics**:
the rate of elimination is proportional to how much drug is currently
present. This produces an exponential decay curve, where a fixed
**fraction** (not a fixed amount) of the drug is removed per unit time.

```
C(t) = C0 * (0.5) ^ (t / half_life)
```

- `C0` — starting dose/concentration
- `half_life` — time for concentration to drop by 50%
- `t` — time elapsed

For repeated dosing, each new dose stacks on top of whatever's left in
the body from previous doses — which is why some drugs build up
("accumulate") if taken too frequently relative to their half-life.

## Setup

```bash
pip install matplotlib
```

## Usage

```bash
python dosing_simulator.py
```

Runs 3 example simulations and pops open a graph for each:

1. **Single dose decay** — paracetamol-like, 500mg, half-life 2.5h
2. **Repeated dosing** — 500mg every 4h for 6 doses, shows accumulation
3. **Long half-life drug** — 10mg every 24h for 5 doses, shows more
   dramatic buildup (diazepam-like, ~30h half-life)

## Try it yourself

Change the numbers in the `if __name__ == "__main__":` block at the
bottom of the script to try real drug half-lives:

| Drug | Approx. half-life |
|---|---|
| Ibuprofen | ~2 hours |
| Paracetamol | ~2.5 hours |
| Caffeine | ~5 hours |
| Diazepam | ~30 hours |
| Fluoxetine | ~4-6 **days** |

## Notes

- This is a simplified one-compartment model — real pharmacokinetics
  also accounts for absorption rate, distribution, and individual
  variation (age, liver/kidney function, etc.), which this doesn't model.
- Useful for building intuition about accumulation and steady-state
  dosing, not for making real clinical dosing decisions.

## Built with

- [Matplotlib](https://matplotlib.org/) — plotting
