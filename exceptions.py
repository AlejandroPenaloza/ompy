def check_types(input_var, types_sup, msg=None, exception=TypeError):

    if type(input_var) not in types_sup and msg:
        raise exception(msg)

    elif type(input_var) not in types_sup and not msg:
        raise exception

    else:
        pass

def check_vals(input_var, values_sup, msg=None, exception=ValueError):

    if input_var not in values_sup and msg:
        raise exception(msg)

    elif input_var not in values_sup and not msg:
        raise exception

    else:
        pass


class UnitError(Exception):
    
    """
    Exception raised when a wrong class type (TypeError) or a not
    supported value (ValueError) is passed, according to the unit features.
    """
    
    def __init__(self, unit=None, message="Class type or value not supported for unit to use."):
        self.unit = unit
        self.message = message
        super().__init__(self.message)


class SexagesimalError(UnitError):

    pass


class SexagesimalFeatureError(SexagesimalError):

    """
    Exception raised when angle features in sexagesimal unit are not matched.

    [KeyError]; from returning value (defaultdict type) wrong keys called; from function 'to_sexagesimal'.
    """

    pass
