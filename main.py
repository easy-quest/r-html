import requests
from auth_data import token

group_name = input("Введите название группы: ")
url = "https://api.vk.com/method/wall.get?domain={group_name}&count=40&access_token={token}&v=5.52"
print(url)
