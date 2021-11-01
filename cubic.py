import math
import numpy as np
import re
import inspect
from collections import Counter


def cbrt(radicand):

    """
    Returns the real cubic root -principal value- of a real number.
    :param radicand: int, float; required. Number to take the root of.
    :return: float; cubic root.
    """

    radicand = float(radicand)

    if radicand < 0:
        return round((-1)*abs(radicand**(1/3)), 12)

    else:
        return round(radicand**(1/3), 12)


def cb_depressed(a, b, c, d):

    """
    Transforms a general cubic equation to a depressed cubic equation.
    It takes general coefficients 'a', 'b', 'c', 'd' and returns depressed coefficients 'p', 'q'.
    :param a: int, float; required (it cannot be 0).
    :param b: int, float; required.
    :param c: int, float; required.
    :param d: int, float; required.
    :return: tuple. [0]: coefficient 'p'. [1]: coefficient 'q'.
    """

    p = (c / a) - (b ** 2) / (3 * (a ** 2))
    q = 2 * (b / (3 * a)) ** 3 - (b * c) / (3 * (a ** 2)) + d / a
    return p, q


def cbdelta(p, q):

    """
    Calculates the cubic discrimant (delta) for a depressed cubic equation.
    :param p: int, float; required. Coefficient 'p' from depressed equation.
    :param q: int, float; required. Coefficient 'q' from depressed equation.
    :return: float; cubic delta number.
    """

    p = float(p)
    q = float(q)
    return (q**2) + ((4*(p**3))/27)


def cb_depressed_roots(p, q):

    """
    For depressed, or reduced, cubic equations returns a tuple with its roots.
    :param p: int, float; required. Coefficient 'p' from depressed equation.
    :param q: int, float; required. Coefficient 'q' from depressed equation.
    :return: tuple.
        [0]: str; first root. Corresponding to a real number.
        [1]: str; seconds root. Corresponding to a real or complex number.
        [2]: str; third root. Corresponding to a real or complex number.
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


def cb_roots_str(a, b, c, d):

    """
    Calculates cubic general equation roots.
    :param a: int, float, required (cannot be 0). Equation coefficient 'a'.
    :param b: int, float; required. Equation coefficient 'b'.
    :param c: int, float; required. Equation coefficient 'c'.
    :param d: int, float; required. Equation coefficient 'd'.
    :return: tuple.
        [0]: str. First root, corresponding to a real number.
        [1]: str. Second root, corresponding to a real or complex number.
        [2]: str. Third root, corresponding to a real or complex number.
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
