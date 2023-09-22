import streamlit as st
import requests
import os
import json


# Replace 'your_api_key_here' with your actual OpenWeatherMap API key
os.environ['MM_open_weather'] = 'eef94865433aba6d8689c10961915c02'
# Set the page title
st.set_page_config(
    page_title="Weather Now",
    page_icon=":partly_sunny:",  # You can use emojis as icons
    layout="wide",  # Adjust the layout
    initial_sidebar_state="expanded"  # Expand the sidebar by default
)

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
            # Create a DataFrame to store weather data
            weather_data = {
                "Attribute": ["City", "Description", "Temperature (°C)", "Humidity (%)"],
                "Value": [data['name'], data['weather'][0]['description'], data['main']['temp'], data['main']['humidity']]
            }

            df = pd.DataFrame(weather_data)

            # Display weather icon
            weather_icon = data['weather'][0]['icon']
            st_icon(weather_icon, width=100)

            # Display the DataFrame using pandas
            st.table(df)
        else:
            st.error(f"Error: Unable to retrieve weather data. Status code: {response.status_code}")


