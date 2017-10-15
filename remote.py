import RPi.GPIO as GPIO
import time
import pyrebase
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("home/pi/CoolAir.json")
firebase_admin.initialize_app(cred)

config = {
    "apiKey": "LB8jak6UuIs9hEFWrfCl2TVjI4deGARsHO3yuD2t",
    "authDomain": "coolair-5c653.firebaseapp.com",
    "databaseURL": "https://coolair-5c653.firebaseio.com/",
    "storageBucket": "coolair-5c653.appspot.com",
    "serviceAccount": "home/pi/CoolAir.json"
    }

firebase = firebase.initialize(config)
db = firebase.database()
email = "evan.peter.jones@gmail.com"
password = "needthatcoolair"
auth = firebase.auth(n)
user = sign_in_with_email_and_password(email, password)

data = {
    'status' : '0'
    }

LED = 19
GPIO.setmode(BCM)
GPIO.setup(LED, OUTPUT)

def run():
    with open(IRFunction.txt) as f:
        for i in range(0, 729):
            code = f.read(i)
            if (code == 0):
                GPIO.output(LED, False)
                time.sleep(.001)
            if (code == 1):
                GPIO.output(LED, True)
                time.sleep(.001)
                
def check():
    for ():
        if (db.child("status").get(user['idToken']).val() == 1):
            run()
            db.set(data, user['idToken'])
        time.sleep(5)

check()
