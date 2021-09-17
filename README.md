# Swiggy_Web-scraping
Scraping Swiggy website
For this project I have used three library - Selenium, BeautifulSoup, and pandas.
Using these libraries I have tried to get all the information such as Name of the restuarants, Types of food they offer, Reviews, and Discounts from Swiggy Bangalore website.
The swiggy bangalore have around 1400 restaurants in operations and these restaurants are arranged in grid format in 84 different webpages.
To iterate through the each webpages I have used a 'while' loop.
Inside this while loop I have used two nested 'for' loops to iterate through each resaturants in each pages using findAll() function of BeautifulSoup.
I have declared four lists. 
res=[] to store the name of restaurants.
rev=[] to store the ratings.
dis=[] to store the discounts offered
typ=[] to store the type of foods offered
I have also used a 'page=1' variable to count the number of pages, so that I can update the url.
while True:                                                #to iterate through the 84 webpages
      .
      .
      .
      .
      .
      next_page=soup.find('a',attrs={'class':'_1FZ7A'})
	if next_page:
		page+=1
		driver.get("https://www.swiggy.com/bangalore"+"?page="+str(page))
	else:
		break
Two 'for' loops inside the while loops are:
     for a in soup.findAll('div',attrs={'class':'MZy1T'}):
		             for b in a.findAll('div',attrs={'class':'_3XX_A'}):
                        .
                        .
                        .
This part of code is used incase there is null value in reviews and discount, otherewise the compiler will throw 'nonetype object has no attribute text' error.
                if(review!=None):
				           rev.append(review.text)
                else:
				           rev.append("N/A")
			          if(discount!=None):
				           dis.append(discount.text)
			          else:
			           	 dis.append("N/A")
df = pd.DataFrame({'Restaurants':res,'Food Offered':typ,'Reviews':rev,'Disounts':dis}) to convert the newly created list into dataframe.
For saving the dataframe in csv format- df.to_csv('C:/Users/Pratik/Downloads/Programs/pynb/Swiggy.csv',index=False)
The newly created csv file had 1334 rows and 4 columns.
