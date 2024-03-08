import arrow
import requests
from address_to_coordinates import address_to_coordinates


# Get the current hour
current_hour = arrow.now().floor('hour')

# Get the address from the user
address = input("Where would you like to check the weather? :")

# Get the latitude and longitude of the address
latitude, longitude = address_to_coordinates(address)

# Checking lattitude and longitude
# print(latitude, longitude)

# Check if the address is found
if latitude is None or longitude is None:
    print("The address is not found.")
    exit()

try:
    response = requests.get(
        'https://api.stormglass.io/v2/weather/point',
        params={
            'lat': latitude,
            'lng': longitude,
            'params': ','.join(['airTemperature','pressure','humidity','snowDepth','visibility','windSpeed', 'windWaveDirection','gust']),
            'start': current_hour.to('UTC').timestamp(),  # Start from the current hour
            'end': current_hour.to('UTC').timestamp(),   # End on the current hour
            #'end': current_hour.shift(hours=1).to('UTC').timestamp(),  # End one hour later
            'source': 'sg',
        },
        headers={
            'Authorization': 'f65ddbec-9279-11ee-950b-0242ac130002-f65ddc64-9279-11ee-950b-0242ac130002'
        }
    )
    
    # Check for successful response
    response.raise_for_status()

    # Saving response to json_data
    json_data = response.json()

    # Example of raw json_data
    #print(json_data)

    # Extracting data from json_data
    hours_data = json_data.get('hours', [])

    for hour in hours_data:
        air_temperature = hour.get('airTemperature', {}).get('sg')
        gust = hour.get('gust', {}).get('sg')
        humidity = hour.get('humidity', {}).get('sg')
        pressure = hour.get('pressure', {}).get('sg')
        snow_depth = hour.get('snowDepth', {}).get('sg')
        time = hour.get('time')
        visibility = hour.get('visibility', {}).get('sg')
        wind_speed = hour.get('windSpeed', {}).get('sg')
        wind_wave_direction = hour.get('windWaveDirection', {}).get('sg')

        output = (
            f"Time: {time}\n"
            f"Air Temperature: {air_temperature}\n"
            f"Gust: {gust}\n"
            f"Humidity: {humidity}\n"
            f"Pressure: {pressure}\n"
            f"Snow Depth: {snow_depth}\n"
            f"Visibility: {visibility}\n"
            f"Wind Speed: {wind_speed}\n"
            f"Wind Wave Direction: {wind_wave_direction}\n"
        )
        print(output)

except requests.exceptions.RequestException as req_err:
    print(f"Request Exception: {req_err}")



