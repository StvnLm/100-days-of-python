from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
    postal = request.form['postal']
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=' + postal + ',us&appid=2c54c46636f5009ce7ade8900c96fa48')
    json_text = response.json()
    temp_k = json_text['main']['temp']
    temp_f = (temp_k - 273.15) * 1.8 + 32
    return render_template('temperature.html', temp=temp_f)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
