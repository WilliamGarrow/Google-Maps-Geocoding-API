# Google Maps Geocoding API
Python wrapper for Google Maps Geocoding API

This is a basic Python wrapper ideation for the Google Maps Geocoding API. 

Geocoding is the process of converting addresses (like "1600 Amphitheatre Parkway, Mountain View, CA") into geographic coordinates (like latitude 37.423021 and longitude -122.083739), which you can use to place markers on a map, or position the map. Reverse geocoding is the process of converting geographic coordinates into a human-readable address. The Google Maps Geocoding API's reverse geocoding service also lets you find the address for a given place ID. The Google Maps Geocoding API provides a direct way to access these services via an HTTP request. https://developers.google.com/maps/documentation/geocoding/intro

Note: The Java and Python client libraries should probably supersede this basic approach. https://developers.google.com/maps/web-services/client-library

__Virtualenv Setup:__

* Create and activate [virtual environment](https://virtualenv.readthedocs.org/en/latest/userguide.html).
* Install requirements `pip install -r /requirements.txt`

__Example Usage:__
`geo_code = GeoCodeAccessAPI(address="Atlanta, GA")`

__Accessing latitude/longitude or Address:__
`lat = geo_code.lat`
`lng = geo_code.lng`
`address = geo_code.address`
