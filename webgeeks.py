import requests
from bs4 import BeautifulSoup
req=requests.get("https://webgeeks-3.herokuapp.com/sonnet3.html")
soup=BeautifulSoup(req.content,"html.parser")
links_list=soup.find_all('div')
for link in links_list:
	if 'class' in link.attrs:
		print(str(link.attrs['class'])+"\n")


