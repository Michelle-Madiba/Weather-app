

# Set the page title
st.set_page_config(
    page_title="Weather Forecast App",
    page_icon=":partly_sunny:",
    layout="wide"
)

# Streamlit title and description
st.title("Weather Forecast App")
st.write("Select a city to view the 3-hour forecast over 5 days and the weather map.")

# User input for city selection
cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",  # Add more cities here
    # ...
]

selected_city = st.sidebar.selectbox("Select a city:", cities)

# API configuration
api_key = 'YOUR_OPENWEATHER_API_KEY'  # Replace with your OpenWeather API key
base_url = 'http://api.openweathermap.org/data/2.5/forecast'

# API request parameters
params = {'q': selected_city, 'appid': api_key, 'units': 'metric'}  # 'units' for temperature in Celsius

# Make the API request
response = requests.get(base_url, params=params)

if response.status_code == 200:
    # Parse the JSON response into a Python dictionary
    data = response.json()

    # Create a DataFrame from the JSON data
    df = pd.json_normalize(data['list'])

    # Display the DataFrame using pandas
    st.write("3-Hour Forecast for the Next 5 Days:")
    st.write(df)

    # Create a folium map to display weather information
    m = folium.Map(location=[data['city']['coord']['lat'], data['city']['coord']['lon']], zoom_start=10)
    marker_cluster = MarkerCluster().add_to(m)

    for index, row in df.iterrows():
        popup_text = f"{row['dt_txt']}<br>Temperature: {row['main.temp']}°C<br>Description: {row['weather'][0]['description'].capitalize()}"
        folium.Marker([row['coord.lat'], row['coord.lon']], popup=popup_text).add_to(marker_cluster)

    st.write("Weather Map:")
    st.write(m)
else:
    st.error(f"Error: Unable to retrieve weather data. Status code: {response.status_code}")

# Display a footer with attribution to OpenWeatherMap
st.markdown("Data provided by [OpenWeatherMap](https://openweathermap.org/).")


# Display a footer with attribution to OpenWeatherMap
st.markdown("Data provided by [OpenWeatherMap](https://openweathermap.org/).")

