import requests
import datetime
import time

def get_quesions(from_date, to_date):
    fromdate = int(time.mktime(time.strptime(from_date, "%Y-%m-%d")))
    todate = int(time.mktime(time.strptime(to_date, "%Y-%m-%d")))
    url = f'https://api.stackexchange.com/2.3/questions?{fromdate}&{todate}&order=desc&sort=activity&site=stackoverflow'
    resp = requests.get(url)
    response = resp.json()
    questions = response.get('items')
    for item in questions:
      for k, v in item.items():
          if k == 'tags' and 'python' in(item['tags']):
            print(f'Вопросы, содержащие тег "python": {item["title"]}')


get_quesions("2023-4-9", "2023-4-11")