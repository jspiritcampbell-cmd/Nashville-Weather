import requests
import json

# Nashville coordinates
LATITUDE = 36.1627
LONGITUDE = -86.7816

# User Agent required by NWS API
HEADERS = {
    "User-Agent": "(Nashville Weather Test App, test@example.com)"
}

print("=" * 60)
print("Testing National Weather Service (NWS) API")
print("=" * 60)
print(f"\nLocation: Nashville, TN 37203")
print(f"Coordinates: {LATITUDE}°N, {LONGITUDE}°W")
print(f"\nBase URL: https://api.weather.gov")

# Step 1: Get grid point data
print("\n" + "=" * 60)
print("STEP 1: Getting grid point data...")
print("=" * 60)

grid_url = f"https://api.weather.gov/points/{LATITUDE},{LONGITUDE}"
print(f"URL: {grid_url}")

try:
    response = requests.get(grid_url, headers=HEADERS, timeout=10)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        grid_data = response.json()
        print("✅ Grid point data retrieved successfully!")
        
        # Extract important URLs
        forecast_url = grid_data['properties']['forecast']
        stations_url = grid_data['properties']['observationStations']
        
        print(f"\nForecast URL: {forecast_url}")
        print(f"Stations URL: {stations_url}")
        
        # Step 2: Get forecast
        print("\n" + "=" * 60)
        print("STEP 2: Getting forecast data...")
        print("=" * 60)
        
        forecast_response = requests.get(forecast_url, headers=HEADERS, timeout=10)
        print(f"Status Code: {forecast_response.status_code}")
        
        if forecast_response.status_code == 200:
            forecast_data = forecast_response.json()
            print("✅ Forecast data retrieved successfully!")
            
            periods = forecast_data['properties']['periods']
            print(f"\n📅 Showing first 3 forecast periods:")
            print("-" * 60)
            
            for i, period in enumerate(periods[:3], 1):
                print(f"\n{i}. {period['name']}")
                print(f"   Temperature: {period['temperature']}°{period['temperatureUnit']}")
                print(f"   Conditions: {period['shortForecast']}")
                print(f"   Details: {period['detailedForecast'][:100]}...")
        else:
            print(f"❌ Failed to get forecast: {forecast_response.status_code}")
        
        # Step 3: Get current observations
        print("\n" + "=" * 60)
        print("STEP 3: Getting current observations...")
        print("=" * 60)
        
        stations_response = requests.get(stations_url, headers=HEADERS, timeout=10)
        print(f"Status Code: {stations_response.status_code}")
        
        if stations_response.status_code == 200:
            stations_data = stations_response.json()
            print("✅ Stations data retrieved successfully!")
            
            if stations_data.get('observationStations'):
                station_id = stations_data['observationStations'][0]
                print(f"\nNearest Station: {station_id}")
                
                # Get latest observation
                obs_url = f"{station_id}/observations/latest"
                obs_response = requests.get(obs_url, headers=HEADERS, timeout=10)
                print(f"Observation URL: {obs_url}")
                print(f"Status Code: {obs_response.status_code}")
                
                if obs_response.status_code == 200:
                    obs_data = obs_response.json()
                    print("✅ Current observations retrieved successfully!")
                    
                    props = obs_data['properties']
                    
                    # Convert temperature from Celsius to Fahrenheit
                    temp_c = props.get('temperature', {}).get('value')
                    temp_f = (temp_c * 9/5) + 32 if temp_c else None
                    
                    print(f"\n🌡️  Current Conditions:")
                    print("-" * 60)
                    print(f"Temperature: {temp_f:.1f}°F" if temp_f else "Temperature: N/A")
                    print(f"Humidity: {props.get('relativeHumidity', {}).get('value', 'N/A')}%")
                    
                    wind_speed = props.get('windSpeed', {}).get('value')
                    if wind_speed:
                        wind_mph = wind_speed * 0.621371
                        print(f"Wind Speed: {wind_mph:.1f} mph")
                    else:
                        print("Wind Speed: N/A")
                    
                    print(f"Conditions: {props.get('textDescription', 'N/A')}")
                else:
                    print(f"❌ Failed to get observations: {obs_response.status_code}")
        else:
            print(f"❌ Failed to get stations: {stations_response.status_code}")
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED - NWS API is working correctly!")
        print("=" * 60)
        
    else:
        print(f"❌ Failed to get grid point: {response.status_code}")
        print(f"Response: {response.text}")

except Exception as e:
    print(f"\n❌ Error occurred: {str(e)}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
print("API Test Complete")
print("=" * 60)
