# Aircraft PiAware and DUMP1090 API and wrapper 


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
``` 
from aircraft import Aircraft
from queryscanner import QueryScanner

q = QueryScanner("RPI_IP_ADDR_AS_STRING")
aircraft = q.get_all_aircraft()

for i in aircraft: 
    print(i)
    
```

# To-Do

- [ ] Setup a docs for reference
- [ ] Improve setup.py and requirements
- [ ] Better exception handling- 
- [ ] Implement generator function for querying
- [ ] Fixes "To-Dos" throughout code base