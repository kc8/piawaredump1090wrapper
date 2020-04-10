from .calculate_distance_of_aircraft import calculate_distance_of_aircraft
from .exceptions import NotofTypeFloat, IncorrectDeltaCalculation, IncorrectLngLat


class Aircraft:
    """
    Airacraft class containg information regarding a single aircraft.
    
    Some notes about arugments:
     Note: maybe we can make another class or method that tracks location? 
     Note: hex is ICAO number. ADSBexchange gives it the name hex. 
     Note: lat and lng have differing names in class verus API
     Note: gs is ground speed. 
     Note: alt_geom is altitude
     icaco_number is used to identify the object when created
    """

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
        self.is_within_distance = None # boolean if within a certain distance
        self.distance_specific_point = None # value from that distance


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
        Compares the two icao numbers and returns. ICAO is the identifies for a unique
        aircarft
        """
        return self.icao_number == other.icao_number
    

    def __key(self): 
        """
        Key for __hash__
        """
        return (self.icao_number)


    def __hash__(self):
        """
        Hashes based on __key, which is the icao number
        """
        hash_val = hash(self.__key())
        print(hash_val) 
        return hash_val


    def update_info(self, **kwargs) -> bool: 
        """
        Updates attirubutes of the airplane. 
        
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
        

    def get_aircraft_within_specific_distance(self, distance: float, lat: float, lng: float) -> float:
        """
        Returns the aircrafts distance from a cente 
        :params:
            distance: The radius to be measured from the central point in lng and lat 
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
            

        if self.distance_specific_point and _dist <= distance:
            self.is_within_distance = True
        else: 
            self.is_within_distance = False
        return _dist
        

    def get_aircraft_info(self) -> tuple: 
        """
        Returns a tuple of all parameters of the aircraft. Some may be "None" 
        if they did not get populated during init. Usually due to lack of 
        information from the ADSB scanner. 
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