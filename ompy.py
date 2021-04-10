import math
import re
import numpy as np
import sympy
import traceback
import inspect
from decimal import Decimal
from collections import defaultdict

import .exceptions


def are_bools(tuple_arg):

    """
    are_bools
    ---------

    - Param: tuple_arg. Tuple, required.
    - Returns: bool. True if all items in tuple_arg are booleans. False otherwise. 
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
    from_sexagesimal=False, 
    from_gradians=False, 
    from_turns=False,
    from_radians=True
):

  
    """
    Converts the provided angle into decimal degrees.
    
    
    Parameters
    ----------
    theta            : int, float or str; required. 
        Angle to convert. If provided as str, current unit has to be sexagesimal system as 
        respective input is to be "DdMM'SS''" or "DdMM'SS''" pattern; where D could be any-digits number 
        (under supported range), MM (whole num) and SS (could be decimal) are a 1-2 digit number lower than 60.

    from_sexagesimal : bool; default False.
        Select it (pass True) if current unit to convert from is degrees, minutes 
        and seconds (sexagesimal measurement system).

    from_gradians    : bool; default False.
        Select it (pass True) if current unit to convert from is gradians.

    from_turns       : bool; default False.
        Select it (pass True) if current angle to convert from is number of turns/revolutions.

    from_radians     : bool; default True.
        Select it (pass True) if current unit to convert from is radians.


    Returns
    ----------
    float; original angle now in decimal degrees.
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
    passed_True_unit_args = re.findall("True", passed_unit_args)

    if len(passed_True_unit_args) >= 2:

        raise ValueError(
            "Unit error; more than one unit requested for converting.\nOnly one supported."
        )
    
    if from_sexagesimal:
        # Angle conversion from sexagesimal angle measurement (degrees, minutes and seconds).

        sexagesimal_pattern = f"[0-9]+[d{chr(176)}][0-5]?[0-9]'[0-5]?[0-9]([.][0-9]*)*''"

        if type(theta) != str:
            raise TypeError(
                "Class type not supported; string expected."
            )

        if not re.fullmatch(
            sexagesimal_pattern, theta
        ):
            
            raise ValueError(
                f"Angle {theta} not matching correct format or out of numeric range. " 
                f"Requested numeric type and degrees, minutes, seconds pattern: " 
                f"D{chr(176)}MM'SS'' or DdMM'SS''"
            )    

            
        separator = re.findall(f"[0-9]+[d{chr(176)}]", theta)[0][-1]

        sexagesimal_ = theta.split(separator)
        degrees = float(sexagesimal_[0])
        minutes = float(sexagesimal_[1].split("'")[0])
        seconds = float(sexagesimal_[1].split("'")[1])
        dec_degrees = round(degrees + (minutes/60) + (seconds/3600), 13)
        return dec_degrees

    elif type(theta) not in (int, float):
        
        raise TypeError(
            f"Class type not supported; {theta} int or float expected. "\
            f"If used sexagesimal system, pass from_sexagesimal parameter as True."
        )

    elif from_gradians:
        # Angle conversion from gradians.

        dec_degrees = round(theta * 9 / 10, 13)
        return dec_degrees

    elif from_turns:
        # Angle conversion from decimal degrees.

        dec_degrees = round(theta * 360, 13)
        return dec_degrees

    else:
        # Angle conversion from radians.
        
        dec_degrees = round(theta * 180 / math.pi, 13)
        return dec_degrees


