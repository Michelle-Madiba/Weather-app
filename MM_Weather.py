import streamlit as st
import requests
import os
import json

# Set Streamlit title
st.title("Weather NOW")

# Retrieve the OpenWeatherMap API key from the environment variable
openweather_api = os.environ.get('MM_open_weather')
if not openweather_api:
    st.warning("Please set the 'MM_open_weather' environment variable with your API key.")
else:
    # Ask the user to input the city name
    location = st.text_input('Enter city name:')

    if st.button('Get Weather'):
        # Set the base URL for the OpenWeatherMap API
        base_url = 'http://api.openweathermap.org/geo/1.0/direct?q='
        #{city name},{state code},{country code}{limit}&appid={API key}

        # Set the API key
        api_key = openweather_api

        # Create the URL for the API request with 'q' parameter for the city name
        url = base_url  + location + '&limit=3'+'&appid=' + api_key

        # Send the request to the API
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the JSON response
            data = json.loads(response.text)

            # Display the weather data using Streamlit
            st.write(f"Weather in {data['name']}: {data['weather'][0]['description']}")
            st.write(f"Temperature: {data['main']['temp']}°C")
            st.write(f"Humidity: {data['main']['humidity']}%")
        else:
            st.error(f"Error: Unable to retrieve weather data. Status code: {response.status_code}")

