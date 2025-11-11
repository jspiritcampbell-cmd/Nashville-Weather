import random
from datetime import datetime, timedelta

def get_weather_forecast(city_name):
    """
    Generate fake 5-day weather forecast for a given city
    """
    if not city_name or len(city_name.strip()) == 0:
        print(f"❌ Please enter a valid city name.")
        return None
    
    # Generate fake forecast data
    forecast = {
        'time': [],
        'temperature_2m_max': [],
        'temperature_2m_min': [],
        'precipitation_sum': [],
        'weathercode': []
    }
    
    # Generate data for 5 days
    today = datetime.now()
    for i in range(5):
        date = today + timedelta(days=i)
        forecast['time'].append(date.strftime('%Y-%m-%d'))
        
        # Random temperatures (50-85°F high, 35-65°F low)
        high_temp = random.uniform(50, 85)
        low_temp = high_temp - random.uniform(15, 25)
        forecast['temperature_2m_max'].append(high_temp)
        forecast['temperature_2m_min'].append(low_temp)
        
        # Random precipitation (0-20mm)
        forecast['precipitation_sum'].append(random.uniform(0, 20))
        
        # Random weather code
        weather_codes = [0, 1, 2, 3, 45, 51, 61, 63, 71, 80, 95]
        forecast['weathercode'].append(random.choice(weather_codes))
    
    return {
        'city': city_name.title(),
        'forecast': forecast
    }

def get_weather_emoji(code):
    """Convert weather code to emoji"""
    weather_codes = {
        0: "☀️",   # Clear sky
        1: "🌤️",  # Mainly clear
        2: "⛅",  # Partly cloudy
        3: "☁️",   # Overcast
        45: "🌫️", # Fog
        48: "🌫️", # Depositing rime fog
        51: "🌦️", # Light drizzle
        53: "🌦️", # Moderate drizzle
        55: "🌧️", # Dense drizzle
        61: "🌧️", # Slight rain
        63: "🌧️", # Moderate rain
        65: "⛈️",  # Heavy rain
        71: "🌨️", # Slight snow
        73: "🌨️", # Moderate snow
        75: "❄️",  # Heavy snow
        77: "🌨️", # Snow grains
        80: "🌦️", # Slight rain showers
        81: "🌧️", # Moderate rain showers
        82: "⛈️",  # Violent rain showers
        85: "🌨️", # Slight snow showers
        86: "❄️",  # Heavy snow showers
        95: "⛈️",  # Thunderstorm
        96: "⛈️",  # Thunderstorm with slight hail
        99: "⛈️"   # Thunderstorm with heavy hail
    }
    return weather_codes.get(code, "🌡️")

def get_weather_description(code):
    """Convert weather code to description"""
    descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Foggy",
        48: "Foggy",
        51: "Light drizzle",
        53: "Drizzle",
        55: "Heavy drizzle",
        61: "Light rain",
        63: "Rain",
        65: "Heavy rain",
        71: "Light snow",
        73: "Snow",
        75: "Heavy snow",
        77: "Snow grains",
        80: "Rain showers",
        81: "Rain showers",
        82: "Heavy rain showers",
        85: "Snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with hail",
        99: "Thunderstorm with hail"
    }
    return descriptions.get(code, "Unknown")

def display_forecast(data):
    """Display the 5-day forecast in a nice format"""
    print("\n" + "="*60)
    print(f"📍 5-DAY WEATHER FORECAST FOR {data['city']}")
    print("="*60 + "\n")
    
    forecast = data['forecast']
    
    for i in range(5):
        date = datetime.strptime(forecast['time'][i], '%Y-%m-%d')
        day_name = date.strftime('%A')
        date_str = date.strftime('%B %d, %Y')
        
        max_temp = forecast['temperature_2m_max'][i]
        min_temp = forecast['temperature_2m_min'][i]
        precipitation = forecast['precipitation_sum'][i]
        weather_code = forecast['weathercode'][i]
        
        emoji = get_weather_emoji(weather_code)
        description = get_weather_description(weather_code)
        
        print(f"{emoji}  {day_name}, {date_str}")
        print(f"   {description}")
        print(f"   🌡️  High: {max_temp:.1f}°F  |  Low: {min_temp:.1f}°F")
        print(f"   💧 Precipitation: {precipitation:.1f} mm")
        print()

def main():
    """Main function to run the weather app"""
    print("\n🌤️  WELCOME TO THE 5-DAY WEATHER FORECAST APP  🌤️\n")
    
    while True:
        city = input("Enter a city name (or 'quit' to exit): ").strip()
        
        if city.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Thanks for using the weather app! Stay safe!\n")
            break
        
        if not city:
            print("❌ Please enter a valid city name.\n")
            continue
        
        print(f"\n🔍 Fetching forecast for {city}...\n")
        
        forecast_data = get_weather_forecast(city)
        
        if forecast_data:
            display_forecast(forecast_data)
            
        another = input("\nWould you like to check another city? (yes/no): ").strip().lower()
        if another not in ['yes', 'y']:
            print("\n👋 Thanks for using the weather app! Stay safe!\n")
            break

if __name__ == "__main__":
    main()
