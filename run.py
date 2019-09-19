from flask import Flask, render_template, redirect, url_for, request, flash
import requests, json, time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/alarms.html')
def alarms():
    return render_template('alarms.html')

@app.route('/settings.html')
def settings():
    return render_template('settings.html')

@app.route('/_light', methods=['POST'])
def lightOn():
    status_on = request.form['status_on']
    flash("status_on:", status_on)
    
    # Setting up URL to send commands to the bulb via the hue bridge
    url = "http://192.168.178.28/api/QpwEJGEz2Vw6J6z66yj2vRhC4yruI6sMr8jOnyZe/lights/4/state"

    # Setting up the command/data based on content of status_on (true or false)
    if(status_on == True):
        data = {"on":True, "bri":200} #bri = 254 is full brightness
        response = {'turned on'}
    else:
        data = {"on":False}
        response = {'turned off'}

    flash(response)
    
    # Send the command to the bulb via hue bridge
    r = requests.put(url, json.dumps(data), timeout=5)

    return response    

if __name__ == '__main__':
    app.run(debug=True, port=1337)
