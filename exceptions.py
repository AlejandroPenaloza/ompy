class UnitError(Exception):
    
    """
    Creation of UnitError, implemented when an exception must be raised in case of a wrong class type 
    (TypeError) or a not supported value (ValueError) is passed according to the unit features.
    """
    
    def __init__(self, unit=None, message="Class type or value not supported for unit to use."):
        self.unit = unit
        self.message = message
        super().__init__(self.message)


class SexagesimalError(UnitError):
    pass


class SexagesimalFeatureError(SexagesimalError):
    pass
