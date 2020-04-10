import requests
from json import loads
from requests import HTTPError
from aircraft import Aircraft 

class QueryScanner:

    def _create_query_url(self):
        """
        Creates the query string for the object and stores it. 
        """
        try: 
            self._query_url = str(self.url) + ":" + str(self.port)
        except TypeError:
            return "Not able to form query URL. Check they are strings and not malformed"


    def __init__(self,
                url="localhost", 
                port="8080",
                stats_api_path="/dump1090-fa/data/stats.json",
                scanner_aircraft_path="/dump1090-fa/data/aircraft.json", 
                **auth,
                ):
        """
        @param:
            url: Url/uri/IP address of the PiAware, default is localhost
            port: port number as string, default is 8080
        """ 
        self.url = url 
        self.auth = None
        self.port = port
        self._query_url = None
        self._stats_api_path = stats_api_path
        self._scanner_aircraft_path = scanner_aircraft_path
        self._create_query_url()


    def __repr__(self): 
        """
        Represent Object and a fall back for __str__
        """
        return f'{self.__class__.__name__}, {self.url}'


    def __eq__(self, other):
        """
        Compaures and return if both objects are of same class and if URLs are the same
        """
        return self.__class__ == other.__class__ and self.url == other.url


    def _auth(self, **auth) -> None:
        """
        Not implemented because there is no need to authorize to API 
        Need to research more into this, left this here as a reminder
        
        """
        return None
    

    def get_sensor_stats(self) -> None: 
        """
        Returns the status of the Raspberry Pi Sensor. Not yet implemented
        URL is: .../dump1090-fa/data/stats.json
        Part of a To-Do is to implment this. 
        @return
            Dictionary of stats. 
        """
        return None

    def _query(self, _specific_api_url: str) -> dict:
        """
        Queries the API. Function is to reduce code duplications
        :Return: Response object as json
        """
        url = self._query_url + _specific_api_url
        try:
            r = requests.get(url)
            r = r.json()
        except HTTPError as e:
            raise e
        except ValueError as e :
            raise e

        return r


    def get_all_aircraft(self) -> [Aircraft]:
        """
        Returns list of all aircraft scanner has seen regardless of whether it 
        has received all Aircraft information (such as tail number or Flight #)
        :return: List of Airfract seen by the receiver
        """ 
        _raw_aircraft_data = self._query(self._scanner_aircraft_path)

        # List of attributes from aircraft JSON. Is there a better way? 
        _response_keys = [
            'hex',
            'flight',
            'squawk',
            'lat',
            'lon',
            'alt_geom', #altitude
            'geom_rate',
            'track',
            'gs',
            'seen' ,
        ]

        known_aircarft = []
        _parameters = {}
        # To-Do: n^2, need something better instead of brute force,
        # (Replace with generator? )
        for i in _raw_aircraft_data['aircraft']:
            for k in _response_keys:
                try:
                    _parameters.update({k : i[k]})
                except KeyError: # Data was not picked up by reciever
                    pass  
            known_aircarft.append(Aircraft(**_parameters))
            _parameters = {}
        return known_aircarft