#!/usr/bin/env python3
"""The pane and the ladder (case 04, Figure G-1): a schematic, not data.

Panel A draws the picture the word "greenhouse" gives a listener: the atmosphere as a single pane of glass
that lets sunlight in and holds the ground's infrared back.  Drawn that way, an opaque pane cannot be made
more opaque, which is the saturation argument.

Panel B draws the mechanism as the physics states it: a column whose temperature falls with height at the
convective lapse rate (about 6.5 K per km); in the CO2 band the planet radiates to space from the height at
which the air is thin enough to let the radiation out (where the column is at the effective emission
temperature, about 255 K), not from the ground.  Adding CO2 raises that height into colder air; a colder
emitter radiates less; the column warms (the dashed profile) until the emitting level is as warm as before,
and the surface, tied to it along the lapse rate, warms with it.  The shift is drawn for a 3 K surface
warming (about half a kilometre), which is larger than the no-feedback response to a doubling (about 1.2 K)
and within the assessed range with feedbacks.

Numbers used: surface 288 K; lapse rate 6.5 K/km; effective emission temperature 255 K; illustrative
warming 3 K.  All are textbook values, chosen for the drawing.  Output: figures/pane-and-ladder.png and .svg.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.patches import FancyArrowPatch, Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, ".."))
OUTDIR = os.path.join(REPO, "case-studies", "04-greenhouse", "figures")

# ---- palette (as in Figures Q3-1 and R-1) ----
SURFACE = "#fcfcfb"; INK = "#0b0b0b"; INK2 = "#52514e"; MUTED = "#8a8984"; GRID = "#e6e5e1"
BLUE = "#2a78d6"; ORANGE = "#eb6834"
RAMP = ["#c9ddf7", "#86b6ef", "#5598e7", "#2a78d6", "#184f95"]   # light (thin, high) to dark (dense, low)
GROUND = "#b8b6b0"

rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": MUTED,
                 "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
                 "axes.spines.top": False, "axes.spines.right": False})

T_SURF, LAPSE, T_EMIT, DT = 288.0, 6.5, 255.0, 3.0

def arrow(ax, x0, y0, x1, y1, color, lw=1.6, style="-|>", ms=10, **kw):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle=style, mutation_scale=ms, color=color,
                                 linewidth=lw, shrinkA=0, shrinkB=0, **kw))

def panel_a(ax):
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.set_axis_off(); ax.set_facecolor(SURFACE)
    # ground and pane
    ax.add_patch(Rectangle((0.6, 0.8), 8.8, 0.9, facecolor=GROUND, edgecolor="none"))
    ax.text(5.0, 1.25, "ground", ha="center", va="center", fontsize=8, color=INK)
    ax.plot([0.6, 9.4], [6.2, 6.2], color=BLUE, linewidth=6, solid_capstyle="butt", alpha=0.85)
    ax.text(9.3, 6.6, "the pane \u2014 \u201cthe glass of a hot-house\u201d", ha="right", va="bottom", fontsize=7.8, color=BLUE)
    # sunlight in (three grey arrows through the pane to the ground)
    for x in (1.3, 2.1, 2.9):
        arrow(ax, x, 8.5, x, 1.75, INK2, lw=1.4)
    ax.text(2.1, 8.7, "sunlight passes in", ha="center", va="bottom", fontsize=8, color=INK2)
    # infrared up from the ground, held back at the pane (orange arrows that turn back)
    for x in (5.4, 6.4, 7.4):
        arrow(ax, x, 1.75, x, 5.9, ORANGE, lw=1.6)
        arrow(ax, x + 0.3, 5.9, x + 0.3, 2.3, ORANGE, lw=1.0, style="-|>", ms=7, linestyle=(0, (2, 2)))
    ax.text(4.25, 3.9, "the ground\u2019s\ninfrared is\n\u201ctrapped\u201d", ha="center", va="center", fontsize=7.8, color=ORANGE)
    ax.text(5.0, 9.75, "one layer: once it is opaque, more gas can do nothing \u2014\nthe saturation argument is an entailment of the drawing",
            ha="center", va="top", fontsize=7.8, color=INK, style="italic")
    ax.set_title("A. The picture: a single pane", loc="left", color=INK, fontsize=10, pad=6)

def panel_b(ax):
    ax.set_facecolor(SURFACE)
    z = np.linspace(0, 8, 200)
    T0 = T_SURF - LAPSE * z; T1 = T_SURF + DT - LAPSE * z
    ze0 = (T_SURF - T_EMIT) / LAPSE; ze1 = (T_SURF + DT - T_EMIT) / LAPSE
    # layers: bands lighter and thinner-looking with height
    edges = [0, 1.6, 3.2, 4.8, 6.4, 8.0]
    for i in range(5):
        ax.axhspan(edges[i], edges[i + 1], color=RAMP[4 - i], alpha=0.16, linewidth=0, zorder=0)
    ax.axhspan(-0.5, 0, color=GROUND, linewidth=0, zorder=0)
    # profiles
    ax.plot(T0, z, color=INK, linewidth=2.0, zorder=4, label="before: T = 288 K at the surface")
    ax.plot(T1, z, color=ORANGE, linewidth=2.0, linestyle=(0, (4, 3)), zorder=4, label="after more CO₂: the whole column warmer")
    # emission levels
    ax.axhline(ze0, color=INK2, linewidth=0.8, linestyle=(0, (1, 3)), zorder=3)
    ax.axhline(ze1, color=ORANGE, linewidth=0.8, linestyle=(0, (1, 3)), zorder=3)
    ax.plot([T_EMIT], [ze0], marker="o", markersize=7, color=INK, markeredgecolor=SURFACE, zorder=6)
    ax.plot([T_EMIT], [ze1], marker="o", markersize=7, color=ORANGE, markeredgecolor=SURFACE, zorder=6)
    # to space arrows from the emission levels
    arrow(ax, T_EMIT + 1.5, ze0, 298.5, ze0, INK2, lw=1.2, ms=9)
    ax.text(298.8, ze0 - 0.18, "radiates to space from here, at 255 K", ha="right", va="top", fontsize=7.6, color=INK2)
    # the rise of the emission level
    arrow(ax, 247.5, ze0 + 0.05, 247.5, ze1 - 0.05, ORANGE, lw=1.6, ms=10)
    ax.text(243.0, 5.9, "more CO₂:\nthe emitting level\nmoves up, into colder air",
            ha="right", va="bottom", fontsize=7.6, color=ORANGE)
    # surface warming arrow
    arrow(ax, T_SURF, 0.35, T_SURF + DT, 0.35, ORANGE, lw=1.6, ms=10)
    ax.text(T_SURF + DT + 1.0, 0.9, "the surface\nwarms with it", ha="left", va="center", fontsize=7.6, color=ORANGE)
    # lapse-rate note
    ax.text(262, 6.9, "convection fixes the slope:\nabout 6.5 K per km", ha="left", va="center", fontsize=7.6, color=INK2)
    ax.set_xlim(229, 300); ax.set_ylim(-0.5, 8.2)
    ax.set_xlabel("temperature (K)"); ax.set_ylabel("height (km)")
    ax.grid(True, axis="x", color=GRID, linewidth=0.7); ax.set_axisbelow(True)
    ax.legend(loc="upper right", frameon=False, fontsize=7.6)
    ax.text(230.5, 0.85, "ground", fontsize=8, color=INK, va="bottom")
    ax.set_title("B. The mechanism: a ladder of layers — nothing is trapped; the exit moves", loc="left", color=INK, fontsize=10, pad=6)
    return ze0, ze1

def main():
    os.makedirs(OUTDIR, exist_ok=True)
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(11.0, 5.4), dpi=160, facecolor=SURFACE,
                                   gridspec_kw={"width_ratios": [1, 1.25], "wspace": 0.12})
    panel_a(axA); ze0, ze1 = panel_b(axB)
    fig.text(0.01, 0.005,
             "Schematic, not data. Panel B uses textbook values (surface 288 K, lapse rate 6.5 K/km, effective emission temperature 255 K) and an illustrative 3 K warming, "
             f"which moves the emitting level by {ze1 - ze0:.2f} km;\nthe no-feedback response to a doubling of CO₂ is about 1.2 K. "
             "The emission-height account is the one P01 of climate-science-evolution gives for why the saturation objection failed. Script: scripts/fig_pane_and_ladder.py.",
             fontsize=6.4, color=INK2, ha="left", va="bottom")
    fig.subplots_adjust(left=0.04, right=0.985, top=0.9, bottom=0.17)
    for ext in ("png", "svg"):
        fig.savefig(os.path.join(OUTDIR, f"pane-and-ladder.{ext}"), facecolor=SURFACE)
    print(f"emission level before {ze0:.2f} km, after {ze1:.2f} km (shift {ze1 - ze0:.2f} km for {DT:.0f} K)")

if __name__ == "__main__":
    main()
