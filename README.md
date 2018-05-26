# The closest bars 

There are diferrent data on the cite data.mos.ru. You find Moscow bars
[https://data.mos.ru/opendata/7710881420-bary]
 (https://data.mos.ru/opendata/7710881420-bary) and donwload its in file.json.

There write a script which accounts: the biggest bar, the smallest bar, the closest bar
(there need to point your gps-coordinate).</pre>

 # Quickstart

The example of script launch on Linux, Python 3.5 and you need bars.json, which can be downloaded from  [https://data.mos.ru/opendata/7710881420-bary](https://data.mos.ru/opendata/7710881420-bary)

# How to use 

``` $ python3 bars.py ```


You can print data like this: 

Input coordinate longitude:1
Input coordinate latitude:1
The closest bar is
{'Name': 'Staropramen', 'AdmArea': 'Центральный административный округ', 'IsNetObject': 'нет', 'Address': 'Садовая-Спасская улица, дом 19, корпус 1', 'ID': '00146638', 'Latitude_WGS84': '55.3033000000000000', 'global_id': 281494712, 'PublicPhone': [{'global_id': 34992.0, 'global_object_id': 281494712.0, 'system_object_id': '00146638 _1', 'PublicPhone': '(985) 069-34-47'}], 'SeatsCount': 50, 'TypeObject': 'бар', 'geoData': {'type': 'Point', 'coordinates': [36.900000000253, 55.303299999814]}, 'system_object_id': '00146638', 'Longitude_WGS84': '36.9000000000000000', 'District': 'Красносельский район', 'SocialPrivileges': 'нет'}


 # Project Goals

 The code is written for educational purposes. Training course for web-developers - 
[DEVMAN.org](https://devman.org))
