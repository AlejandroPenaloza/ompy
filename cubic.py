import math
import fractions
import sympy as sp
import re
import inspect
from collections import Counter
from .exceptions import check_types, check_vals


def _f(
    num,
    get="fraction"
):

    """
    Transforms a number (int or float) to a Fraction object or , by passing it as
    str first so it is a more accurate value.
    """

    ct_unsup_excep_msg = "Class type not supported; only int, float or fractions.Fraction object expected."
    check_types(num, (int, float, fractions.Fraction), ct_unsup_excep_msg)

    vals_unsup_excep_msg = f"{num} not supported; options are 'numerator', 'denominator', 'asfloat' and 'asstr'."
    check_vals(get, ("fraction", "numerator", "denominator", "asfloat", "asstr"), vals_unsup_excep_msg)

    if type(num) != fractions.Fraction:
        num = fractions.Fraction(str(num))

    num_n = num.numerator
    num_d = num.denominator

    if get == "numerator":

        return num_n

    elif get == "denominator":

        return num_d

    elif get == "asfloat":

        return num_n / num_d

    elif get == "asstr":

        return f"{num_n}/{num_d}"

    else:

        return num


def cbrt(radicand):

    """
    Calculates the real cubic root -principal value- of rational representations
    of real numbers.

    Parameter
    ---------
    radicand: int, float, fractions.Fraction; required. Number to take the root of.

    Returns
    -------
    float; cubic root.
    """

    global _radicand_type_exc_msg
    _radicand_type_exc_msg = "class type not supported; int, float or fractions.Fraction object expected."
    check_types(radicand, (int, float, fractions.Fraction), _radicand_type_exc_msg)
    radicand = _f(radicand)

    if radicand < 0:
        rt = round((-1) * abs(radicand ** (1 / 3)), 12)

    else:
        rt = round(radicand ** (1 / 3), 12)

    return rt


def to_depressed(
    coef_a,
    coef_b,
    coef_c,
    coef_d
):

    """
    Transforms a general cubic equation to a depressed cubic equation.
    It takes general coefficients 'a', 'b', 'c', 'd' and returns depressed coefficients 'p', 'q'.

    Parameters
    ----------
    coef_a: int, float; required (it cannot be 0).
    coef_b: int, float; required.
    coef_c: int, float; required.
    coef_d: int, float; required.

    Returns
    -------
    tuple. Depressed equation coefficients.
    [0]: coefficient 'p'.
    [1]: coefficient 'q'.
    """

    for coef in (coef_a, coef_b, coef_c, coef_d):
        check_types(coef, (int, float, fractions.Fraction), _coefs_type_exc_msg)

    a, b, c, d = _f(coef_a), _f(coef_b), _f(coef_c), _f(coef_d)
    coef_p = (c / a) - (b ** 2) / (3 * (a ** 2))
    coef_q = 2 * (b / (3 * a)) ** 3 - (b * c) / (3 * (a ** 2)) + d / a
    coef_p = round(_f(coef_p, get="asfloat"), 12)
    coef_q = round(_f(coef_q, get="asfloat"), 12)

    return coef_p, coef_q


def cbdelta(
    coef_p,
    coef_q,
    as_frac=False
):

    """
    Calculates the cubic discriminant (delta) for a depressed cubic equation.

    Parameters
    ----------
    coef_p: int, float; required. Coefficient 'p' from depressed equation.
    coef_q: int, float; required. Coefficient 'q' from depressed equation.
    as_frac: bool (True or False); optional. False by default. Object type to be returned.

    Returns
    -------
    Cubic delta number.
    fractions.Fration object if as_frac passed as True, float otherwise.
    """

    _as_frac_type_exc_msg = "Bool expected; True if delta required as fractions.Fraction object or False for float."

    for coef in (coef_p, coef_q):
        check_types(coef, (int, float, fractions.Fraction), _coefs_type_exc_msg)

    check_vals(as_frac, (True, False), _as_frac_type_exc_msg)

    p, q = _f(coef_p), _f(coef_q)
    delta = (q ** 2) + ((4 * (p ** 3)) / 27)

    if as_frac:
        delta = _f(delta)

    else:
        delta = _f(delta, get="asfloat")

    return delta


