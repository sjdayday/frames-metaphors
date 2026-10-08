#!/usr/bin/env python3
"""Start-date and dataset sensitivity of short-window temperature trends (case 02, pair Q3).

Two annual global-mean series:
  * HadCRUT4 (Met Office, ensemble median, 1950-2021) - the series the AR5 window was computed
    on and the one most "pause" statements used; a copy with provenance is kept beside the
    figure at figures/data/hadcrut4-annual-1950-2021.csv.
  * NOAA NOAAGlobalTemp (source "GCAG") - the current series, with the post-2015 corrections
    built in; read from the climate-explain case file's snapshot
    (../climate-explain/loehle-scafetta-curve-fitting/data/annual.csv, or $ANNUAL_CSV).

Panels:
  A. HadCRUT4 1979-2021 with least-squares trend lines over windows that all end in 2012 but
     start in 1996, 1998, 2000, 2002 - the start year sets the slope.
  B. The fitted trend (deg C per decade) as a function of the window's start year, windows
     ending 2012, for both datasets - start year and dataset together.
  C. The same with the windows extended to each series' last complete year.

Intervals (90%) are ordinary least squares with the residuals' lag-1 autocorrelation folded
into an effective sample size (n_eff = n (1-r)/(1+r), the Santer et al. 2008 form).  The figure
is about the shape of the curves; the AR5 values quoted in the case (0.05 [-0.05, 0.15] for
1998-2012; 0.12 [0.08, 0.14] for 1951-2012, on HadCRUT4 at its 2013 version) are printed in the
caption for comparison.

Outputs: figures/startdate-sensitivity.png and .svg and figures/startdate-sensitivity-trends.csv.
Deterministic; no randomness.
"""
import csv, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import rcParams

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, ".."))
OUTDIR = os.path.join(REPO, "case-studies", "02-pause-hiatus", "figures")
NOAA_CSV = os.environ.get("ANNUAL_CSV") or os.path.join(
    REPO, "..", "climate-explain", "loehle-scafetta-curve-fitting", "data", "annual.csv")
HAD_CSV = os.path.join(OUTDIR, "data", "hadcrut4-annual-1950-2021.csv")

# ---- palette (validated with the dataviz skill's validator, light mode) ----
SURFACE = "#fcfcfb"; INK = "#0b0b0b"; INK2 = "#52514e"; MUTED = "#8a8984"; GRID = "#e6e5e1"
ORDINAL = {1996: "#86b6ef", 1998: "#5598e7", 2000: "#2a78d6", 2002: "#184f95"}   # blue ramp, steps 250/350/450/600
C_HAD = "#2a78d6"    # categorical slot 1: HadCRUT4
C_NOAA = "#eb6834"   # categorical slot 2: NOAA

rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": MUTED,
                 "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
                 "axes.spines.top": False, "axes.spines.right": False})

def load_noaa(path, last_full=None):
    years, vals = [], []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["Source"] == "GCAG":
                years.append(int(row["Year"])); vals.append(float(row["Mean"]))
    y, v = np.array(years), np.array(vals); o = np.argsort(y); y, v = y[o], v[o]
    last_full = last_full or int(os.environ.get("LAST_FULL_YEAR", y.max() - 1))  # the snapshot's last year is partial
    m = y <= last_full
    return y[m], v[m]

