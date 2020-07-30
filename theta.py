import math
import numpy as np
import re
import inspect
from collections import Counter


def to_dec_degrees(theta, from_radians=True, from_degs_mins_secs=False, from_gradians=False, from_turns=False):
    # It takes an angle given in the following units: degrees-minutes-seconds, radians, gradians and turns;
    # and returns the angle converted in degrees.
    # Angles must be provided as 'int' or 'float', denoting the magnitude with no unit,
    # except for degrees-minutes-seconds.

    try:
        assert Counter(re.findall("\[.+]", str(locals().values()))[0][1:-1].split(", "))['True'] == 1

    except AssertionError:
        raise TypeError("Unit error; more than one unit requested for converting.\nOnly one supported.")

    if from_degs_mins_secs:

        try:
            assert type(theta) == str and re.fullmatch("[0-9]+"+str(chr(176))+"[0-9]{2}'[0-9]{2}''", theta)

        except AssertionError:
            raise TypeError("Angle ", theta, " class type not supported; not matching correct format.\n",
                            "Numeric type requested or degrees, minutes, seconds pattern(", str(chr(176)), " ' ''")

        degs_mins_secs = theta.split(str(chr(176)))
        degrees_part = float(degs_mins_secs[0])
        minutes_part = float(degs_mins_secs[1].split("'")[0])
        seconds_part = float(degs_mins_secs[1].split("'")[1])
        return degrees_part + minutes_part + seconds_part

    try:
        assert type(theta) in [int, float]
    except AssertionError:
        raise TypeError("Angle ", theta, " class type not supported; not matching correct format.\n"
                        "Numeric type requested or degrees, minutes, seconds pattern(", str(chr(176)), " ' ''")

    theta = float(theta)
    if from_gradians:
        return 9 * theta / 10

    if from_turns:
        return theta * 360

    else:
        return theta * 180 / math.pi


def to_radians(theta, from_dec_degrees=True, from_degs_mins_secs=False, from_gradians=False, from_turns=False):
    units = np.array([from_dec_degrees, from_degs_mins_secs, from_gradians, from_turns])

    try:
        assert len(units[units == True]) == 1

    except AssertionError:
        raise TypeError("Unit error; more than one unit requested for converting.\nOnly one supported")

    if from_degs_mins_secs:

        try:
            assert type(theta) == str and re.fullmatch("[0-9]+"+str(chr(176))+"[0-9]{2}'[0-9]{2}''", theta)

        except AssertionError:
            raise TypeError("Angle ", theta, " class type not supported; not matching correct format.\n",
                            "Numeric type requested or degrees, minutes, seconds pattern(", str(chr(176)), " ' ''")
        return to_dec_degrees(theta, from_degs_mins_secs=True) * math.pi / 180

    try:
        assert type(theta) in [int, float]

    except AssertionError:
        raise TypeError("Angle ", theta, " class type not supported; not matching correct format.\n"
                        "Numeric type requested or degrees, minutes, seconds pattern(", str(chr(176)), " ' ''")

    theta = float(theta)

    if from_gradians:
        return theta * 2 * math.pi / 400

    if from_turns:
        return theta * 2 * math.pi

    else:
        return theta * math.pi / 180


def to_gradians(theta, from_radians=True, from_dec_degrees=False, from_degs_mins_secs=False, from_turns=False):
    units = np.array([from_radians, from_dec_degrees, from_degs_mins_secs, from_turns])

    try:
        assert len(units[units]) == 1

    except AssertionError:
        raise TypeError("Unit error; more than one unit requested for converting.\nOnly one supported")

    if from_degs_mins_secs:

        try:
            assert type(theta) == str and re.fullmatch("[0-9]+"+str(chr(176))+"[0-9]{2}'[0-9]{2}''", theta)

        except AssertionError:
            raise TypeError("Angle ", theta, " class type not supported; not matching correct format.\n",
                            "Numeric type requested or degrees, minutes, seconds pattern(", str(chr(176)), " ' ''")

        return to_dec_degrees(theta, from_degs_mins_secs=True) * 10 / 9

    try:
        assert type(theta) in [int, float]

    except AssertionError:
        raise TypeError("Angle ", theta, " class type not supported; not matching correct format.\n"
                                         "Numeric type requested or degrees, minutes, seconds pattern(", str(chr(176)),
                        " ' ''")

    theta = float(theta)

    if from_dec_degrees:
        return theta * 10 / 9

    if from_turns:
        return theta * 400

    else:
        return theta * 200 / math.pi


def to_turns(theta, from_radians=True, from_dec_degrees=False, from_degs_mins_secs=False, from_gradians=False):
    try:
        assert Counter(re.findall("\[.+]", str(locals().values()))[0][1:-1].split(", "))['True'] == 1

    except AssertionError:
        raise TypeError("Unit error, more than one unit requested for converting"
                        "Only one supported")

    if from_gradians:
        return theta / 400

    elif from_radians:
        return theta / (2 * math.pi)

    else:

        if from_degs_mins_secs:
            theta = to_dec_degrees(theta, from_degs_mins_secs=True)
        return theta / 360
