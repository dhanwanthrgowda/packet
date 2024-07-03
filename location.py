import requests

def get_location_from_coordinates(latitude, longitude, api_key="AIzaSyCEHQlY_PD7S_6gDvcuHxvpDlC-6GbP_3c"):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "latlng": f"{latitude},{longitude}",
        "key": api_key
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # Extract city and country from the API response
        if "results" in data and data["results"]:
            result = data["results"][0]
            address_components = result.get("address_components", [])
            city = next((component["long_name"] for component in address_components if "locality" in component["types"]), "Unknown")
            country = next((component["long_name"] for component in address_components if "country" in component["types"]), "Unknown")
            return address_components

    except requests.exceptions.RequestException as e:
        print(f"Error fetching location information: {e}")

    return "Location information not available"
if __name__ == "__main__":
    print(get_location_from_coordinates(latitude="12.9719", longitude="77.5937"))