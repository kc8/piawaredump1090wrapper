# PiAware and DUMP1090 Python Request wrapper 

**Application is still in testing and development. If you have suggestions, comments or want to help out feel free to open a PR or submit an issue.**

This is a Python wrapper for the piaware/dump1090 ADBS library. This module requests information from the Raspberry Pi via a RESTful request. Returning a list of all aircraf the PiAware is reading. 

You will need local LAN access to a Piaware enabled device. 

# Requirments
- Python 3.7+ 
- Python Requests Library
- An active and working FlightAware/ Piaware with dump1090 (You can get started here: https://flightaware.com/adsb/piaware/)
- **Make sure to have alook in the requirments.txt file for additional dependencies** 

# Setup  
- run setup.py. In venv or other
```python3 setup.py install ```

# Sample Usuage
```python
from aircraft import Aircraft
from queryscanner import QueryScanner

q = QueryScanner("http://RPI_IP_ADDR_AS_STRING")
aircraft = q.get_all_aircraft()

for i in aircraft: 
    print(i)
    
```

# To-Do

- [ ] Setup a docs for reference
- [ ] Fix some typos
- [ ] Improve setup.py and requirements
- [ ] Better exception handling- 
- [ ] Implement generator function for querying 
- [ ] Fixes "To-Dos" throughout code base
- [ ] When calling aircraft.update() method should not update the hex (ICAO) number as it is unique per aircraft. Implement method that will throw/return error and override the __setattr__ method? 
- [ ] Implement custom exceptions on aircraft distance calculation while continuing to set attrs to None. 
- [ ] Try to implement tuple unpacking or a cleaner way to take arugments for the calucluate_distance_of_aircraft method
- [ ] Check calculation for any mathmetical errors when computed? Need to read more about this equation to do so? Is there something more accurate? Is this a concern? 
- [ ] Do we need to check for any more errors in the input values of calculate_distance_of_airacft?
- [ ] Implment testing (waiting on this as I am working on a firebase project for this)
- [ ] Create exception for QueryScanner._create_query_url() if the url is invalid. Should sanatize this data more? 
- [ ] In Query Scanner there is an _auth method. Need to see if some PiAwares have a method of authorization. 
- [ ] Implement ability to get the status of the PiAware. This should be just an fstring dump of the date as it would be out of scope to relay on this for that information (maybe make a seperate model?)
- [ ] Using n^2 method for querying data in get_all_aircraft(). I was able to improve a feature that queried the reciever twice for something, now need to work on improving this for effieceny. 
- [ ] Need to improve on exception handinling in get_all_aircraft()