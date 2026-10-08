#!/usr/bin/env python3
"""What "consensus" measured: the surveyed field and the assessments' attribution statements (case 03, Figure R-1).

Data: the Bray & von Storch surveys of climate scientists (1996, 2003, 2008, 2013, 2015/16), as read from
the original reports by the climate-science-evolution project and tabulated in its
data/bray-von-storch-series.json; a verbatim snapshot of that file is kept beside this figure at
figures/data/bray-von-storch-series.json (set $BVS_JSON to read another copy).

Panel A. The share of surveyed scientists accepting, in the middle on, and rejecting the attribution
         statement, by survey year.  The wording changed in 2008: 1996 and 2003 asked for agreement with
         "Climate change is mostly the result of anthropogenic causes" (1-7; accept = 1-3, middle = 4,
         reject = 5-7); from 2008 the question was "How convinced are you that most of recent or near
         future climate change is, or will be, a result of anthropogenic causes?" (1-7; accept = 5-7,
         middle = 4, reject = 1-3).  The connectors across the change are dashed.  The 2008 counts were
         reconstructed by the evolution project from the report's histograms and reproduce its means and
         standard deviations exactly.  Above the panel, the IPCC assessments' attribution statements and
         their calibrated terms (06-assessment-language.md), at the year of each report.
Panel B. The 2015/16 survey's share question: "Since 1850 ... warmed by 0.5-0.7 C.  Approximately what
         percent would you attribute to human causes?" (N = 587) - the grain at which the surveyed
         minority mostly sits.

Outputs: figures/consensus-surveyed-field.png and .svg.  Deterministic; no randomness.
"""
import json, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import rcParams

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, ".."))
OUTDIR = os.path.join(REPO, "case-studies", "03-consensus", "figures")
BVS_JSON = os.environ.get("BVS_JSON") or os.path.join(OUTDIR, "data", "bray-von-storch-series.json")

# ---- palette (validated with the dataviz skill's validator, light mode; as in Figure Q3-1) ----
SURFACE = "#fcfcfb"; INK = "#0b0b0b"; INK2 = "#52514e"; MUTED = "#8a8984"; GRID = "#e6e5e1"
C_ACCEPT = "#2a78d6"   # categorical slot 1
C_REJECT = "#eb6834"   # categorical slot 2
C_MIDDLE = "#8a8984"   # neutral
RAMP5 = ["#c9ddf7", "#86b6ef", "#5598e7", "#2a78d6", "#184f95"]   # blue ramp for the five share bins

rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": MUTED,
                 "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
                 "axes.spines.top": False, "axes.spines.right": False})

SURVEYS = [("1996", 1996.0, "1996"), ("2003", 2003.0, "2003"), ("2008", 2008.0, "2008"),
           ("2013", 2013.0, "2013"), ("2015_16", 2016.0, "2015/16")]
ASSESSMENTS = [  # year, report, attribution term, row for the label (0 = upper, 1 = lower)
    (1995, "SAR 1995", "“a discernible human influence”", 0),
    (2001, "TAR 2001", "“likely”", 2),
    (2007, "AR4 2007", "“very likely”", 1),
    (2013, "AR5 2013", "“extremely likely”", 2),
    (2021, "AR6 2021", "“unequivocal”", 0),
]

