# Flask-weather_app
#### Description:
Weather web app created with Python, Flask and free weather.api.

#### flaskr/__init__.py is The application factory with create_app function which creates Flask instance.
In __init__.py we need to import and register any blueprint, in this case that would be blueprint from
weather.py.

#### flaskr/weather.py containes the blueprint for index view and function lookup() used to retrive data from weatherapi.
Views:
Index:
index() function renders the template with all the weather info retrieved from lookup json data.


#### Installation:
Install with pip (windows):
$ pip install -r requirements.txt
$ pip3 install virtualenv
$py -3 -m venv venv
$venv\Scripts\activate
$pip install Flask

Initialize the database
$ flask --app flaskr init-db

Run in development server
$ flask --app flaskr --debug run

#### Project Directory:
```
/home/user/Projects/FLASK_WEATHER_APP
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── weather.py
│   ├── templates/weather/
│   │                 ├── index.html
│   └── static/
│   │    |── style.css
├── venv/
└── README.md
```
