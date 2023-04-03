from bs4 import BeautifulSoup
import requests

URL = "http://biik.ru/rasp/cg109.htm"
a = requests.get(URL)
a.encoding="windows-1251"
print(a.text)
if a == 404:
	print ('Not Found')
else: 
	all_web_code = a.text
	bs =BeautifulSoup(all_web_code,"html.parser")
	Lesson = bs.findAll('td')
	
	file = open ("Raspisanie.txt", "w")
	for item in Lesson:
		file.write(item.text +"\n")
	file.close()

	line = open ("Raspisanie.txt").readlines()
	for i in range(104):
		line.pop(0)
	
	f = open ("Raspisanie.txt", "w")
	for i in line:
		f.write(i)
	f.close()