def to_radians(
    theta,
    from_sexagesimal=False,  
    from_gradians=False,
    from_turns=False,
    from_dec_degrees=True
):
    

    """
    Converts the provided angle into radians.
    
    
    Parameters
    ----------
    theta            : int, float or str; required. 
        Angle to convert. If provided as str, current unit has to be sexagesimal system as 
        respective input is to be "DdMM'SS''" or "DdMM'SS''" pattern; where D could be any-digits number 
        (under supported range), MM (whole num) and SS (could be decimal) are a 1-2 digit number lower than 60.

    from_sexagesimal : bool; default False.
        Select it (pass True) if current unit to convert from is degrees, minutes 
        and seconds (sexagesimal measurement system).

    from_gradians    : bool; default False.
        Select it (pass True) if current unit to convert from is gradians.

    from_turns       : bool; default False.
        Select it (pass True) if current angle to convert from is number of turns/revolutions.

    from_dec_degrees : bool; default True.
        Select it (pass True) if current unit to convert from is decimal degrees.


    Returns
    ----------
    float; original angle now in radians.
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
    passed_True_unit_args = re.findall("True", passed_unit_args)

    if len(passed_True_unit_args) >= 2:

        raise ValueError(
            "Unit error; more than one unit requested for converting.\nOnly one supported."
        )
    
    if from_sexagesimal:
        # Angle conversion from sexagesimal angle measurement (degrees, minutes and seconds).

        sexagesimal_pattern = f"[0-9]+[d{chr(176)}][0-5]?[0-9]'[0-5]?[0-9]([.][0-9]*)*''"

        if type(theta) != str:
            raise TypeError(
                "Class type not supported; string expected."
            )

        if not re.fullmatch(
            sexagesimal_pattern, theta
        ):
            
            raise ValueError(
                f"Angle {theta} not matching correct format or out of numeric range. " 
                f"Requested numeric type and degrees, minutes, seconds pattern: " 
                f"D{chr(176)}MM'SS'' or DdMM'SS''"
            )    

            
        separator = re.findall(f"[0-9]+[d{chr(176)}]", theta)[0][-1]

        sexagesimal_ = theta.split(separator)
        degrees = float(sexagesimal_[0])
        minutes = float(sexagesimal_[1].split("'")[0])
        seconds = float(sexagesimal_[1].split("'")[1])
        radians = round((degrees + (minutes / 60) + (seconds / 3600)) * math.pi / 180, 13)
        return radians

    elif type(theta) not in (int, float):
        
        raise TypeError(
            f"Class type not supported; {theta} int or float expected. "\
            f"If used sexagesimal system, pass from_sexagesimal parameter as True."
        )

    elif from_gradians:
        # Angle conversion from gradians.

        radians = round(theta * math.pi / 200, 13)
        return radians

    elif from_turns:
        # Angle conversion from turns / revolutions.

        radians = round(theta * math.pi * 2, 13)
        return radians

    else:
        # Angle conversion from decimal degrees.
        
        radians = round(theta * math.pi / 180, 13)
        return radians


def to_gradians(
    theta,
    from_dec_degrees=False,
    from_sexagesimal=False,
    from_turns=False,
    from_radians=True
):


    """
    Converts the provided angle into centesimal measurement system used in gradians.
    
    
    Parameters
    ----------
    theta            : int, float or str; required. 
        Angle to convert. If provided as str, current unit has to be sexagesimal system as 
        respective input is to be "DdMM'SS''" or "DdMM'SS''" pattern; where D could be any-digits number 
        (under supported range), MM (whole num) and SS (could be decimal) are a 1-2 digit number lower than 60.

    from_dec_degrees : bool; default False.
        Select it (pass True) if current unit from which to convert is decimal degrees.

    from_sexagesimal : bool; default False.
        Select it (pass True) if current unit from which to convert is degrees, minutes 
        and seconds (sexagesimal measurement system).

    from_turns       : bool; default False.
        Select it (pass True) if current unit from which to convert is number of turns / revolutions.

    from_radians     : bool; default True.
        Select it (pass True) if current unit from which to convert is radians.


    Returns
    ----------
    float; original angle now in gradians.
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
    passed_True_unit_args = re.findall("True", passed_unit_args)
    print(passed_True_unit_args)

    if len(passed_True_unit_args) >= 2:

        raise ValueError(
            "Unit error; more than one unit requested for converting. \nOnly one supported."
        )

    if from_sexagesimal:
        # Angle conversion from sexagesimal angle measurement (degrees, minutes and seconds).

        sexagesimal_pattern = f"[0-9]+[d{chr(176)}][0-5]?[0-9]'[0-5]?[0-9]([.][0-9]*)*''"

        if type(theta) != str:
            raise TypeError(
                "Class type not supported; 'str' expected."
            )

        if not re.fullmatch(
            sexagesimal_pattern, theta
        ):
            
            raise ValueError(
                "Angle " + str(theta) +  
                " not matching correct format or out of numeric range. " + 
                "Requested numeric type and degrees, minutes, seconds pattern: D" +  
                str(chr(176)) + "MM'SS'' or DdMM'SS''"
            )
            
        separator = re.findall(f"[0-9]+[d{chr(176)}]", theta)[0][-1]

        sexagesimal_ = theta.split(separator)
        degrees = float(sexagesimal_[0])
        minutes = float(sexagesimal_[1].split("'")[0])
        seconds = float(sexagesimal_[1].split("'")[1])
        gradians = round(10 * (degrees + (minutes/60) + (seconds/3600)) / 9, 13)
        return gradians

    elif type(theta) not in (int, float):
        
        raise TypeError(
            "Angle " + str(theta) + 
            " class type not supported.'int' or 'float' expected. " + 
            "If used sexagesimal system; pass from_sexagesimal parameter as True."
        )

    elif from_radians:
        # Angle conversion from radians.

        gradians = round(200 * theta / math.pi, 13)
        return gradians

    elif from_turns:
        # Angle conversion from turns/revolutions.

        gradians = float(round(400 * theta, 13))
        return gradians

    else:
        # Angle conversion from decimal degrees.

        gradians = round(10 * theta / 9, 13)
        return gradians


