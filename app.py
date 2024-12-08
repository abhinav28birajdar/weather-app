from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'a3ff7c13d429ec8c6bbfbec5b3010aad'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    if not city:
        return render_template('index.html', error='Please enter a city name.')

    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return render_template('weather.html', weather=weather_info)
    else:
        error_message = data.get('message', 'City not found!')
        return render_template('index.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
