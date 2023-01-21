from flask import (
    Blueprint, flash, render_template, request
)
import requests
bp = Blueprint('weather', __name__)
from datetime import datetime


now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y")
tm_string = now.strftime("%d/%m/%Y")
# print("date and time =", dt_string)

key="0c631eb08af548f6a6f170943231901"


def lookup(city):
    """Look up quote for symbol."""
        # Contact API
    url = f"http://api.weatherapi.com/v1/current.json?key=0c631eb08af548f6a6f170943231901&q={city}"
    response = requests.get(url)
    data = response.json()
    # print(data)
    return {
        "city": data["location"]["name"],
        "country": data["location"]["country"],
        "local": data["location"]["localtime"],
        "temp": data["current"]["temp_c"],
        "feels":data["current"]["feelslike_c"],
        "is_day":data["current"]["is_day"],
        "cond": data["current"]["condition"]["text"],
        "cond_icon": data["current"]["condition"]["icon"],
        "humidity": data["current"]["humidity"],
    }

@bp.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":      
        city = request.form.get("city")
        # print(city)
        # print(dat)
        if not city:
            error = 'Please enter the city'            
        else:
            try:
                data = lookup(city)
                city = data["city"]
                country = data["country"]
                time = data["local"]
                temp = data["temp"]
                feels = data["feels"]
                icon = str(data["cond_icon"])
                condition = data["cond"]
                humidity = data["humidity"]
            except KeyError:
                error = f"Incorrect city"
            else:                
                return render_template('weather/index.html',city=city, 
                                       country=country, time=time, temp=temp, feels=feels, 
                                       icon=icon, condition=condition, humidity=humidity)
        
        flash(error)    

    return render_template('weather/index.html', error=error)
        # return 'hello'
    


# code_dict={
#    "1000":113,
# "1003":116,
# "1006":119,
# "1009":122,
# "1030":143,
# "1063":176,
# "1066":179,
# "1069":182,
# "1072":185,
# "1087":200,
# "1114":227,
# "1117":230,
# "1135":248,
# "1147":260,
# "1150":263,
# "1153":266,
# "1168":281,
# "1171":284,
# "1180":293,
# "1183":296,
# "1186":299,
# "1189":302,
# "1192":305,
# "1195":308,
# "1198":311,
# "1201":314,
# "1204":317,
# "1207":320,
# "1210":323,
# "1213":326,
# "1216":329,
# "1219":332,
# "1222":335,
# "1225":338,
# "1237":350,
# "1240":353,
# "1243":356,
# "1246":359,
# "1249":362,
# "1252":365,
# "1255":368,
# "1258":371,
# "1261":374,
# "1264":377,
# "1273":386,
# "1276":389,
# "1279":392,
# "1282":395,

# }