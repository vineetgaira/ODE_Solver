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
</p>

<p align="center">
A colourful command-line tool for solving first-order ordinary differential
equations numerically — five methods, side-by-side comparison, plots, and
export, all from the terminal.
</p>

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

## Features

| Feature | Description |
|---|---|
| **5 numerical methods** | Euler, Heun, Midpoint, Ralston, and RK4 |
| **Method comparison** | Solve with every method at once and compare side-by-side, with or without a known exact solution |
| **Symbolic equation input** | Type equations naturally (`x + y`, `log(x - 2*y)`, `sin(x)*y`) — parsed with SymPy, supports `sin`, `cos`, `tan`, `exp`, `sqrt`, `log`, `pi`, `e` |
| **Plotting** | Plot a single solution or overlay all methods for comparison, via matplotlib |
| **Save graphs** | Save the last plot to `data/graphs/` as a `.png` |
| **Export** | Every solved problem is saved to CSV, TXT, and JSON automatically (toggleable) |
| **Settings** | Configure decimal precision, output colour, graph style (line/scatter), and auto-save — persisted across sessions |
| **Method reference** | Look up the formula, order of accuracy, and a plain-language explanation for any method |

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
3. **Compare** — run all five methods at once, optionally against a known exact solution to see the error.
4. **Plot** — visualize a single solution or all methods overlaid, and save the graph if you'd like.

### Supported functions

`sin(x)` `cos(x)` `tan(x)` `exp(x)` `sqrt(x)` `log(x)` `pi` `e`

## Methods implemented

| Method | Order | Notes |
|---|---|---|
| Euler | 1st — O(h) | Simplest, one evaluation per step, error accumulates fastest |
| Heun | 2nd — O(h²) | Predictor-corrector, trapezoidal rule |
| Midpoint | 2nd — O(h²) | Evaluates slope at the interval midpoint |
| Ralston | 2nd — O(h²) | Minimizes local truncation error among 2nd-order RK methods |
| RK4 | 4th — O(h⁴) | Classical Runge-Kutta, best accuracy-to-cost tradeoff |

## Project structure

```
ODE_Solver/
├── main.py                # Main program loop
├── src/
│   ├── parser.py           # Equation parsing (SymPy) and evaluation
│   ├── solver.py           # Method registry and solve/compare logic
│   ├── methods.py          # Euler, Heun, Midpoint, Ralston, RK4 implementations
│   ├── display.py          # Terminal output (rich tables, colour)
│   ├── graph.py            # Plotting and graph export
│   ├── exporter.py         # CSV / TXT / JSON export
│   ├── settings.py         # Persistent user settings
│   ├── input_handler.py    # Input validation
│   ├── menu.py              # Menu rendering
│   └── constants.py         # Menu definitions, method info
└── data/                    # Exported problems, solutions, settings, graphs
```

## License

MIT — see [LICENSE](LICENSE) for details.
