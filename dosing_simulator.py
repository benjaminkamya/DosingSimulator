"""
Drug Half-Life & Dosing Simulator 💊
--------------------------------------
Simulates how much of a drug remains in the bloodstream over time,
based on its half-life, using first-order elimination kinetics.

Supports single doses AND repeated dosing schedules (e.g. every 8 hours),
so you can see whether a drug accumulates or reaches "steady state."

The Pharmacology, Briefly
--------------------------------
Most drugs are cleared from the body following first-order kinetics:
the RATE of elimination is proportional to how much drug is currently
present. This produces an exponential decay curve, and means a fixed
FRACTION of the drug is removed per unit time, not a fixed amount.

The formula for remaining concentration after time t:

    C(t) = C0 * (0.5) ^ (t / half_life)

Where:
    C0         = starting concentration (or dose)
    half_life  = time for concentration to drop by 50%
    t          = time elapsed

For repeated dosing, we just add a new dose on top of whatever's left
from the previous one(s) at each dosing interval.

Requirements:
    pip install matplotlib
"""

import matplotlib.pyplot as plt


def single_dose_curve(dose: float, half_life: float, duration: float, dt: float = 0.1):
    """Return time points and remaining-drug amounts for one dose."""
    times = []
    amounts = []
    t = 0.0
    while t <= duration:
        remaining = dose * (0.5) ** (t / half_life)
        times.append(t)
        amounts.append(remaining)
        t += dt
    return times, amounts


def repeated_dose_curve(dose: float, half_life: float, interval: float,
                         num_doses: int, dt: float = 0.1):
    """
    Simulate repeated dosing. Each new dose stacks on top of whatever
    is left in the body from previous doses.
    """
    duration = interval * num_doses
    times = [round(t, 2) for t in _frange(0, duration, dt)]
    amounts = [0.0 for _ in times]

    # For every dose given, add its own decay curve starting at its dose time
    for dose_number in range(num_doses):
        dose_time = dose_number * interval
        for i, t in enumerate(times):
            if t >= dose_time:
                elapsed = t - dose_time
                amounts[i] += dose * (0.5) ** (elapsed / half_life)

    return times, amounts


def _frange(start, stop, step):
    t = start
    while t <= stop:
        yield t
        t += step


def plot_single_dose(dose, half_life, duration):
    times, amounts = single_dose_curve(dose, half_life, duration)

    plt.figure(figsize=(8, 5))
    plt.plot(times, amounts, linewidth=2)
    plt.axhline(y=dose / 2, color='gray', linestyle='--', alpha=0.5,
                label=f"50% remaining (1 half-life = {half_life}h)")
    plt.xlabel("Time (hours)")
    plt.ylabel("Amount of drug remaining (mg)")
    plt.title(f"Single Dose Decay — Half-life: {half_life}h")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_repeated_dose(dose, half_life, interval, num_doses):
    times, amounts = repeated_dose_curve(dose, half_life, interval, num_doses)

    plt.figure(figsize=(9, 5))
    plt.plot(times, amounts, linewidth=2, color='crimson')

    # Mark each dosing time
    for i in range(num_doses):
        plt.axvline(x=i * interval, color='gray', linestyle=':', alpha=0.4)

    plt.xlabel("Time (hours)")
    plt.ylabel("Amount of drug in body (mg)")
    plt.title(f"Repeated Dosing — {dose}mg every {interval}h, half-life {half_life}h")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("💊 Drug Half-Life & Dosing Simulator\n")

    # --- Example 1: Paracetamol-ish single dose ---
    # Paracetamol's real half-life is roughly 2-3 hours
    print("Example 1: Single dose (paracetamol-like, 500mg, half-life 2.5h)")
    plot_single_dose(dose=500, half_life=2.5, duration=15)

    # --- Example 2: Repeated dosing, does it accumulate? ---
    # Same drug, taken every 4 hours for 6 doses (24 hours)
    print("Example 2: Repeated dosing (500mg every 4h, 6 doses)")
    plot_repeated_dose(dose=500, half_life=2.5, interval=4, num_doses=6)

    # --- Example 3: A longer half-life drug (accumulates more) ---
    # e.g. something more like diazepam (~30h half-life) taken daily
    print("Example 3: Long half-life drug (10mg every 24h, 5 doses)")
    plot_repeated_dose(dose=10, half_life=30, interval=24, num_doses=5)
