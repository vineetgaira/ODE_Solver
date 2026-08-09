```
 ███╗   ██╗██╗   ██╗███╗   ███╗███████╗██████╗ ██╗ ██████╗ █████╗ ██╗
 ████╗  ██║██║   ██║████╗ ████║██╔════╝██╔══██╗██║██╔════╝██╔══██╗██║
 ██╔██╗ ██║██║   ██║██╔████╔██║█████╗  ██████╔╝██║██║     ███████║██║
 ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗██║██║     ██╔══██║██║
 ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║███████╗██║  ██║██║╚██████╗██║  ██║███████╗
 ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝

 ██████╗  ██████╗ ███████╗   ███████╗ ██████╗ ██╗     ██╗   ██╗███████╗██████╗
██╔═══██╗██╔══██╗██╔════╝   ██╔════╝██╔═══██╗██║     ██║   ██║██╔════╝██╔══██╗
██║   ██║██║  ██║█████╗     ███████╗██║   ██║██║     ██║   ██║█████╗  ██████╔╝
██║   ██║██║  ██║██╔══╝     ╚════██║██║   ██║██║     ╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██████╔╝███████╗   ███████║╚██████╔╝███████╗ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═════╝ ╚══════╝   ╚══════╝ ╚═════╝ ╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝
```

<p align="center">
  <img src="https://img.shields.io/badge/python-3.13+-blue.svg" alt="Python 3.13+">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License">
  <img src="https://img.shields.io/github/last-commit/vineetgaira/ODE_Solver" alt="Last commit">
  <img src="https://img.shields.io/badge/status-active-brightgreen.svg" alt="Status">
  <img src="https://img.shields.io/badge/type-learning--project-orange.svg" alt="Learning project">
</p>

<p align="center">
  A colourful command-line tool for solving first-order ordinary differential
  equations numerically — five methods, side-by-side comparison, plots, and
  export, all from the terminal.
</p>

---

## About This Project

This is a **learning project**, built to actually understand numerical methods for ODEs from the ground up rather than just calling `scipy.integrate.odeint` and trusting a black box. Every method — Euler, Heun, Midpoint, Ralston, RK4 — is implemented by hand, step by step, so the tradeoffs between accuracy and computational cost are something felt, not just read about.

Along the way this project became a broader exercise in Python fundamentals: refactoring near-duplicate functions into a shared registry pattern, building a proper input-validation pipeline, parsing user-supplied math expressions safely with SymPy instead of trusting raw `eval()`, and designing a caching/export layer that writes to CSV, TXT, and JSON without duplicating logic three times over.

It's a genuine work in progress, built in public, and it's meant to keep growing.

---

## Preview

```
==============================================
             NUMERICAL ODE SOLVER
==============================================
  [1] New Problem
  [2] Solve Initial Value Problem
  [3] Compare Numerical Methods
  [4] Plot Solution Graph
  [5] View Method Information
  [6] Settings
  [7] Help
  [8] Exit
Choice :
```

---

## Features

| Feature | Description |
|---|---|
| **5 numerical methods** | Euler, Heun, Midpoint, Ralston, and RK4 — Heun, Midpoint, and Ralston all share a single generalized `rk2()` implementation, parameterized rather than duplicated |
| **Method comparison** | Solve with every method at once and compare side-by-side, with or without a known exact solution to measure error against |
| **Symbolic equation input** | Type equations naturally (`x + y`, `log(x - 2*y)`, `sin(x)*y`) — parsed and evaluated with SymPy, not raw `eval()`, with a restricted character set and symbol whitelist for safety |
| **Rich terminal tables** | Step-by-step solution tables and comparison views rendered with `rich`, not plain `print()` |
| **Plotting** | Plot a single solution or overlay all methods for comparison, via `matplotlib` |
| **Save graphs** | Save the last plot to `data/graphs/` as a timestamped `.png` |
| **Export** | Every solved problem is saved to CSV, TXT, and JSON automatically (toggleable via settings) |
| **Persistent settings** | Configure decimal precision, output colour, graph style (line/scatter), and auto-save — stored in `data/settings.json` and reloaded on every run |
| **Method reference** | Look up the formula, order of accuracy, and a plain-language explanation for any method from the in-app menu |

