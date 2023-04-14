import time
import urllib.request
import json
offset = 1
count = 1
while count <=39:
    path = "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&" + 'offset=' + str(offset)
    token_header = {"token": "JaNcfAcWzvrGevzkwhWSzVEqwUwGFgGi"}
    output = urllib.request.Request(path, headers=token_header)
    with urllib.request.urlopen(output) as f:
        json_object = json.load(f)
    with open(f"json/location{count}.json", "w") as f:
        json.dump(json_object, f)
    count += 1
    offset += 1000
    time.sleep(2)



