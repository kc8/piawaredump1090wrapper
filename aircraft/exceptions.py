# To - Do: Create custom exceptions for the query logic 

class BaseTypeError(TypeError):
    """
    Base TypeError for calculating distance
    """
    pass

class NotofTypeFloat(BaseTypeError): 
    """
    Cordinates are not of type float. 
    """
    pass

class IncorrectLngLat(BaseTypeError):
    """
    Lat and Long cordinates are not valid
    """
    pass

class IncorrectDeltaCalculation(BaseTypeError): 
    """
    The Delta caluclation was incorrect. This could mean the delta was negative.
    """
    pass