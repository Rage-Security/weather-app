from flask import Flask, render_template
import os
import requests, json
import time


app = Flask(__name__)

# URL
api_key = "729d99bd52f8edc51126144a21673993"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = 'Darwin'
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
#complete_url = 'http://0.0.0.0:8000/rep.json'

# VARs
response = requests.get(complete_url)
x = response.json()
dow = x['dt']

fer = int(x['main']['temp'])
cel = fer - 273.15


#PRINT
print("DAY : "+ time.strftime('%A',time.localtime(1657205852)))

#Icons
ico = None
id = x['weather'][0]['id']
if 200<= id <=232:
    ico = 'cloud-lightning'
elif 300<= id <=321:
    ico = 'cloud-drizzle'
elif 500<= id <=531:
    ico = 'cloud-rain'
elif 600<= id  <=622:
    ico = 'cloud-snow'
elif 700<= id <=781:
    ico = 'wind'
elif 801<= id <=804:
    ico = 'cloud'
elif 'n' in x['weather'][0]['icon']:
    ico = 'moon'
else:
    ico = 'sun'




@app.route('/')
def index():
    return render_template('sideleft.html',day=time.strftime('%A',time.localtime(dow)),
    date=time.strftime('%d %b %Y',time.localtime(dow)),
    city = x['name']+', '+x['sys']['country'],
    tempr = round(cel),
    main = x['weather'][0]['main'],
    icon = ico
    )
@app.route('/side')
def index1():
    return render_template('sideright.html',desc=x['weather'][0]['description'].capitalize(),
    
    humid = x['main']['humidity'],
    wind = round(x['wind']['speed']*3.6)
    )

    
if __name__ == '__main__':

    app.run(debug=True,port=5000)
    
    
