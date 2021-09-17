Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from selenium import webdriver
>>> from bs4 import BeautifulSoup
>>> import pandas as pd
>>> driver=webdriver.Chrome('c:/chromedriver.exe')
>>> res=[]
>>> rev=[]
>>> dis=[]
>>> typ=[]
>>> driver.get("https://www.swiggy.com/bangalore")
>>> page=1
>>> while True:
	content=driver.page_source
	soup=BeautifulSoup(content)
	for a in soup.findAll('div',attrs={'class':'MZy1T'}):
		for b in a.findAll('div',attrs={'class':'_3XX_A'}):
			name = b.find('div',attrs={'class':'nA6kb'})
			review = b.find('div',attrs={'class':'_9uwBC _2lAlc'})
			discount = b.find('div',attrs={'class':'Zlfdx'})
			food = b.find('div',attrs={'class':'_1gURR'})
			res.append(name.text)
			typ.append(food.text)
			if(review!=None):
				rev.append(review.text)
			else:
				rev.append("N/A")
			if(discount!=None):
				dis.append(discount.text)
			else:
				dis.append("N/A")
	next_page=soup.find('a',attrs={'class':'_1FZ7A'})
	if next_page:
		page+=1
		driver.get("https://www.swiggy.com/bangalore"+"?page="+str(page))
	else:
		break

	
>>> df = pd.DataFrame({'Restaurants':res,'Food Offered':typ,'Reviews':rev,'Disounts':dis})
>>> df.to_csv('Swiggy.csv')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    df.to_csv('Swiggy.csv')
  File "C:\Python38\lib\site-packages\pandas\core\generic.py", line 3466, in to_csv
    return DataFrameRenderer(formatter).to_csv(
  File "C:\Python38\lib\site-packages\pandas\io\formats\format.py", line 1105, in to_csv
    csv_formatter.save()
  File "C:\Python38\lib\site-packages\pandas\io\formats\csvs.py", line 237, in save
    with get_handle(
  File "C:\Python38\lib\site-packages\pandas\io\common.py", line 702, in get_handle
    handle = open(
PermissionError: [Errno 13] Permission denied: 'Swiggy.csv'
>>> df.to_csv('C:/Users/Pratik/Downloads/Programs/pynb/Swiggy.csv',index=False)
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1334 entries, 0 to 1333
Data columns (total 4 columns):
 #   Column        Non-Null Count  Dtype 
---  ------        --------------  ----- 
 0   Restaurants   1334 non-null   object
 1   Food Offered  1334 non-null   object
 2   Reviews       1334 non-null   object
 3   Disounts      1334 non-null   object
dtypes: object(4)
memory usage: 41.8+ KB
>>> 