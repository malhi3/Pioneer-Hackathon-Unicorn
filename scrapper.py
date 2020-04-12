import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import csv

def getBSobject(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
    except AttributeError as e:
        return None
    return bs


url1 = "https://www.allrecipes.com/search/results/?wt=&sort=re&page="

with open('recipe.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(1,2):
        url = url1 + str(i)
        soup = getBSobject(url)

        #Need to extract text
        tempTitles = soup.find_all("span", class_="fixed-recipe-card__title-link")

        #Need to extract URL
        tempLinks = soup.find_all("h3" ,class_="fixed-recipe-card__h3")

        for i in range(0,len(tempLinks)):

            title = tempTitles[i].get_text()
            url = tempLinks[i].find('a').get('href')
            print(title)
            print(url)

            soup = getBSobject(url)
            ingredients = soup.find_all("span", class_="recipe-ingred_txt added")

            temp = ""

            for i in range(len(ingredients)):
                concatenate = ingredients[i].get_text().replace(",", ";")
                temp = temp + ", " + (concatenate)

            temp = temp[2:]

            writer.writerow([title, url, temp])
            