def load_had(path):
    years, vals = [], []
    with open(path, newline="", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or line.startswith("year"): continue
            a, b = line.strip().split(","); years.append(int(a)); vals.append(float(b))
    return np.array(years), np.array(vals)

def ols_trend(x, y):
    """Slope per year and its standard error with an AR(1) effective-sample-size correction."""
    n = len(x); xm, ym = x.mean(), y.mean()
    sxx = ((x - xm) ** 2).sum(); b = ((x - xm) * (y - ym)).sum() / sxx; a = ym - b * xm
    resid = y - (a + b * x)
    r1 = float(np.clip(np.corrcoef(resid[:-1], resid[1:])[0, 1], -0.99, 0.99)) if n > 3 else 0.0
    n_eff = max(n * (1 - r1) / (1 + r1), 3.0)
    se = np.sqrt(((resid ** 2).sum() / (n_eff - 2)) / sxx)
    return a, b, se

def curve(years, vals, starts, end):
    b_l, lo_l, hi_l, rows = [], [], [], []
    for s in starts:
        sel = (years >= s) & (years <= end)
        a, b, se = ols_trend(years[sel].astype(float), vals[sel]); bd, sd = 10 * b, 10 * se
        b_l.append(bd); lo_l.append(bd - 1.645 * sd); hi_l.append(bd + 1.645 * sd)
        rows.append((int(s), int(end), int(sel.sum()), bd, bd - 1.645 * sd, bd + 1.645 * sd))
    return np.array(b_l), np.array(lo_l), np.array(hi_l), rows

def main():
    yN, vN = load_noaa(NOAA_CSV); yH, vH = load_had(HAD_CSV)
    endA = 2012; lastN, lastH = int(yN.max()), int(yH.max())
    starts = np.arange(1970, 2004)
    os.makedirs(OUTDIR, exist_ok=True)
    data = {"HadCRUT4": (yH, vH, lastH, C_HAD), "NOAA": (yN, vN, lastN, C_NOAA)}
    allrows = []

    fig, (axA, axB, axC) = plt.subplots(3, 1, figsize=(7.2, 10.8), dpi=160, facecolor=SURFACE,
                                        gridspec_kw={"height_ratios": [1, 1, 1], "hspace": 0.5})
    for ax in (axA, axB, axC):
        ax.set_facecolor(SURFACE); ax.grid(True, axis="y", color=GRID, linewidth=0.8); ax.set_axisbelow(True)

    # ---- A: HadCRUT4 series with four windows ending 2012
    sel = (yH >= 1979)
    axA.plot(yH[sel], vH[sel], color=INK2, linewidth=1.2, marker="o", markersize=2.6, markerfacecolor=INK2,
             markeredgecolor=SURFACE, markeredgewidth=0.6, zorder=3)
    for s in (1996, 1998, 2000, 2002):
        w = (yH >= s) & (yH <= endA); a, b, se = ols_trend(yH[w].astype(float), vH[w])
        xx = np.array([s, endA]); axA.plot(xx, a + b * xx, color=ORDINAL[s], linewidth=2.0, zorder=4, solid_capstyle="round",
                                           label=f"{s}–{endA}: {10*b:+.2f} °C/decade")
    axA.legend(loc="upper left", frameon=False, fontsize=8, title="window and fitted trend", title_fontsize=8)
    i98 = int(np.where(yH == 1998)[0][0])
    axA.annotate("1998 El Niño", xy=(1998, vH[i98]), xytext=(1999.5, vH[i98] + 0.2), color=INK2, fontsize=8,
                 arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.8))
    axA.axvspan(1998, endA, color=C_HAD, alpha=0.05, linewidth=0, zorder=1)
    axA.set_xlim(1978, lastH + 1.5); axA.set_ylabel("anomaly vs. 1961–1990 (°C)")
    axA.set_title("A. HadCRUT4, four windows ending in 2012: the start year sets the slope", loc="left", color=INK, fontsize=10)

    # ---- B and C: trend vs start year, both datasets
    for ax, mode in ((axB, "2012"), (axC, "last")):
        for name, (yy, vv, last, color) in data.items():
            end = endA if mode == "2012" else last
            b_arr, lo, hi, rows = curve(yy, vv, starts, end)
            allrows += [(name,) + r for r in rows]
            label = f"{name}, windows ending {end}"
            ax.fill_between(starts, lo, hi, color=color, alpha=0.13, linewidth=0, zorder=2)
            ax.plot(starts, b_arr, color=color, linewidth=2.0, zorder=4, label=label)
            ax.annotate(name, xy=(starts[-1], b_arr[-1]), xytext=(starts[-1] + 0.4, b_arr[-1]), color=INK, fontsize=8, va="center")
        ax.axhline(0, color=MUTED, linewidth=0.8, zorder=3)
        ax.axvline(1998, color=MUTED, linewidth=0.8, linestyle=(0, (2, 3)), zorder=3)
        ax.set_xlim(1969.5, 2008); ax.set_ylabel("fitted trend (°C/decade), 90% band")
        ax.legend(loc="lower left", frameon=False, fontsize=8)
    # long-term reference on B
    w = (yH >= 1951) & (yH <= 2012); a_l, b_l, se_l = ols_trend(yH[w].astype(float), vH[w])
    axB.axhline(10 * b_l, color=MUTED, linewidth=1.0, linestyle=(0, (4, 3)), zorder=3)
    axB.annotate(f"HadCRUT4 1951–2012: {10*b_l:+.2f} °C/decade", xy=(1970.3, 10 * b_l), xytext=(1970.3, 10 * b_l - 0.045), color=INK2, fontsize=8)
    bH98 = [r for r in allrows if r[0] == "HadCRUT4" and r[1] == 1998 and r[2] == endA][0][4]
    axB.annotate("start at the 1998 El Niño", xy=(1998, bH98), xytext=(1985.5, -0.12), color=INK2, fontsize=8,
                 arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.8))
    axB.set_ylim(-0.25, 0.42)
    axB.set_title("B. Windows ending 2012: slide the start year, and change the dataset", loc="left", color=INK, fontsize=10)
    axC.set_ylim(-0.05, 0.42); axC.set_xlabel("start year of the window")
    axC.set_title(f"C. The same windows extended to each series' last complete year ({lastH}; {lastN})", loc="left", color=INK, fontsize=10)

    fig.text(0.01, 0.003,
             f"Data: HadCRUT.4.6.0.0 annual ensemble median (Met Office; figures/data/) and NOAA NOAAGlobalTemp annual anomalies (GCAG) as snapshotted in climate-explain, years through {lastN}.\n"
             f"Ordinary least squares; 90% bands use an AR(1) effective sample size. For comparison, AR5 (2013, on HadCRUT4) gave 0.05 [–0.05 to 0.15] °C/decade for 1998–2012 and "
             f"0.12 [0.08 to 0.14] for 1951–2012.\nScript: scripts/fig_startdate_sensitivity.py.", fontsize=6.5, color=INK2, ha="left", va="bottom")
    for ext in ("png", "svg"):
        fig.savefig(os.path.join(OUTDIR, f"startdate-sensitivity.{ext}"), facecolor=SURFACE, bbox_inches="tight")

    with open(os.path.join(OUTDIR, "startdate-sensitivity-trends.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["dataset", "start", "end", "n_years", "trend_C_per_decade", "ci90_low", "ci90_high"])
        for r in allrows: w.writerow([r[0], r[1], r[2], r[3], f"{r[4]:.4f}", f"{r[5]:.4f}", f"{r[6]:.4f}"])
    for name in data:
        for s, e in ((1996, endA), (1998, endA), (2000, endA), (2002, endA), (1998, data[name][2])):
            r = [x for x in allrows if x[0] == name and x[1] == s and x[2] == e][0]
            print(f"{name:8s} {s}-{e}: {r[4]:+.3f} [{r[5]:+.3f}, {r[6]:+.3f}] (n={r[3]})")
    print(f"HadCRUT4 1951-2012: {10*b_l:+.3f} [{10*(b_l-1.645*se_l):+.3f}, {10*(b_l+1.645*se_l):+.3f}]")

if __name__ == "__main__":
    main()
