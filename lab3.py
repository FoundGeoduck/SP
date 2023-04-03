import requests

URL = "http://biik.ru/rasp/cg109.htm"
a = requests.get(URL)
a.encoding="windows-1251"
print(a.text)
