import math
import re


def to_dec_degrees(
        theta,
        from_radians=True,
        from_degs_mins_secs=False,
        from_gradians=False,
        from_turns=False
        ):
    """
    It takes an angle given in the following units: degrees-minutes-seconds, radians, gradians and turns;
    and returns the angle converted in decimal degrees.
    Angles must be provided as 'int' or 'float', denoting the magnitude with no unit,
    except for degrees-minutes-seconds, which is to be 'str' pattern DdMM'SS'' or D°MM'SS''.
    """

    arguments_False_by_default = list(locals().values())[-3:]

    if any(arguments_False_by_default):

        try:
            assert arguments_False_by_default.count(True) == 1

        except AssertionError:
            raise TypeError(
                "Unit error; more than one unit requested for converting.\nOnly one supported.")

    if from_degs_mins_secs:

        try:
            assert type(theta) == str and re.fullmatch("[0-9]+[d" + str(chr(176)) + "][0-9]{2}'[0-9]{2}.*[0-9]*''",
                                                       theta)

        except AssertionError:
            raise TypeError(
                "Angle ", theta,
                " class type not supported; not matching correct format.",
                "Requested numeric type and degrees, minutes, seconds pattern(D",
                str(chr(176)), "MM'SS'') or (DdMM'SS''")

        if str(chr(176)) in theta:
            separator = str(chr(176))

        else:
            separator = "d"

        degs_mins_secs = theta.split(separator)
        degrees = float(degs_mins_secs[0])
        minutes = float(degs_mins_secs[1].split("'")[0])
        seconds = float(degs_mins_secs[1].split("'")[1])
        return round(degrees + (minutes / 60) + (seconds / 3600), 15)
