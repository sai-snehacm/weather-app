import requests

# ----------------------------
# WEATHER APP USING API
# ----------------------------

API_KEY = "https://wttr.in"  # Free weather API


def get_weather(city):
    try:
        print(f"\nFetching weather for {city}...")
        url = f"{API_KEY}/{city}?format=j1"
        response = requests.get(url)

        if response.status_code != 200:
            print("Could not fetch data. Try again.")
            return

        data = response.json()

        # Extract useful information
        area = data["nearest_area"][0]["areaName"][0]["value"]
        region = data["nearest_area"][0]["region"][0]["value"]
        country = data["nearest_area"][0]["country"][0]["value"]
        temp = data["current_condition"][0]["temp_C"]
        feels = data["current_condition"][0]["FeelsLikeC"]
        humidity = data["current_condition"][0]["humidity"]

        print("\n--- Weather Report ---")
        print(f"Location : {area}, {region}, {country}")
        print(f"Temperature : {temp}°C")
        print(f"Feels Like : {feels}°C")
        print(f"Humidity : {humidity}%")
        print("----------------------\n")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
