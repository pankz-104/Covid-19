import requests
from win10toast import ToastNotifier
import json 
import time

def update():
    r = requests.get("https://coronavirus-19-api.herokuapp.com/all")
    data = r.json()
    text = f'coinformed cases : {data["cases"]} \n Deaths : {data["deaths"]}\n Recovered : {data["recovered"]}'
    while True:
        toast = ToastNotifier()
        toast.show_toast("Covid-19 updates",text,duration=20)
        time.sleep(5)

update()