def depressed_roots(
        coef_p,
        coef_q,
        symbolic=False
):

    """
    For depressed, or reduced, cubic equations returns a tuple with its roots.

    Parameters
    ----------
    coef_p  : int, float, fractions.Fraction object; required. Coefficient 'p' from depressed equation.
    coef_q  : int, float, fractions.Fraction object; required. Coefficient 'q' from depressed equation.
    symbolic: bool (True or False); optional. For requesting symbolic math output. False by default.

    Returns
    -------
    tuple. Equation roots.
        [0]: str; first root, represents a real number.
        [1]: str; second root, represents a real or complex number.
        [2]: str; third root, represents a real or complex number.
    """

    global _symbolic_exc_msg
    _symbolic_exc_msg = "Bool expected; True if symbolic mathematics output required or False for strings output."
    check_vals(symbolic, (True, False), _symbolic_exc_msg)

    delta = cbdelta(coef_p, coef_q, True)
    p, q = _f(coef_p), _f(coef_q)

    if delta > 0:
        z1 = cbrt(0.5 * (-q + math.sqrt(delta))) + cbrt(0.5 * (-q - math.sqrt(delta)))
        imaginary_part = math.sqrt(3 * (z1 ** 2) + 4 * p) * 0.5
        imaginary_part = str(round(_f(imaginary_part, "asfloat"), 11))
        z1 = round(_f(z1, "asfloat"), 11)
        real_part = str(-0.5 * z1)
        z2 = real_part + " + " + imaginary_part + "i"
        z3 = real_part + " - " + imaginary_part + "i"
        z1 = str(z1)

        if symbolic:
            z1, sym_real, sym_imry = sp.symbols(z1 + " " + real_part + " " + imaginary_part)
            z2 = sym_real + sym_imry * sp.I
            z3 = sym_real - sym_imry * sp.I
            return display(z1, z2, z3)

    elif delta == 0:
        z1 = _f(cbrt(-4 * q), "asfloat")
        z1 = str(round(z1, 11))
        z2 = _f(cbrt(4 * q) / 2, "asfloat")
        z2 = str(round(z2, 11))
        z3 = z2

        if symbolic:
            z1, z2, z3 = sp.symbols(z1 + " " + z2 + " " + z3)

            return display(z1, z2, z3)

    else:
        formula_angle = math.acos(-q * _f(0.5) * _f(math.sqrt(27 / (-p ** 3)))) / 3
        z1 = str(round(2 * math.sqrt(-p / 3) * math.cos(formula_angle), 11))
        z2 = str(round(2 * math.sqrt(-p / 3) * math.cos(_f(formula_angle) + 2 * _f(math.pi) / 3), 11))
        z3 = str(round(2 * math.sqrt(-p / 3) * math.cos(_f(formula_angle) + 4 * _f(math.pi) / 3), 11))

        if symbolic:
            z1, z2, z3 = sp.symbols(z1 + " " + z2 + " " + z3)

            return display(z1, z2, z3)

    return z1, z2, z3


def roots(
    coef_a,
    coef_b,
    coef_c,
    coef_d,
    symbolic=False
):

    """
    Calculates cubic general equation roots.

    Parameters
    ----------
    coef_a  : int, float, required (cannot be 0). Equation coefficient 'a'.
    coef_b  : int, float; required. Equation coefficient 'b'.
    coef_c  : int, float; required. Equation coefficient 'c'.
    coef_d  : int, float; required. Equation coefficient 'd'.
    symbolic: bool (True or False); optional. For requesting symbolic math output. False by default.

    Returns
    -------
    tuple. Equation roots.
        [0]: str. First root, represents a real number.
        [1]: str. Second root, represents a real or complex number.
        [2]: str. Third root, represents a real or complex number.
    """

    for coef in (coef_a, coef_b, coef_c, coef_d):
        check_types(coef, (int, float, fractions.Fraction), _coefs_type_exc_msg)

    check_vals(symbolic, (True, False), _symbolic_exc_msg)

    a, b, c, d = _f(coef_a), _f(coef_b), _f(coef_c), _f(coef_d)
    variable_change = -b / (3 * a)
    corresp_p = (c / a) - (b ** 2) / (3 * (a ** 2))
    corresp_q = 2 * (b / (3 * a)) ** 3 - (b * c) / (3 * (a ** 2)) + d / a
    cor_depressed_eq_roots = depressed_roots(corresp_p, corresp_q)
    delta = cbdelta(corresp_p, corresp_q)

    if delta <= 0:
        x1 = str(round(float(cor_depressed_eq_roots[0]) + variable_change, 11))
        x2 = str(round(float(cor_depressed_eq_roots[1]) + variable_change, 11))
        x3 = str(round(float(cor_depressed_eq_roots[2]) + variable_change, 11))

        if symbolic:
            x1, x2, x3 = sp.symbols(x1 + " " + x2 + " " + x3)

            return display(x1, x2, x3)

    else:
        z1 = cbrt(0.5*(-corresp_q + _f(math.sqrt(delta)))) + cbrt(0.5 * (-corresp_q - _f(math.sqrt(delta))))
        real_part = str(round(-0.5 * z1 + variable_change, 11))
        imaginary_part = str(round(0.5 * math.sqrt(3 * (z1 ** 2) + 4 * corresp_p), 11))
        x1 = str(round(z1 + variable_change, 11))
        x2 = real_part + " + " + imaginary_part + "i"
        x3 = real_part + " - " + imaginary_part + "i"

        if symbolic:
            x1, sym_real, sym_imry = sp.symbols(x1 + " " + real_part + " " + imaginary_part)
            x2 = sym_real + sym_imry * sp.I
            x3 = sym_real - sym_imry * sp.I

            return display(x1, x2, x3)

    return x1, x2, x3
