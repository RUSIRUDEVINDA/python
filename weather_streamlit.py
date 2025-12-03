import streamlit as st
import requests

st.set_page_config(page_title="Weather Checker", page_icon="⛅")

API_KEY = "34a0d78a075fa35398ebc64d9380d745"  #API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

st.title("⛅ Weather Checker")
st.write("Enter a city name to check the current weather 🌍")

city = st.text_input("City Name")

if st.button("Get Weather"):
    if city:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            st.success(f"Weather in **{city.capitalize()}** 🌞")
            st.metric("Temperature (°C)", f"{temp}°C")
            st.metric("Humidity", f"{humidity}%")
            st.metric("Wind Speed", f"{wind_speed} m/s")

            st.write(f"**Description:** _{weather.capitalize()}_")

        else:
            st.error("City not found ❌ Try again!")
    else:
        st.warning("Please enter a city name first 🏙")
