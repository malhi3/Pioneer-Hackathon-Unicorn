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

    for i in range(1,50):
        print(i)
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

            soup = getBSobject(url)
            ingredients = soup.find_all("span", class_="recipe-ingred_txt added")

            temp = ""

            try:
                ingredients[0]
                for i in range(len(ingredients)):
                    concatenate = ingredients[i].get_text().replace(",", ";")
                    temp = temp + ", " + (concatenate)
            except IndexError as I:
                ingredients = soup.find_all("span", class_="ingredients-item-name")

                for i in range(len(ingredients)):
                    concatenate = ingredients[i].get_text().replace(",", ";")
                    concatenate = " ".join(concatenate.split())
                    temp = temp + ", " + (concatenate)


            """
            if (ingredients[0].get_text() = ""):
                for i in range(len(ingredients)):
                    concatenate = ingredients[i].get_text().replace(",", ";")
                    temp = temp + ", " + (concatenate)
            else:
                ingredients = soup.find_all("span", class_="ingredients-item-name")

                for i in range(len(ingredients)):
                    concatenate = ingredients[i].get_text().replace(",", ";")
                    concatenate = " ".join(concatenate.split())
                    temp = temp + ", " + (concatenate)
            """

            temp = temp[2:]
            writer.writerow([title, url, temp])
