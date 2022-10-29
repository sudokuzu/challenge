import IP2Location
import os

IP2LocObj = IP2Location.IP2Location();
IP2LocObj.open("IP-COUNTRY.BIN");
rec = IP2LocObj.get_all(os.environ["REMOTE_ADDR"]);

if rec.country_short == "FR":
    print "Status: 301 Moved Permanently"
    print "Location: http://JUMP.COM"
    print