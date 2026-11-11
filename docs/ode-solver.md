# ODE Solver: algorithms and execution

This guide describes the implementation in this repository, including the numerical methods, how a problem moves through the program, and how the solver architecture developed. It is written against the current source in `src/`; when behavior in code differs from the README's intended behavior, this guide calls that out.

## 1. Problem being solved

The program accepts a scalar first-order initial-value problem

\[
  y' = f(x,y), \qquad y(x_0)=y_0,
\]

and a target coordinate `target_x` plus a fixed step size `h`. A numerical method repeatedly estimates the next value of `y` from the current pair `(x_n, y_n)`. The solver stores the initial point and every computed point as a sequence `[(x_0,y_0), (x_1,y_1), ...]`.

The implementation is explicit and fixed-step: it does not estimate error during integration, change `h`, locate events, or solve systems of equations. A “comparison” runs the same input independently through each registered method.

## 2. Methods and formulas

Write `f_n = f(x_n,y_n)`. Each method returns the next coordinate and value `(x_{n+1}, y_{n+1})`; the driver supplies the same `h` on each step.

### Euler

\[
 x_{n+1}=x_n+h, \qquad y_{n+1}=y_n+h f(x_n,y_n).
\]

This is the forward tangent-line estimate. It evaluates the derivative once per step. Its local truncation error is order `h²` and its accumulated/global error is order `h` for a sufficiently smooth problem. It is inexpensive and useful as a baseline, but can be inaccurate or unstable for a large step.

### The shared two-stage RK2 implementation

`src/methods.py` factors three second-order Runge–Kutta schemes into `rk2`. Its parameters correspond to

\[
 k_1=f(x_n,y_n),\quad
 k_2=f(x_n+\alpha h, y_n+\beta h k_1),\quad
 y_{n+1}=y_n+h(c_1k_1+c_2k_2).
\]

The concrete coefficient sets are:

| Method | `alpha` | `beta` | `c1` | `c2` | Interpretation |
|---|---:|---:|---:|---:|---|
| Heun | 1 | 1 | 1/2 | 1/2 | Euler-predict to the end, then average the initial and predicted endpoint slopes (trapezoidal predictor-corrector). |
| Midpoint | 1/2 | 1/2 | 0 | 1 | Take an Euler half-step and use its midpoint slope for the full step. |
| Ralston | 2/3 | 2/3 | 1/4 | 3/4 | A two-stage second-order scheme with the listed weighted slope combination. |

Each uses two derivative evaluations per step. They all have local error order `h³` and global error order `h²` under the usual smoothness assumptions. The methods have different error constants, so their answers need not match at the same step size.

### Classical RK4

In `rk4`, the implementation stores the increments (each `k` already includes `h`):

\[
\begin{aligned}
 k_1 &= h f(x_n,y_n),\\
 k_2 &= h f(x_n+h/2,y_n+k_1/2),\\
 k_3 &= h f(x_n+h/2,y_n+k_2/2),\\
 k_4 &= h f(x_n+h,y_n+k_3),\\
 y_{n+1} &= y_n+(k_1+2k_2+2k_3+k_4)/6,\\
 x_{n+1} &= x_n+h.
\end{aligned}
\]

It evaluates the derivative four times per step. Its local truncation error is order `h⁵`; its global error is order `h⁴`. It is not an adaptive or implicit RK method, and “order four” does not guarantee accuracy for every equation or step size.

## 3. Development history

The history below is inferred from the repository's Git commit subjects and current source; it is a high-level chronology, not a claim that each commit introduced a complete feature.

1. **Initial expression and Euler work.** Early commits created equation parsing, allowed-element and symbol validation, evaluation of `f(x,y)`, and Euler stepping (`090c07c`, `d880b5f`, `0322202`, `43b111f`). The expression evaluator and numerical loop form the foundation still used by every method.
2. **More integrators.** Commits added modified Euler/Heun, RK4, and Ralston (`c3fa63c`, `b5845bb`, `4bcbd5e`). Midpoint and the second-order variants followed.
3. **Shared RK2 architecture.** The project refactored Heun, Midpoint, and Ralston into parameterized `rk2()` instead of maintaining three nearly identical algorithms (`7263d85`, `54223c6`).
4. **Reusable solve and comparison path.** Solver orchestration and comparison were introduced (`a944608`, `c3d4ba5`, `d1d936e`). Current code registers methods in `METHODS_REGISTRY`, so a named method is called through one common loop.
5. **User-facing output and persistence.** Method reference, richer terminal tables, smoother input flow, JSON export, and a fix to remove spurious imaginary residue during symbolic evaluation appear in later history (`d27c3be`, `54ac3be`, `9132394`, `0e93919`, `ae3ceb6`). Plotting and persistent settings round out the command-line workflow.

Useful history commands for a deeper audit:

```sh
git log --oneline --reverse
git log --oneline -- src/methods.py src/solver.py src/parser.py
git show <commit>
```

## 4. End-to-end execution

### 4.1 Start and choose an action

`main.py` loads persisted settings, shows the banner, then enters a menu loop. Menu maps live in `src/constants.py`; `get_menu_choice()` in `src/input_handler.py` converts a selection to an action string. The main loop retains the current problem, most recent single-method history, comparison results, and last plot in module-level variables.

