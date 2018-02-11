import requests

def get_data():
    "Gets api data"
    ship_api_url = "https://app.uhds.oregonstate.edu/api/webcam/ship"
    request_data = requests.get(ship_api_url)
    return request_data.json()

def convert_c_to_f(temp):
    "Converts Celsius to Fahrenheit."
    conversion = round(9.0 / 5.0 * temp + 32, 2)
    return conversion

def convert_knot_to_mph(knot):
    "Converts wind from knots to mph"
    conversion = round(1.1507 * knot, 2)
    return conversion

def format_data(data_to_format):
    "Formats the data how we want it"
    formatted = """
    Air Temp [{0} F] Water Temp [{1} F]
    Wind [{2} mph] Depth [{3} meters]
    Lat [{4}] Long [{5}]    
    Current Location: https://www.google.com/maps/place/{4},{5}
    *note* You may need to zoom out on the map to see the relative location!
    """.format(convert_c_to_f(data_to_format['air_temp']),
               convert_c_to_f(data_to_format['water_temp']),
               convert_knot_to_mph(data_to_format['wind']),
               data_to_format['depth'], data_to_format['lat'], data_to_format['lng'])
    return formatted

data = get_data()
latest_dataset = data[0]
print(format_data(latest_dataset))
