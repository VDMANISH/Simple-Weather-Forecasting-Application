import requests
import json

# OpenWeatherMap API key
api_key = "4b463278862eba6e4cbf1df5e2a82d73"  # Replace with your API key

while True:
    city_name = input("Enter city name (or type 'exit' to quit): ").strip()   # Prompt the user for a city name
    if city_name.lower() == "exit":
        print("Exiting the application. Goodbye!")
        break
    # Construct the API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    try:
        
        response = requests.get(url)   # Send a request to the OpenWeatherMap API
        response.raise_for_status()    # Check for HTTP request errors
        weather_data = response.json() # Parse the response into JSON format

        # Extract the necessary weather information
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        # Display the weather details
        print(f"\nWeather in {city_name.title()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s\n")

    except requests.exceptions.HTTPError as err:
        print(f"Error: {err}")
    except json.JSONDecodeError:
        print("Error: Failed to parse weather data.")
    except KeyError:
        print("Error: Invalid weather data format. Please try a different city.")
      
#####################

# import requests
# import json

# # API key for OpenWeatherMap
# api_key = "4b463278862eba6e4cbf1df5e2a82d73"  # Replace with your own API key

# # Asks the user for a city name
# city_name = input("Enter city name: ")

# # Construct the API URL with the city name and API key
# url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

# try:
#     # Send a request to the API and get the response
#     response = requests.get(url)
#     response.raise_for_status()  # Raise an error if the request was unsuccessful

#     # Parse the JSON response into a Python dictionary
#     weather_data = response.json()

#     # Extract the temperature and weather description
#     temperature = weather_data["main"]["temp"]
#     description = weather_data["weather"][0]["description"]

#     # Display the weather information
#     print(f"Weather in {city_name}:")
#     print("Temperature:", temperature)
#     print("Description:", description)

# except requests.exceptions.HTTPError as err:
#     print("Error:", err)
# except json.JSONDecodeError:
#     print("Error: Failed to parse weather data.")
# except KeyError:
#     print("Error: Invalid weather data format.")
