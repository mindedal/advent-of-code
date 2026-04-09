from __future__ import annotations

from collections.abc import Sequence
from typing import Any, cast

try:
    import z3  # type: ignore[import-not-found]
except ImportError as exc:  # pragma: no cover - dependency should be installed
    raise ImportError("z3-solver is required. Install with `uv add z3-solver`.") from exc

ArithExpr = z3.ArithRef
Expr = z3.ExprRef
SolverLike = z3.Solver | z3.Optimize
SAT = z3.sat


def make_solver() -> z3.Solver:
    """Create a typed z3 solver instance."""

    return z3.Solver()


def make_optimizer() -> z3.Optimize:
    """Create a typed z3 optimizer instance."""

    return z3.Optimize()


def int_var(name: str) -> z3.ArithRef:
    """Create a typed integer variable."""

    return z3.Int(name)  # pyright: ignore[reportUnknownMemberType]


def add_constraints(solver: SolverLike, *constraints: object) -> None:
    """Add one or more constraints to a solver-like object."""

    cast(Any, solver).add(*constraints)


def sum_expr(terms: Sequence[z3.ArithRef]) -> z3.ArithRef | int:
    """Build a typed sum expression from z3 arithmetic terms."""

    return cast(z3.ArithRef | int, z3.Sum(terms))  # pyright: ignore[reportUnknownMemberType]


def minimize_expr(solver: z3.Optimize, expr: z3.ArithRef | int) -> None:
    """Register an objective on a z3 optimizer."""

    cast(Any, solver).minimize(expr)


def check_solver(solver: SolverLike) -> z3.CheckSatResult:
    """Run satisfiability checking with a typed result."""

    return cast("z3.CheckSatResult", cast(Any, solver).check())


def eval_int(model: z3.ModelRef, expr: z3.ExprRef) -> int:
    """Evaluate an integer-valued expression in a z3 model."""

    value = cast("z3.IntNumRef", cast(Any, model).eval(expr, model_completion=True))
    return int(value.as_long())
