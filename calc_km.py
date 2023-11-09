import requests
from math import radians, sin, cos, sqrt, atan2

def get_coordinates(address):
    params = {
        'address': address,
        'key': 'Your_Google_Maps_API_Key'
    }
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            location = data['results'][0]['geometry']['location']
            latitude = location['lat']
            longitude = location['lng']
            return (latitude, longitude)
    return None

def calculate_distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    R = 6371  # Radius of the Earth in kilometers
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2) * sin(dlat/2) + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2) * sin(dlon/2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    return distance

def main():
    address1 = input("Enter the first address: ")
    address2 = input("Enter the second address: ")

    coord1 = get_coordinates(address1)
    coord2 = get_coordinates(address2)

    if coord1 and coord2:
        distance = calculate_distance(coord1, coord2)
        print(f"The distance between {address1} and {address2} is approximately {round(distance, 2)} kilometers.")
    else:
        print("Failed to retrieve coordinates for the provided addresses.")

if __name__ == "__main__":
    main()
