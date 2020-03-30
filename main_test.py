from aircraft import Aircraft
from queryscanner import QueryScanner

q = QueryScanner("http://192.168.1.140")
aircraft = q.get_all_aircraft()

for i in aircraft: 
    print(i)