def main():
    with open(BVS_JSON, encoding="utf-8") as f:
        d = json.load(f)
    att = d["attribution"]
    xs = np.array([x for _, x, _ in SURVEYS])
    acc = np.array([att[k]["accept"] for k, _, _ in SURVEYS], dtype=float)
    mid = np.array([att[k]["middle"] for k, _, _ in SURVEYS], dtype=float)
    rej = np.array([att[k]["reject"] for k, _, _ in SURVEYS], dtype=float)
    Ns = [att[k]["N"] for k, _, _ in SURVEYS]
    share = d["attribution"]["2015_16_share"]
    counts = np.array(share["counts_1_to_5"], dtype=float); N_share = int(share["N"])
    assert int(counts.sum()) == N_share
    pct = 100 * counts / N_share

    os.makedirs(OUTDIR, exist_ok=True)
    fig = plt.figure(figsize=(7.2, 8.8), dpi=160, facecolor=SURFACE)
    gs = fig.add_gridspec(4, 1, height_ratios=[0.85, 2.7, 0.22, 1.75], hspace=0.06, left=0.1, right=0.97, top=0.95, bottom=0.11)
    axT = fig.add_subplot(gs[0]); axA = fig.add_subplot(gs[1]); axB = fig.add_subplot(gs[3])
    for ax in (axT, axA, axB):
        ax.set_facecolor(SURFACE)
    XLIM = (1993.5, 2023)

    # ---- strip: the assessments' attribution statements
    axT.set_ylim(0, 1); axT.set_xlim(*XLIM)
    for sp in ("left", "bottom"): axT.spines[sp].set_visible(False)
    axT.set_xticks([]); axT.set_yticks([])
    for yr, rep, term, row in ASSESSMENTS:
        y = (0.74, 0.46, 0.18)[row]
        axT.plot([yr], [y], marker="v", color=INK2, markersize=5, zorder=4, clip_on=False)
        ha, dx = ("left", -0.3) if yr == 1995 else ("right", 0.3) if yr == 2021 else ("center", 0.0)
        axT.text(yr + dx, y + 0.13, f"{rep}: {term}", ha=ha, va="bottom", fontsize=7.6, color=INK)
        axA.axvline(yr, color=MUTED, linewidth=0.7, linestyle=(0, (1, 3)), zorder=1)
    axT.set_title("IPCC attribution statement, by report year (06-assessment-language.md)", loc="left", fontsize=7.6, color=INK2, style="italic", pad=4)

    # ---- A: the surveyed field
    axA.set_xlim(*XLIM)
    axA.grid(True, axis="y", color=GRID, linewidth=0.8); axA.set_axisbelow(True)
    axA.axvspan(2005.5, XLIM[1], color=C_ACCEPT, alpha=0.035, linewidth=0, zorder=0)
    axA.axvline(2005.5, color=MUTED, linewidth=0.9, linestyle=(0, (3, 3)), zorder=2)
    series = [(acc, C_ACCEPT, "accept: mostly anthropogenic", "o"), (rej, C_REJECT, "reject", "s"), (mid, C_MIDDLE, "middle (4 of 7)", "D")]
    for vals, color, label, mk in series:
        # same-wording segments solid, the 2003->2008 connector dashed
        axA.plot(xs[:2], vals[:2], color=color, linewidth=2.0, zorder=4)
        axA.plot(xs[1:3], vals[1:3], color=color, linewidth=1.4, linestyle=(0, (3, 3)), zorder=3)
        axA.plot(xs[2:], vals[2:], color=color, linewidth=2.0, zorder=4)
        axA.plot(xs, vals, color=color, linewidth=0, marker=mk, markersize=6, markerfacecolor=color,
                 markeredgecolor=SURFACE, markeredgewidth=0.9, zorder=5, label=label)
    # value labels: accept above (below at 1996, where reject sits above it); reject below, or to the right where the middle series is close
    acc_off = [(0, -13), (0, 7), (0, 7), (0, 7), (0, 7)]
    rej_off = [(0, 7), (0, -13), (8, 7), (8, 7), (9, -2)]
    for i, x in enumerate(xs):
        axA.annotate(f"{acc[i]:.0f}%", xy=(x, acc[i]), xytext=acc_off[i], textcoords="offset points", ha="center", va="center" if acc_off[i][1] < 0 else "bottom", fontsize=8, color=C_ACCEPT)
        axA.annotate(f"{rej[i]:.0f}%", xy=(x, rej[i]), xytext=rej_off[i], textcoords="offset points", ha="left" if rej_off[i][0] else "center", va="center" if rej_off[i][1] < 0 else "bottom", fontsize=8, color=C_REJECT)
    axA.set_ylim(0, 112); axA.set_yticks([0, 20, 40, 60, 80, 100]); axA.set_yticklabels([f"{t}%" for t in (0, 20, 40, 60, 80, 100)])
    axA.set_xticks(xs); axA.set_xticklabels([f"{lab}\nN = {Ns[i]}" for i, (_, _, lab) in enumerate(SURVEYS)], fontsize=8); axA.tick_params(axis="x", length=0)
    axA.legend(loc="center left", bbox_to_anchor=(0.5, 0.42), frameon=False, fontsize=8, title="surveyed climate scientists", title_fontsize=8)
    axA.text(1994.2, 110, "“Climate change is mostly the result of\nanthropogenic causes” — agree / disagree", ha="left", va="top", fontsize=7.4, color=INK2, style="italic")
    axA.text(2006.2, 110, "“How convinced are you that most of recent or near future\nclimate change is, or will be, a result of anthropogenic causes?”", ha="left", va="top", fontsize=7.4, color=INK2, style="italic")
    axA.text(2005.2, 52, "wording changed", ha="right", va="center", fontsize=7.4, color=MUTED, rotation=90)
    axA.set_title("A. The surveyed field, 1996–2015/16: an even split becomes five-sixths as the assessment statements step up",
                  loc="left", color=INK, fontsize=9.4, pad=5)

    # ---- B: the 2015/16 share question
    bins = ["0%", "1–25%", "26–50%", "51–75%", "76–100%"]
    xb = np.arange(5)
    axB.grid(True, axis="y", color=GRID, linewidth=0.8); axB.set_axisbelow(True)
    axB.bar(xb, pct, color=RAMP5, width=0.72, zorder=3)
    for i in range(5):
        axB.annotate(f"{pct[i]:.1f}%\n(n = {int(counts[i])})", xy=(xb[i], pct[i]), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom", fontsize=7.6, color=INK)
    axB.set_xticks(xb); axB.set_xticklabels(bins); axB.tick_params(axis="x", length=0)
    axB.set_xlabel("share of the warming since 1850 attributed to human causes (2015/16 survey, N = %d)" % N_share, fontsize=8)
    axB.set_ylim(0, 70); axB.set_yticks([0, 20, 40, 60]); axB.set_yticklabels(["0%", "20%", "40%", "60%"])
    above_half = 100 * counts[3:].sum() / N_share; at_or_below = 100 * counts[:3].sum() / N_share
    axB.annotate(f"{at_or_below:.1f}% put the human share at half or below;\n{pct[0]:.1f}% put it at zero",
                 xy=(1.0, 13), xytext=(-0.3, 42), fontsize=7.8, color=INK2, ha="left",
                 arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.8))
    axB.plot([2.64, 4.36], [63, 63], color=MUTED, linewidth=0.9); axB.plot([2.64, 2.64], [61, 63], color=MUTED, linewidth=0.9); axB.plot([4.36, 4.36], [61, 63], color=MUTED, linewidth=0.9)
    axB.text(3.5, 64.5, f"{above_half:.1f}% above half", ha="center", va="bottom", fontsize=7.8, color=INK2)
    axB.set_title("B. Where the minority sits: the human share, as the surveyed scientists estimate it (2015/16)",
                  loc="left", color=INK, fontsize=9.4, pad=5)

    fig.text(0.01, 0.004,
             "Data: Bray & von Storch surveys of climate scientists (GKSS 2007/11; GKSS 2010/9; HZG 2014-4; HZG 2016-2), as read from the reports by the\n"
             "climate-science-evolution project (data/bray-von-storch-series.json, snapshot in figures/data/). 2008 counts reconstructed from the report's histograms.\n"
             "Accept = 1–3 of 7 (1996, 2003) or 5–7 of 7 (2008 on); middle = 4; reject = the rest; 1996 and 2003 omit 1% and 5% missing. Script: scripts/fig_consensus_surveys.py.",
             fontsize=6.4, color=INK2, ha="left", va="bottom")
    for ext in ("png", "svg"):
        fig.savefig(os.path.join(OUTDIR, f"consensus-surveyed-field.{ext}"), facecolor=SURFACE, bbox_inches="tight")
    for i, (k, _, lab) in enumerate(SURVEYS):
        print(f"{lab:8s} N={Ns[i]:4d}  accept {acc[i]:5.1f}  middle {mid[i]:4.1f}  reject {rej[i]:5.1f}")
    print("2015/16 share bins (%):", ", ".join(f"{b} {p:.1f}" for b, p in zip(bins, pct)), f"| above half {above_half:.1f}")

if __name__ == "__main__":
    main()
