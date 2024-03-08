def address_to_coordinates(address):
    # importing geopy library and Nominatim class
    from geopy.geocoders import Nominatim

    # calling the Nominatim tool and create Nominatim class
    loc = Nominatim(user_agent="Geopy Library")

    # entering the location name
    getLoc = loc.geocode(address)

    if getLoc:
        # Return latitude and longitude
        return getLoc.latitude, getLoc.longitude
    else:
        # Return None if the location is not found
        return None, None
