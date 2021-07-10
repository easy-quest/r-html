import requests
from auth_data import token

group_name = input("Введите название группы: ")

url = f"https://api.vk.com/method/wall.get?domain={group_name}&count=40&access_token={token}&v=5.52"
req = requests.get(url)
print(req.text)