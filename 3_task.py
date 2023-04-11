import requests
import datetime
import time


def get_quesions(from_date, to_date, tag):
    fromdate = int(time.mktime(time.strptime(from_date, "%Y-%m-%d")))
    todate = int(time.mktime(time.strptime(to_date, "%Y-%m-%d")))
    url = f'https://api.stackexchange.com//2.3/questions?{fromdate}&{todate}&order=desc&sort=activity&tagged={tag}&site=stackoverflow'
    resp = requests.get(url)
    response = resp.json()
    get_items = response.get('items')
    for item in get_items:
      questions = item.get('title')
      print(questions)

get_quesions("2023-4-9", "2023-4-11", 'python')