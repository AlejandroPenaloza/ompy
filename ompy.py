import math
import re


def are_bool(tuple_arg):

    if type(tuple_arg) != tuple:
        raise TypeError(
            "Class type not supported; tuple expected."
        )

    item_not_bool = False
    for item in tuple_arg:
        if type(item) != bool:
            item_not_bool = True
            break

    return not item_not_bool
  

def to_dec_degrees(
    theta, 
    from_radians=True, 
    from_degs_mins_secs=False, 
    from_gradians=False, 
    from_turns=False
    ):
  
    """
    It takes an angle given in the following units: degrees-minutes-seconds,
    radians, gradians and turns; and returns the angle converted in decimal degrees.
    Angles must be provided as 'int' or 'float', denoting the magnitude with 
    no unit, except for degrees-minutes-seconds, which is to be 'str' pattern 
    DdMM'SS'' or D°MM'SS''.
    """
    
    unit_arguments = [
        False if type(argument) == bool else True for argument in list(locals().values())[1:]
                      ]
    
    if any(unit_arguments):
        
        raise TypeError(
            "Class type not supported; use only 'True' or 'False' as arguments for current angle units to convert."
        )

    arguments_False_by_default = list(locals().values())[2:5]

    if any(arguments_False_by_default):
        # checking on how many units were passed as True

        try:
            assert arguments_False_by_default.count(True) == 1

        except AssertionError:
            raise TypeError(
                "Unit error; more than one unit requested for converting.\nOnly one supported.")
    
    if from_degs_mins_secs:
        #Angle conversion from degrees, minutes and seconds

        try:
            assert type(theta) == str and re.fullmatch(
                "[0-9]+[d"+str(chr(176))+"][0-5][0-9]'[0-5][0-9].*[0-9]*''", theta)

        except AssertionError:
            raise TypeError(
                "Angle ", theta, 
                " class type not supported; not matching correct format or out of numeric range.",
                "Requested numeric type and degrees, minutes, seconds pattern(D", 
                str(chr(176)), "MM'SS'') or (DdMM'SS''"
                )
            
        if str(chr(176)) in theta:
            separator = str(chr(176))

        else:
            separator = "d"

        degs_mins_secs = theta.split(separator)
        degrees = float(degs_mins_secs[0])
        minutes = float(degs_mins_secs[1].split("'")[0])
        seconds = float(degs_mins_secs[1].split("'")[1])
        return round(degrees + (minutes/60) + (seconds/3600), 15)

    try:

      assert type(theta) == int or type(theta) == float

    except AssertionError:
        raise TypeError(
            "Angle", theta, "class type not supported.\n'int' or 'float' expected."
        )

    theta = float(theta)

    if from_gradians:
        # Angle conversion from gradians
        
        return 9 * theta / 10

    if from_turns:
        # Angle conversion from turns

        return theta * 360

    else:
        # Angle conversion from radians

        return theta * 180 / math.pi


class Def:

    def __init__(self, value):
        self.value = value


def to_radians(
    theta, 
    from_dec_degrees=Def(True), 
    from_degs_mins_secs=False, 
    from_gradians=False, 
    from_turns=False
    ):
    
    """
    It takes an angle given in the following units: degrees-minutes-seconds,
    radians, gradians and turns; and returns the angle converted in decimal degrees.
    Angles must be provided as 'int' or 'float', denoting the magnitude with 
    no unit, except for degrees-minutes-seconds, which is to be 'str' pattern 
    DdMM'SS'' or D°MM'SS''.
    """
    
    unit_arguments = tuple(locals().values()[1:])

    if from_dec_degrees is to_radians.__defaults__[0]:
        unit_arguments = unit_arguments[1:]

    if not are_bool(unit_arguments):
        raise TypeError(
            "Class type not supported; use only 'True' or 'False' as arguments for current angle units to convert."
        )

    if unit_arguments.count(True) >= 2:
        raise ValueError(
            "Unit error; more than one unit requested for converting.\nOnly one supported."
        )
