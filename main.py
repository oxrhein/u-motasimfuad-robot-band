"""Name the Robot Band - make.fun entry.

Writes one funny name for a band made of robots, plus a few words
on the band's hit song, to entry.txt. Stdlib only, no network,
deterministic.
"""

import os

# One line, 67 characters. The gate (RULES.txt) allows 1-200.
LINE = "The Blue Screens of Death \u2014 hit single 'Ctrl+Alt+Delete My Number'."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
