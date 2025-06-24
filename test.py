import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 200, "name": "Mack", "views": 100000},
        {"likes": 10000, "name": "How to make Rest API", "views": 80000},
        {"likes": 47, "name": "Ken", "views": 2000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())


input()
response = requests.get(BASE + "video/6")
print(response.json())