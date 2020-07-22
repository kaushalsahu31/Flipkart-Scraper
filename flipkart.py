import requests, json, os, time, random, webbrowser

from bs4 import BeautifulSoup

from pprint import pprint


a=input("What you want to search in -_- Flipkart -_-\n Search here\n")

url="https://www.flipkart.com/search?q="+a+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
data=requests.get(url).text
soup=BeautifulSoup(data,"html.parser")
flipkart=soup.find_all("div",class_="_1HmYoV _35HD7C")
flipkart=flipkart[1]
flipkartdata=flipkart.find_all("div",class_="bhgxx2 col-12-12")
datalists=[]
for i in flipkartdata:
	content=i.find("div",class_="_3O0U0u")
	if content!=None:
		contentdata=content.find_all("div")
		for j in contentdata:
			atag=j.find_all("a")
			if j!=None:
				for k in atag:
					if k!=None and k.text!=None:
						datas=j.find("a")["href"]
						if datas not in datalists:
							datalists.append(datas)
a=1
for i in datalists:
	print(a,i,"\n")
	a+=1
inp=int(input(""))
webbrowser.open("https://www.flipkart.com"+datalists[inp-1])
