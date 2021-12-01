import math
from fractions import *
import re
import inspect
from collections import Counter
from .exceptions import check_types, check_vals


def F(num, get="fraction"):
    """
    Transforms a number (int or float) to a Fraction object or , by passing it as
    str first so it is a more accurate value.
    """

    ct_unsup_excep_msg = "Class type not supported; only int, float or fractions.Fraction object expected."
    check_types(num, (int, float, fractions.Fraction), ct_unsup_excep_msg)
    vals_unsup_excep_msg = f"{num} not supported; options are 'numerator', 'denominator', 'asfloat' and 'asstr'."
    check_vals(get, ("fraction", "numerator", "denominator", "asfloat", "asstr"), vals_unsup_excep_msg)

    if type(num) != fractions.Fraction:
        num = Fraction(str(num))

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
    radicand: int, float; required. Number to take the root of.

    Returns
    -------
    float; cubic root.
    """

    radicand_type_exc_msg = "class type not supported; only int, float or fractions.Fraction object expected."
    check_types(radicand, (int, float, fractions.Fraction), radicand_type_exc_msg)
    radicand = F(radicand)

    if radicand < 0:
        rt = round((-1) * abs(radicand ** (1 / 3)), 12)

    else:
        rt = round(radicand ** (1 / 3), 12)

    return rt


def to_depressed(a, b, c, d):

    """
    Transforms a general cubic equation to a depressed cubic equation.
    It takes general coefficients 'a', 'b', 'c', 'd' and returns depressed coefficients 'p', 'q'.

    Parameters
    ----------
    a: int, float; required (it cannot be 0).
    b: int, float; required.
    c: int, float; required.
    d: int, float; required.

    Returns
    -------
    tuple. Depressed equation coefficients.
    [0]: coefficient 'p'.
    [1]: coefficient 'q'.
    """

    coefs_type_exc_msg = "Class type not supported; int, float or fractions.Fraction object expected."

    for coef in (a, b,c, d):
        check_types(coef, (int, float, fractions.Fraction), coefs_type_exc_msg)

    a, b, c, d = F(a), F(b), F(c), F(d)
    coef_p = (c / a) - (b ** 2) / (3 * (a ** 2))
    coef_q = 2 * (b / (3 * a)) ** 3 - (b * c) / (3 * (a ** 2)) + d / a

    coef_p = round(F(coef_p, get="asfloat"), 12)
    coef_q = round(F(coef_q, get="asfloat"), 12)
    return coef_p, coef_q


def cbdelta(p, q):

    """
    Calculates the cubic discriminant (delta) for a depressed cubic equation.

    Parameters
    ----------
    p: int, float; required. Coefficient 'p' from depressed equation.
    q: int, float; required. Coefficient 'q' from depressed equation.

    Returns
    -------
    float; cubic delta number.
    """

    p = float(p)
    q = float(q)
    return (q**2) + ((4*(p**3))/27)


def depressed_roots(p, q):

    """
    For depressed, or reduced, cubic equations returns a tuple with its roots.

    Parameters
    ----------
    p: int, float; required. Coefficient 'p' from depressed equation.
    q: int, float; required. Coefficient 'q' from depressed equation.

    Returns
    -------
    tuple. Equation roots.
        [0]: str; first root, represents a real number.
        [1]: str; second root, represents a real or complex number.
        [2]: str; third root, represents a real or complex number.
    """

    p = float(p)
    q = float(q)
    delta = cbdelta(p, q)

    if delta > 0:
        z1 = round(cbrt(0.5*(-q + math.sqrt(delta))) + cbrt(0.5*(-q - math.sqrt(delta))), 11)
        real_part = -0.5*z1
        imaginary_part = round(0.5*math.sqrt(3*(z1**2) + 4*p), 11)
        z2 = str(real_part) + " + " + str(imaginary_part) + "i"
        z3 = str(real_part) + " - " + str(imaginary_part) + "i"
        z1 = str(z1)
        return z1, z2, z3

    elif delta == 0:
        z1 = str(round(cbrt(-4*q), 11))
        z2 = str(round(cbrt(4*q)/2, 11))
        z3 = z2
        return z1, z2, z3

    else:
        angle = math.acos(-q * 0.5 * math.sqrt(27 / (-p ** 3))) / 3
        z1 = str(round(2 * math.sqrt(-p / 3) * math.cos(angle), 11))
        z2 = str(round(2 * math.sqrt(-p / 3) * math.cos(angle + 2 * math.pi / 3), 11))
        z3 = str(round(2 * math.sqrt(-p / 3) * math.cos(angle + 4 * math.pi / 3), 11))
        return z1, z2, z3


def roots(a, b, c, d):

    """
    Calculates cubic general equation roots.

    Parameters
    ----------
    a: int, float, required (cannot be 0). Equation coefficient 'a'.
    b: int, float; required. Equation coefficient 'b'.
    c: int, float; required. Equation coefficient 'c'.
    d: int, float; required. Equation coefficient 'd'.

    Returns
    -------
    tuple. Equation roots.
        [0]: str. First root, represents a real number.
        [1]: str. Second root, represents a real or complex number.
        [2]: str. Third root, represents a real or complex number.
    """


    a, b, c, d = float(a), float(b), float(c), float(d)
    variable_change = -b/(3*a)
    p = (c / a) - (b ** 2) / (3 * (a ** 2))
    q = 2 * (b / (3 * a)) ** 3 - (b * c) / (3 * (a ** 2)) + d / a
    cor_depressed_eq_roots = cb_depressed_roots(p, q)
    delta = cbdelta(p, q)

    if delta < 0:
        x1 = str(round(float(cor_depressed_eq_roots[0]) + variable_change, 10))
        x2 = str(round(float(cor_depressed_eq_roots[1]) + variable_change, 10))
        x3 = str(round(float(cor_depressed_eq_roots[2]) + variable_change, 10))
        return x1, x2, x3

    elif delta == 0:
        x1 = str(round(float(cor_depressed_eq_roots[0]) + variable_change, 10))
        x2 = str(round(float(cor_depressed_eq_roots[1]) + variable_change, 10))
        x3 = str(round(float(cor_depressed_eq_roots[2]) + variable_change, 10))
        return x1, x2, x3

    else:
        z1 = cbrt(0.5*(-q + math.sqrt(delta))) + cbrt(0.5*(-q - math.sqrt(delta)))
        real_part = -0.5*z1
        imaginary_part = 0.5*math.sqrt(3*(z1**2) + 4*p)
        x1 = str(round(z1 + variable_change, 10))
        x2 = str(round(real_part + variable_change, 10)) + " + " + str(round(imaginary_part, 10)) + "i"
        x3 = str(round(real_part + variable_change, 10)) + " - " + str(round(imaginary_part, 10)) + "i"
        return x1, x2, x3
