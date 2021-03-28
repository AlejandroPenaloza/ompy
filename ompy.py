import math
import re
import traceback
import inspect


class DefVal:

    def __init__(self, value):
        self.value = value


def are_bools(tuple_arg):

    """
    #### are_bool
    - param: tuple_arg (tuple).
    - returns: True if all items in tuple_arg are booleans. False otherwise.
    """

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
    from_sexagesimal=False, 
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
        # checking on how many units were passed as True.

        try:

            assert arguments_False_by_default.count(True) == 1

        except AssertionError:

            raise TypeError(
                "Unit error; more than one unit requested for converting.\nOnly one supported.")
    
    if from_sexagesimal:
        # Angle conversion from degrees, minutes and seconds.

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

        sexagesimal = theta.split(separator)
        degrees = float(sexagesimal[0])
        minutes = float(sexagesimal[1].split("'")[0])
        seconds = float(sexagesimal[1].split("'")[1])
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
        # Angle conversion from turns.

        return theta * 360

    else:
        # Angle conversion from radians.

        return theta * 180 / math.pi


def to_radians(
    theta, 
    from_dec_degrees=DefVal(True), 
    from_sexagesimal=False, 
    from_gradians=False, 
    from_turns=False
):
    
    """
    It takes an angle given in the following units: degrees-minutes-seconds,
    radians, gradians and turns; and returns a 'float' representing 
    the angle converted in decimal degrees.
    Angles must be provided as 'int' or 'float', denoting the magnitude with 
    no unit, except for degrees-minutes-seconds, which is to be 'str' pattern 
    DdMM'SS'' or D°MM'SS''.
    Decimal degrees is the unit to convert from by default.
    """
    
    unit_arguments = tuple(locals().values())[1:]

    # Checking if 'from_dec_degrees' was passed when function called or is default value.
    if from_dec_degrees is to_radians.__defaults__[0]:
        unit_arguments = unit_arguments[1:]
        #from_dec_degrees = from_dec_degrees.value

    if not are_bools(unit_arguments):

        raise TypeError(
            "Class type not supported; use only 'True' or 'False' as " + 
            "arguments for current angle units to convert."
        )

    if unit_arguments.count(True) >= 2:

        raise ValueError(
            "Unit error; more than one unit requested for converting.\nOnly one supported."
        )
    
    if from_sexagesimal:
        # Angle conversion from sexagesimal angle measurement (degrees, minutes and seconds).

        try:

            assert type(theta) == str and re.fullmatch(
                "[0-9]+[d"+str(chr(176))+"][0-5][0-9]'[0-5][0-9].*[0-9]*''", theta)

        except AssertionError:

            raise TypeError(
                "Angle " + str(theta) +  
                " class type not supported; not matching correct format or out of numeric range. " + 
                "Requested numeric type and degrees, minutes, seconds pattern: D" +  
                str(chr(176)) + "MM'SS'' or DdMM'SS''"
                )
            
        if str(chr(176)) in theta:

            separator = str(chr(176))

        else:

            separator = "d"

        sexagesimal = theta.split(separator)
        degrees = float(sexagesimal[0])
        minutes = float(sexagesimal[1].split("'")[0])
        seconds = float(sexagesimal[1].split("'")[1])
        return round(degrees + (minutes/60) + (seconds/3600), 15)

    try:

        assert type(theta) == int or type(theta) == float

    except AssertionError:

        raise TypeError(
            "Angle " + str(theta) + 
            " class type not supported.'int' or 'float' expected. " + 
            "If used degrees, minutes, seconds unit; set it as True."
        )

    theta = float(theta)

    if from_gradians:
        # Angle conversion from gradians.
        
        return round(9 * theta / 10, 15)

    elif from_turns:
        # Angle conversion from turns.

        return round(theta * 360, 15)

    elif from_dec_degrees:
        # Angle conversion from decimal degrees.

        return round(theta * math.pi / 180, 15)

    else:
        # No unit selected, raise ValueError.

        raise ValueError(
            "No angle unit was selected; all units are False."
        )


def to_gradians(
    theta,
    from_dec_degrees=True,
    from_radians=False,
    from_sexagesimal=False,
    from_turns=False
):

    """
    Converts the provided angle into centesimal measurement system used in gradians.
    
    
    Parameters
    ----------
    theta           : int, float or str; required. 
        Angle to convert. If provided as str, current unit has to be sexagesimal system as 
        respective input is to be "DdMM'SS''" or "DdMM'SS''" pattern (no maximum numerical D).
    from_dec_degrees: bool, default True.
        Select it (True) if current unit from which to convert is decimal degrees.
    from_radians    : bool, default False.
        Select it (True) if current unit from which to convert is radians.
    from_sexagesimal: bool, default False.
        Select it (True) if current unit from which to convert is degrees, minutes 
        and seconds (sexagesimal measurement system).
    from_turns      : bool, default False.
        Select it (True) if current unit from which to convert is turns / revolutions.
    Returns
    ----------
    float, original angle now in decimal degrees.
    """

    unit_arguments = tuple(locals().values())[1:]
    
    # Checking whether unit arguments are booleans.
    if not are_bools(unit_arguments): 

        raise TypeError(
            "Class type not supported; use only 'True' or 'False' as " + 
            "arguments fur current angle units to convert."
        )

    # Checking whether all unit arguments are False,
    # meaning 'from_dec_degrees' was passed as False.
    if not any(unit_arguments):

        raise ValueError(
            "No angle unit was selected; all units are False."
        )

    passed_unit_args = inspect.stack()[1].code_context[0]
    passed_True_unit_args = re.findall("f.+True", passed_unit_args)

    if len(passed_True_unit_args) >= 2:

        raise ValueError(
            "Unit error; more than one unit requested for converting.\nOnly one supported."
        )

    if from_sexagesimal:
        # Angle conversion from sexagesimal angle measurement (degrees, minutes and seconds).

        if type(theta) != str:
            raise TypeError(
                "Class type not supported; 'str' angle required."
            )

        elif not re.fullmatch(
            "[0-9]+[d" + str(chr(176)) + "][0-5][0-9]'[0-5][0-9]([.][0-9]*)*''", theta
        ):
            
            raise ValueError(
                "Angle " + str(theta) +  
                " not matching correct format or out of numeric range. " + 
                "Requested numeric type and degrees, minutes, seconds pattern: D" +  
                str(chr(176)) + "MM'SS'' or DdMM'SS''"
            )
            
        separator = re.findall("[0-9]+[d"+str(chr(176))+"]", theta)[0][-1]

        sexagesimal = theta.split(separator)
        degrees = float(sexagesimal[0])
        minutes = float(sexagesimal[1].split("'")[0])
        seconds = float(sexagesimal[1].split("'")[1])
        gradians = round(10 * (degrees + (minutes/60) + (seconds/3600)) / 9, 15)
        return gradians

    elif type(theta) not in (int, float):
        
        raise TypeError(
            "Angle " + str(theta) + 
            " class type not supported.'int' or 'float' expected. " + 
            "If used sexagesimal system; pass from_sexagesimal parameter as True."
        )

    elif from_radians:
        # Angle conversion from radians.

        gradians = round(200 * theta / math.pi, 15)
        return gradians

    elif from_turns:
        # Angle conversion from turns/revolutions.

        gradians = float(round(400 * theta, 15))
        return gradians

    else:
        # Angle conversion from decimal degrees.

        gradians = round(10 * theta / 9, 15)
        return gradians
