from math import sin, radians, cos, asin, sqrt
from .exceptions import NotofTypeFloat, IncorrectLngLat, IncorrectDeltaCalculation

def calculate_distance_of_aircraft(lat1: float, lng1: float, lat2: float, lng2: float) -> float: 
    """
    # To-Do: Use tuple unpacking instead of arguments to make code cleaner? 
    # To-Do: Think of any other mathmatical errors we could see
    Calculate the distance from two sets of geographic cordinates and return their distance from each other. 
    Source of equation: https://en.wikipedia.org/wiki/Great-circle_distance 
    Steps: 
    1. Convert lat and long to radian
    2. Get difference of lat long
    3. Calculate archav of two cordinates
    4. Return archave * radius of earth
    """
    
    # Check to make sure our lat and lng cordinates make sense and are of type float
    validation_list = [lat1, lng1, lat2, lng2]
    for i in validation_list: 
        if not isinstance(i, float): 
            raise NotofTypeFloat
        elif (i < -90 or i > 90) or (i > 180 or i < -180):
            raise IncorrectLngLat

    # Convert lat and lng to radians
    lat1, lat2, lng1, lng2 = map(radians, [lat1, lat2, lng1, lng2])

    d_long = lng2 - lng1
    d_lat = lat2 - lat1

    # Find the angle 
    a = sin(d_lat/2)**2 + cos(lat1) * cos(lat2) * sin(d_long/2)**2
    r_earth = 3958.8 # Radius of Earth w/ decimal for more accuracy
    if a < 0: 
        raise IncorrectDeltaCalculation
    c = 2 * asin(sqrt(a))

    return c * r_earth
