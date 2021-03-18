"""
1) install flask https://flask.palletsprojects.com/en/1.1.x/installation/#install-flask
2) install flask_restful https://flask-restful.readthedocs.io/en/latest/installation.html
3) run this file. While it is running,
4) Go to your browser and visit http://127.0.0.1:5000/services
5) Go to your browser and visit http://127.0.0.1:5000/hospitals

Steps 4 and 5 should return some json.
"""
from flask import Flask
from flask_restful import Resource, Api
import random

class Services(Resource):
    def get(self):
        return {
           "90899,2":"Pc Clinical Care Consultation, 21-30 Min, Facetoface",
           "90912,1":"Biofeedback training for bowel or bladder control, initial 15 minutes",
           "90935,1":"Hemodialysis procedure with one physician evaluation",
           "90935-3":"",
           "0C1776,4505":"",
           "90945,1":"Dialysis procedure including one evaluation",
           "90964,95":"ESRD HOME PT SERV P MO 2-11 - TELEMEDICINE",
           "90964":"",
           "90967,95":"ESRD HOME PT SERV P DAY &lt;2 -TELEMEDICINE",
           "90997":""
        }, 200

class Hospitals(Resource):
    def get(self):
        return {
            "Hospitals" : {
                "Minute Clinic" : {
                    "Latitude" : 9.00 + random.random(),
                    "Longitude" : 4.31 + random.random(),
                    "Price" : 3.50 + random.random()
                },
                "Mercy Hospital" : {
                    "Latitude": 9.12 + random.random(),
                    "Longitude": 4.20 + random.random(),
                    "Price": 3.58
                },
                "St. John's": {
                    "Latitude": 9.13 + random.random(),
                    "Longitude": 4.69 + random.random(),
                    "Price": 3.53 + random.random()
                }
            },
            "Natl_Distribution_Data" : [(2.75, 0.01), (2.85, 0.05), (2.95, 0.1), (3.05, 0.1), (3.15, 0.25), (3.25, 0.3), (3.35, 0.1), (3.45, 0.05), (3.55, 0.03), (3.65, 0.01)]
        }, 200

app = Flask(__name__)
api = Api(app)
api.add_resource(Services, '/services')
api.add_resource(Hospitals, '/hospitals')
app.run()