"""This file will only store values that are constant."""

PROGRAM_NAME = "Numerical ODE sovler"

MAIN_MENU = {
    1: "new",
    2: "solve",
    3: "compare",
    4: "plot",
    5: "info",
    6: "settings",
    7: "help",
    8: "exit"
}

METHODS_MENU = {
    1: "euler",
    2: "heun",
    3: "midpoint",
    4: "ralston",
    5: "rk4"
}

COMPARE_MENU = {
    1: "all",
    2: "exact"
}

PLOT_MENU = {
    1: "numerical",
    2: "exact",
    3: "both"
}

SETTINGS = {
    1: "precision",
    2: "colour",
    3: "save_res",
    4: "graph_style",
    5: "return"
    
}

METHOD_INFO = {
    "euler": {
        "name": "Euler Method",
        "formula": "y(n+1) = y(n) + h * f(x(n), y(n))",
        "order": "1st order — Global error O(h)",
        "description": (
            "The simplest numerical method for solving ODEs. It uses the slope "
            "at the current point (x(n), y(n)) to step forward, assuming the "
            "slope stays constant over the interval. Only one function "
            "evaluation per step, but error accumulates quickly since it "
            "ignores curvature in the solution. Good as a baseline to compare "
            "against higher-order methods."
        ),
    },

    "heun": {
        "name": "Modified Euler / Heun's Method",
        "formula": (
            "predictor: y~(n+1) = y(n) + h * f(x(n), y(n))\n"
            "corrector: y(n+1) = y(n) + (h/2) * [f(x(n), y(n)) + f(x(n+1), y~(n+1))]"
        ),
        "order": "2nd order — Global error O(h^2)",
        "description": (
            "A predictor-corrector method. It first predicts the next point "
            "using standard Euler, then corrects the estimate by averaging "
            "the slope at the start and the (predicted) end of the interval. "
            "Equivalent to applying the trapezoidal rule to the ODE. More "
            "accurate than Euler at the cost of one extra function evaluation "
            "per step."
        ),
    },

    "midpoint": {
        "name": "Midpoint Method",
        "formula": (
            "k1 = f(x(n), y(n))\n"
            "k2 = f(x(n) + h/2, y(n) + (h/2) * k1)\n"
            "y(n+1) = y(n) + h * k2"
        ),
        "order": "2nd order — Global error O(h^2)",
        "description": (
            "Instead of averaging the slopes at both endpoints like Heun's "
            "method, this evaluates the slope at the midpoint of the "
            "interval, using a half-step Euler prediction to get there. Same "
            "order of accuracy as Heun's method, but with a different error "
            "constant — the two aren't numerically identical even at "
            "matching step sizes."
        ),
    },

    "ralston": {
        "name": "Ralston's Method",
        "formula": (
            "k1 = f(x(n), y(n))\n"
            "k2 = f(x(n) + (2/3)*h, y(n) + (2/3)*h*k1)\n"
            "y(n+1) = y(n) + h * [(1/4)*k1 + (3/4)*k2]"
        ),
        "order": "2nd order — Global error O(h^2)",
        "description": (
            "Another member of the second-order Runge-Kutta family (like "
            "Heun's and Midpoint), but with alpha = 2/3 and weights 1/4, 3/4. "
            "Ralston chose these specific coefficients in 1962 to minimize "
            "the bound on local truncation error among all possible "
            "second-order RK methods, making it the theoretically most "
            "accurate two-stage RK2 variant, even though it shares the same "
            "overall order as Heun's and Midpoint methods."
        ),
    },

    "rk4": {
        "name": "RK4 (Classical Runge-Kutta)",
        "formula": (
            "k1 = f(x(n), y(n))\n"
            "k2 = f(x(n) + h/2, y(n) + (h/2)*k1)\n"
            "k3 = f(x(n) + h/2, y(n) + (h/2)*k2)\n"
            "k4 = f(x(n) + h, y(n) + h*k3)\n"
            "y(n+1) = y(n) + (h/6) * (k1 + 2*k2 + 2*k3 + k4)"
        ),
        "order": "4th order — Global error O(h^4)",
        "description": (
            "The classical Runge-Kutta method and the standard default ODE "
            "solver for most practical use. Uses four slope evaluations per "
            "step, weighted to cancel out lower-order error terms. Doubling "
            "the number of steps roughly divides error by 16, making it the "
            "best accuracy-to-cost tradeoff among these five methods."
        ),
    },
}