---

## Installation

```bash
git clone https://github.com/vineetgaira/ODE_Solver.git
cd ODE_Solver
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

1. **New Problem** — enter an equation for `dy/dx`, initial values `x0`/`y0`, a target `x`, and a step size `h`.
2. **Solve** — pick a single method and see the step-by-step table.
3. **Compare** — run all five methods at once, optionally against a known exact solution to see the error for each.
4. **Plot** — visualize a single solution or all methods overlaid, and save the graph if you'd like.
5. **Settings** — adjust precision, colour output, graph style, and auto-save, all persisted between sessions.

### Supported functions

`sin(x)` `cos(x)` `tan(x)` `exp(x)` `sqrt(x)` `log(x)` `pi` `e`

Only `x`, `y`, numbers, and the operators/functions above are accepted — anything else is rejected before it ever reaches SymPy's parser.

---

## Methods implemented

| Method | Order | Notes |
|---|---|---|
| Euler | 1st — O(h) | Simplest, one evaluation per step, error accumulates fastest |
| Heun | 2nd — O(h²) | Predictor-corrector / trapezoidal rule, built as a parameterized case of `rk2()` |
| Midpoint | 2nd — O(h²) | Evaluates the slope at the interval midpoint, also a case of `rk2()` |
| Ralston | 2nd — O(h²) | Minimizes local truncation error among 2nd-order RK methods, also a case of `rk2()` |
| RK4 | 4th — O(h⁴) | Classical Runge-Kutta, best accuracy-to-cost tradeoff of the five |

All five are registered in a single `METHODS_REGISTRY` dict in `solver.py`, so solving, comparing, and adding a new method later all go through one consistent code path rather than a long `if/elif` chain.

---

## Project structure

```
ODE_Solver/
├── main.py                  # Main program loop
├── src/
│   ├── parser.py             # Equation parsing (SymPy), validation, and evaluation
│   ├── solver.py             # METHODS_REGISTRY and solve/compare orchestration
│   ├── methods.py            # Euler, Heun, Midpoint, Ralston, RK4 implementations
│   ├── display.py            # Terminal output (rich tables, colour, comparisons)
│   ├── graph.py               # Plotting and graph export (matplotlib)
│   ├── exporter.py            # CSV / TXT / JSON export
│   ├── settings.py            # Persistent user settings
│   ├── input_handler.py       # Menu choice + numeric input validation
│   ├── menu.py                 # Menu rendering
│   ├── ascii_art.py            # Banner and terminal art
│   └── constants.py             # Menu definitions and method reference info
└── data/                        # Exported problems, solutions, settings, saved graphs
```

---

## What's Still In Progress

This project is being built incrementally, and a few areas are still evolving:
- Broader test coverage for edge cases in equation parsing and step-size handling
- More descriptive error messages for malformed or ambiguous equations
- Possible future support for systems of ODEs, not just single first-order equations

None of this is hidden — it's genuinely part of the learning process, and the roadmap is open.

---

## Contributing

This project is open source, and contributions are genuinely welcome — whether that's fixing a bug, improving the parser's error handling, adding a new numerical method, writing tests, or just cleaning up a rough edge in the code. If you're learning numerical methods or Python yourself, digging through this codebase and proposing improvements is a great way to learn by doing, and a PR (even a small one) is always appreciated.

If you're planning something larger (a new feature, a structural refactor), opening an issue first to discuss it is a good way to make sure the direction fits before you put in the work — but small fixes and improvements are welcome to come straight as a PR.

---

## License

MIT — see [LICENSE](LICENSE) for details.
