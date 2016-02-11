from geocode.geocode import GeoCodeAccessAPI

if __name__ == "__main__":
    api = GeoCodeAccessAPI()
    geocode = api.get_geocode("Atlanta, GA")
    print geocode