### 4.2 Enter a problem and parse the right-hand side

The “New Problem” path calls `get_all_inputs()`:

1. `get_equation()` reads the right-hand side of `dy/dx = ...`.
2. `is_valid_charset()` rejects an empty expression, expressions over 200 characters, and characters outside its configured set.
3. `safe_parse()` calls SymPy `parse_expr` with implicit multiplication and `^`-to-power transformations, binding `x` and `y` as symbols.
4. `has_valid_symbols()` requires at least one free symbol and limits free symbols to `x` and `y`.
5. Numeric prompts collect `x0`, `y0`, `target_x`, and `h`; current input validation requires `h > 0`.
6. `collect_initial_values()` packages those values in a dictionary. If auto-save is on, `save_problem()` appends the problem to CSV, TXT, and JSON files.

For a numerical derivative evaluation, `src/parser.py:f()` substitutes the current numeric `x` and `y` into the SymPy expression, evaluates it numerically, takes the real component, and converts that component to Python `float`. Thus the numerical methods receive a scalar real derivative.

### 4.3 Integrate with one method

For “Solve”, `main.py` looks up the method name and calls:

```python
solve_with_method(method_name, equation, x0, y0, target_x, h)
```

`src/solver.py` resolves the function from `METHODS_REGISTRY`, initializes history to `[(x0, y0)]`, computes `n_steps = round((target_x - x0) / h)`, then invokes the selected step function `n_steps` times. Each returned point becomes the start of the next step and is appended to history. `display_solution()` prints every stored pair in a Rich table and reports the final point.

### 4.4 Compare methods

`compare_methods()` iterates through `METHODS_REGISTRY` and calls the same `solve_with_method()` for each key. It returns a mapping from method name to history. The UI can display final values, or ask the user for a scalar exact value at the target and show absolute differences `abs(y_approx - exact)`. That input is a value, not a symbolic exact solution function, and the comparison report only compares final values.

When auto-save is active, comparison histories are appended to `data/solutions.json`. Plots use the histories already held in memory: a single method or all comparison curves. Graph saving renders a PNG under `data/graphs/`.

### 4.5 Export and settings

`src/exporter.py` serializes problem metadata to `data/problems.csv`, `data/problems.txt`, and `data/problems.json`; comparison histories go to `data/solutions.json`. `src/settings.py` owns user preferences such as display precision, colors, auto-save, and graph style, saved under `data/settings.json`. These paths are relative to the process working directory. The `data/` directory is runtime output and may be created by the relevant save path.

## 5. Implementation map

| File | Responsibility |
|---|---|
| `main.py` | Menu loop, state for the current problem/results, dispatch to features. |
| `src/parser.py` | Expression checks, SymPy parsing, numerical evaluation of the derivative. |
| `src/input_handler.py` | Menu and numeric prompts, problem input dictionary. |
| `src/methods.py` | Euler, generic RK2, Heun, Midpoint, Ralston, RK4 step functions. |
| `src/solver.py` | Method registry, fixed-step integration loop, method comparison. |
| `src/display.py` | Rich solution/comparison tables and messages. |
| `src/exporter.py` | CSV, TXT, JSON persistence. |
| `src/graph.py` | Plot construction and PNG saving. |
| `src/constants.py` | Menu options and in-app method reference text. |
| `src/settings.py` | Settings load/save and accessors. |

## 6. Behavioral boundaries to know

- **Step count is rounded.** The loop uses `round((target_x - x0) / h)` but always advances by exactly `h`. If the distance is not an integer multiple of `h`, the final `x` can differ from `target_x`. A ratio below one-half can produce zero steps. Python's `round` also uses ties-to-even behavior.
- **Backward integration is not supported by the prompt.** `h` must be positive. If `target_x < x0`, the calculated step count is negative, and `range(n_steps)` performs no iterations; the returned history contains only the initial point.
- **No adaptive error control.** The solver does not check local error, enforce tolerances, or shrink a step near difficult regions. Users choose the fixed step size.
- **Expression parser guardrails are limited.** The project applies a character allowlist and symbol check before numerical work. SymPy's `parse_expr` is not a general-purpose security sandbox; the current character check is not a substitute for a purpose-built safe expression grammar. Treat expressions as trusted input when running in an untrusted environment.
- **Real component is selected.** `f()` converts the real component of the evaluated result to `float`; it does not reject a nonzero imaginary component or explicitly diagnose singular/non-finite values. The intended problem domain is real-valued scalar ODEs.
- **Persistence assumes writable paths.** Export files are relative to the working directory, and current export functions expect the `data/` directory to exist for problem exports.

These details describe current behavior and are useful when interpreting outputs; they are not claims about desired future behavior.

## 7. Extending the solver

To add a method, implement a step function in `src/methods.py` with the same `(equation, x, y, h) -> (next_x, next_y)` contract, import it in `src/solver.py`, and add it to `METHODS_REGISTRY`. Add its menu entry in `src/constants.py` and reference information in `METHOD_INFO` if it should appear in the UI. Since comparison iterates the registry, the new method then participates in comparison automatically. Keep the method's formula and error order accurate for the assumptions under which it is intended to be used.