def to_turns(
    theta,
    from_dec_degrees=False,
    from_sexagesimal=False,
    from_gradians=False,
    from_radians=True
):

    """
    Converts the provided angle into number of equivalent turns or revolutions.
    
    
    Parameters
    ----------
    theta            : int, float or str; required. 
        Angle to convert. If provided as str, current unit has to be sexagesimal system as 
        respective input is to be "DdMM'SS''" or "DdMM'SS''" pattern; where D could be any-digits number 
        (under supported range), MM (whole num) and SS (could be decimal) are a 1-2 digit number lower than 60.

    from_dec_degrees : bool; default False.
        Select it (pass True) if current unit to convert from is decimal degrees.

    from_sexagesimal : bool; default False.
        Select it (pass True) if current unit to convert from is degrees, minutes 
        and seconds (sexagesimal measurement system).

    from_gradians    : bool; default False.
        Select it (pass True) if current unit to convert from is gradians.

    from_radians     : bool; default True.
        Select it (pass True) if current unit to convert from is radians.


    Returns
    ----------
    float; original angle now in number of turns/revolutions.
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
    passed_True_unit_args = re.findall("True", passed_unit_args)

    if len(passed_True_unit_args) >= 2:

        raise ValueError(
            "Unit error; more than one unit requested for converting.\nOnly one supported."
        )
    
    if from_sexagesimal:
        # Angle conversion from sexagesimal angle measurement (degrees, minutes and seconds).

        sexagesimal_pattern = f"[0-9]+[d{chr(176)}][0-5]?[0-9]'[0-5]?[0-9]([.][0-9]*)*''"

        if type(theta) != str:
            raise TypeError(
                "Class type not supported; string expected."
            )

        if not re.fullmatch(
            sexagesimal_pattern, theta
        ):
            
            raise ValueError(
                f"Angle {theta} not matching correct format or out of numeric range. " 
                f"Requested numeric type and degrees, minutes, seconds pattern: " 
                f"D{chr(176)}MM'SS'' or DdMM'SS''"
            )    

        separator = re.findall(f"[0-9]+[d{chr(176)}]", theta)[0][-1]   

        sexagesimal_ = theta.split(separator)
        degrees = float(sexagesimal_[0])
        minutes = float(sexagesimal_[1].split("'")[0])
        seconds = float(sexagesimal_[1].split("'")[1])
        turns = round((degrees + (minutes/60) + (seconds/3600)) / 360, 13)
        return turns

    elif type(theta) not in (int, float):
        
        raise TypeError(
            f"Class type not supported; {theta} int or float expected. "\
            f"If used sexagesimal system, pass from_sexagesimal parameter as True."
        )

    elif from_dec_degrees:
        # Angle conversion from decimal degrees.

        turns = round(theta / 360, 13)
        return turns


    elif from_gradians:
        # Angle conversion from gradians.

        turns = float(round(theta / 400, 13))
        return turns

    else:
        # Angle conversion from radians.
        
        turns = round(theta / (2 * math.pi), 13)
        return turns


def to_sexagesimal(
    theta,
    from_dec_degrees=False,
    from_gradians=False,
    from_turns=False,
    from_radians=True
):


    """
    Converts the provided angle into the sexagesimal system, where the angle is
    composed by the degrees, minutes and seconds magnitudes; following the pattern 
    D°MM'SS'' (D, MM, SS are the magnitudes; MM and SS are 1-2 digit numbers lower than 60).

    
    Parameters
    ----------
    theta            : int or float; required. 
        Angle to convert.

    from_dec_degrees : bool; default False.
        Select it (pass True) if current unit to convert from is decimal degrees.

    from_gradians    : bool; default False.
        Select it (pass True) if current unit to convert from is gradians.

    from_turns       : bool; default False.
        Select it (pass True) if current unit to convert from is turns/revolutions.
    
    from_radians     : bool; default True.
        Select it (pass True) if current unit to convert from is radians.


    Returns
    ----------
    Original angle now in degrees, minutes and seconds (sexagesimal system).

    defaultdict; consisting on the following key-value pairs:
        dict[str]      : str; converted angle following the pattern D°MM'SS''.
        dict[tuple]    : tuple; converted angle separated by its parts, (degrees, minutes, seconds).
        dict["degrees"]: int; degrees part from converted angle.
        dict["minutes"]: int; minutes part from converted angle.
        dict["seconds"]: float; seconds part from converted angle.
    """


    unit_arguments = tuple(locals().values())[1:]
    
    # Checking whether unit arguments are booleans.
    if not are_bools(unit_arguments): 

        raise TypeError(
            "Class type not supported; use only 'True' or 'False' as " + 
            "arguments for current angle units to convert."
        )

    # Checking whether all unit arguments are False,
    # meaning 'from_dec_degrees' was passed as False.
    if not any(unit_arguments):

        raise ValueError(
            "No angle unit was selected; all units are False."
        )
    
    passed_unit_args = inspect.stack()[1].code_context[0]
    passed_True_unit_args = re.findall("True", passed_unit_args)

    if len(passed_True_unit_args) >= 2:

        raise ValueError(
            "Unit error; more than one unit requested for converting.\nOnly one supported."
        )

    if type(theta) not in (int, float):
        
        raise TypeError(
            f"Class type not supported; {theta} int or float expected. "
        )

        
    if from_dec_degrees:
        # Angle conversion from decimal degrees.
        pass

    elif from_gradians:
        # Angle conversion from gradians.

        theta = round(theta * 0.9, 13)
        return turns

    elif from_turns:
        # Angle conversion from turns.  

        theta = round(theta * 360, 13)  

    else:
        # Angle conversion from radians.
        
        #theta = to_dec_degrees(theta)
        theta = round(theta * 180 / math.pi, 13)
    
    degrees = int(theta)
    minutes = (theta - degrees) * 60
    seconds = round((minutes - int(minutes)) * 60, 12)
    minutes = int(minutes)

    sexagesimal_str = f"{degrees}{chr(176)}{minutes}'{seconds}''"

    sexagesimal_tuple = (
        degrees,
        minutes,
        seconds,
    )

    KeyError_msg = "Key unavailable; only sexagesimal features str, tuple, 'degrees', 'minutes' and 'seconds' expected."


    def sexagesimal_default_factory(): 

        raise KeyError(KeyError_msg)


    sexagesimal = defaultdict(sexagesimal_default_factory)
    sexagesimal[str] = sexagesimal_str
    sexagesimal[tuple] = sexagesimal_tuple
    sexagesimal["degrees"] = degrees
    sexagesimal["minutes"] = minutes
    sexagesimal["seconds"] = seconds
    return sexagesimal
