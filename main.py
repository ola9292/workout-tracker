import requests
from dotenv import load_dotenv
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os
load_dotenv()

APP_ID= os.environ.get("APP_ID")
API_KEY= os.environ.get("API_KEY")
url ="https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_url = "https://api.sheety.co/a153bedaf05f54250dc7a256b0001748/copyOfMyWorkouts/workouts"
SHEETY_USERNAME= os.environ.get("SHEETY_USERNAME")
SHEETY_PASS= os.environ.get("SHEETY_PASS")
basic = HTTPBasicAuth(SHEETY_USERNAME, SHEETY_PASS)

# print(APP_ID, API_KEY)

query = input("what exercise did you do? ")
headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

data = {
    "query": query,
}
response = requests.post(url=url, json=data, headers=headers)
print(response.status_code)  # 201 if resource created
data = response.json()['exercises']

    
time = "21/07/2020"
today = datetime.now()
formatted_date = today.strftime("%d/%m/%Y")

formatted_time = today.strftime("%H:%M:%S")
# print(formatted_date, formatted_time)
for exercise in data:
    name = exercise['name'].title()
    print(name)
    body = {
        "workout":{
            "date":formatted_date,
            "time":formatted_time,
            "exercise":name,
            "duration":exercise['duration_min'],
            "calories":exercise['nf_calories']
        }
    }
    sheety_response = requests.post(url=sheety_url, json=body, auth=basic)