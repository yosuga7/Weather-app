from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def get_coordinates(city_name):
    """Fetch coordinates for a city using Open-Meteo Geocoding API."""
    try:
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
        response = requests.get(url)
        data = response.json()
        if not data.get('results'):
            return None
        return data['results'][0]
    except Exception as e:
        print(f"Error fetching coordinates: {e}")
        return None

def get_weather_data(lat, lon):
    """Fetch weather data using Open-Meteo Weather API."""
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,is_day,weather_code,wind_speed_10m&timezone=auto"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/weather', methods=['GET'])
def weather_api():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City is required'}), 400
    
    location = get_coordinates(city)
    if not location:
        return jsonify({'error': 'City not found'}), 404
        
    weather = get_weather_data(location['latitude'], location['longitude'])
    if not weather:
        return jsonify({'error': 'Weather data unavailable'}), 500
        
    return jsonify({
        'city': location['name'],
        'country': location.get('country', ''),
        'temp': weather['current']['temperature_2m'],
        'humidity': weather['current']['relative_humidity_2m'],
        'wind_speed': weather['current']['wind_speed_10m'],
        'is_day': weather['current']['is_day'],
        'weather_code': weather['current']['weather_code'],
        'units': {
            'temp': weather['current_units']['temperature_2m'],
            'speed': weather['current_units']['wind_speed_10m']
        }
    })

if __name__ == '__main__':
    app.run(debug=True, port=8080)
