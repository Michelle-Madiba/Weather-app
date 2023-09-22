import streamlit as st
import requests
import os
import json
import pandas as pd

# Set the page title
st.set_page_config(
    page_title="Weather Now",
    page_icon=":partly_sunny:",  # You can use emojis as icons
    layout="wide",  # Adjust the layout
    initial_sidebar_state="expanded"  # Expand the sidebar by default
)

# Set Streamlit title
st.title("Weather NOW")

os.environ['MM_open_weather'] = 'eef94865433aba6d8689c10961915c02'
# Retrieve the OpenWeatherMap API key from the environment variable
openweather_api = os.environ.get('MM_open_weather')
if not openweather_api:
    st.warning("Please set the 'MM_open_weather' environment variable with your API key.")
else:
    # Ask the user to input the city name
    location = st.text_input('Enter city name:')

    if st.button('Get Weather'):
        # Set the base URL for the OpenWeatherMap API
        base_url = 'http://api.openweathermap.org/data/2.5/weather?q='  # Updated API endpoint

        # Set the API key
        api_key = openweather_api

        # Create the URL for the API request
        url = f'{base_url}{location}&appid={api_key}&units=metric'  # Added units parameter for Celsius

        # Send the request to the API
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the JSON response
            data = json.loads(response.text)

            # Check if 'name' key exists in the response (indicating a valid city)
            if 'name' in data:
                # Create a DataFrame to store weather data
                weather_data = {
                    "Attribute": ["City", "Description", "Temperature (°C)", "Humidity (%)"],
                    "Value": [data['name'], data['weather'][0]['description'], data['main']['temp'], data['main']['humidity']]
                }

                df = pd.DataFrame(weather_data)

                # Display weather icon
                weather_icon = data['weather'][0]['icon']
                st.image(f'http://openweathermap.org/img/wn/{weather_icon}.png', width=100)  # Display weather icon

                # Display the DataFrame using pandas
                st.table(df)
            else:
                st.error(f"Error: City not found.")
        else:
            st.error(f"Error: Unable to retrieve weather data. Status code: {response.status_code}")

