import streamlit as st
import requests
import pandas as pd

# Set the page title
st.set_page_config(
    page_title="OpenWeather API Data",
    page_icon=":partly_sunny:",
    layout="wide"
)

# Streamlit title and description
st.title("OpenWeather API Data")
st.write("This app fetches and displays weather data from the OpenWeather API.")

# User input for city name
city_name = st.text_input('Enter city name:', 'New York')  # Default city name is "New York"

# API configuration
api_key = 'eef94865433aba6d8689c10961915c02'  # Replace with your OpenWeather API key
base_url = 'http://api.openweathermap.org/data/2.5/weather'

# Display weather data when the user clicks the "Get Weather" button
if st.button('Get Weather'):
    # API request parameters
    params = {'q': city_name, 'appid': api_key, 'units': 'metric'}  # 'units' for temperature in Celsius

    # Make the API request
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        
        # Create a DataFrame from the JSON data
        df = pd.json_normalize(data)

        # Display the DataFrame using pandas
        st.write(df)
    else:
        st.error(f"Error: Unable to retrieve weather data. Status code: {response.status_code}")

# Display a footer with attribution to OpenWeatherMap
st.markdown("Data provided by [OpenWeatherMap](https://openweathermap.org/).")



# Display a footer with attribution to OpenWeatherMap
st.markdown("Data provided by [OpenWeatherMap](https://openweathermap.org/).")

