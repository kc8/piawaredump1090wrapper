from .calculate_distance_of_aircraft import calculate_distance_of_aircraft
from .exceptions import NotofTypeFloat, IncorrectDeltaCalculation, IncorrectLngLat
"""
Airacraft class that holds information a single aircraft
"""

class Aircraft:

    # Note: maybe we can make another class or method that tracks location? 
    # Note: hex is ICAO number. ADSBexchange gives it the name hex. 
    # Note: lon is lng in class. Similar to how hex is setup
    # gs: Ground Speed. alt_geom = altitude
    #   Use icaco_number to access
    def __init__(self, hex,
                flight=None, 
                squawk=None, 
                lat=None, 
                lon=None,
                alt_geom=None, 
                geom_rate=None, 
                track=None, 
                gs=None, 
                seen=None,
                *args,
                **kwargs,):
        self.icao_number = hex
        self.flight = flight 
        self.squawk = squawk
        self.lat = lat 
        self.lng = lon
        self.altitude = alt_geom 
        self.ver_rate = geom_rate 
        self.track = track 
        self.speed = gs 
        self.seen = seen
        self.is_within_distance = None # boolean if i
        self.distance_specific_point = None # value from distance


    def __repr__(self): 
        """
        :Returns: Flight number if available or ICACO number
        """
        if self.flight is not None:
            return f'{self.flight}'
        else: 
            return f'{self.icao_number}'
    
    
    def __str__(self):
        """
        :Returns: Flight number if available or ICACO number
        """
        if self.flight is not None:
            return f'{self.flight}'
        else: 
            return f'{self.icao_number}'


    def __eq__(self, other):
        """
        Compares on ICAO number not registration number since the registration may not have 
        populated from the request. 
        """
        return self.icao_number == other.icao_number
    

    def __key(self): 
        """
        Key for __hash__
        """
        return (self.icao_number)


    def __hash__(self):
        hash_val = hash(self.__key())
        print(hash_val) 
        return hash_val
    
    """
    # Override the setattr method as we do not want to have custom or accidental __dict__[names]
    def __setattr__(self, name, value): 
        if self.__dict__[name]:
            self.__dict__[name] = value
            return True
    
        return False
    """

    def update_info(self, **kwargs) -> bool: 
        """
        Updates attirubutes of the airplane. 
        This method should not update the hex (ICAO) number
        :param: 
            **kwargs: Dictionary of values to update
        :return: Boolean value if update was sucessful or not
        """
        #: To-do: Check if an attributes exists before adding it. 
        if not kwargs: 
            return False

        for key, value in kwargs.items(): 
            setattr(self, key, value)
        return True
        
    def get_aircraft_within_specific_distance(self, distance: int, lat: float, lng: float) -> float:
        """
        Returns a list of aircraft within the specific distance from the cordinates prodivded. 
        :params:
            distance: The radius to be measured from lng and lat as the central point
            lng: Longitude of location
            lat: Latitude of location
        """
        _dist = None
        try:
            _dist = calculate_distance_of_aircraft(lat, lng, self.lat, self.lng)
            self.distance_specific_point = _dist
        except NotofTypeFloat as err:
            self.distance_specific_point = None
        except IncorrectLngLat as err:
            self.distance_specific_point = None
        except IncorrectDeltaCalculation as err: 
            self.distance_specific_point = None
            # To-Do: Log Exception error

        if self.distance_specific_point and _dist <= distance:
            self.is_within_distance = True
        else: 
            self.is_within_distance = False
        return _dist
        

    def get_aircraft_info(self) -> tuple: 
        """
        Returns a tuple of all parameters of the aircraft. Some may be "None" or a 
        similar value if they did not get populated during init. Usually due to lack of 
        information from the ADSB scanner"
        :param: None
        :return: Tuple of all characteristics of the aircraft
        """
        return (
        f'ICAO#: {self.icao_number}, \
        Flight#: {self.flight}, \
        SQUAWK: {self.squawk}, \
        LAT: {self.lat}, \
        LNG: {self.lng}, \
        ALT: {self.altitude}ft, \
        VERT_RATE: {self.ver_rate}, \
        TRACK: {self.track}, \
        SPEED: {self.speed}kt, \
        SEEN: {self.seen}, \
        ')