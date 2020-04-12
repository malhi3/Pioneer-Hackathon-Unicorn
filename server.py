from flask import Flask, render_template, redirect, url_for, request
import csv

import sys

reload(sys)
sys.setdefaultencoding('utf8')


app = Flask(__name__)

@app.route('/', methods=['GET'])
def init():
    f = open("ingredients.txt", 'r')
    ingredients_text = f.read()
    ingredients_list = sorted(ingredients_text.lower().split(","))

    return render_template("index.html", ingredients=ingredients_list)

@app.route('/recipes', methods=['GET'])
def recipes():
    return render_template("recipes.html")

@app.route('/get_recipes', methods=['POST'])
def get_recipes():
    ingredients_str = request.form['ingredients']
    ingredients = ingredients_str.split(',')
    #ingredients = [unicode(item) for item in ingredients]
    databaseFileName = "recipe"

    def atLeast(ingredients,recipe):

    	count = 0
    	for recipeIngredient in ingredients:

    		for temp in recipe:

    			if(recipeIngredient in temp or recipeIngredient[:len(recipeIngredient)-1]+"ies" in temp):
    				count = count + 1
    				break

    	if(count<len(recipe)):
    		return False

    	return True


    def searchForRecipe(csvFileName, ingredients, allRecipies = []):


    	try:
    		open(csvFileName+".csv")
    	except FileNotFoundError as e:
    		print("File Not Found")
    		return None



    	try:
    		ingredients[0]

    		#ingredients =
    		print(ingredients)
    	except Exception as e:
    		print(e)
    		return None

    	with open(csvFileName+".csv") as csv_file:

    	    csv_reader = csv.reader(csv_file, delimiter=',')

    	    for count, row in enumerate(csv_reader):

    	    	if(count==0):
    	    		continue

    	    	tempDelimiter = ","
    	    	temp =list(map(str, row[2:][0].lower().split(tempDelimiter)))

    	    	if(atLeast(ingredients, temp)):

    	    		allRecipies.append(row)


    	return allRecipies

    recipesList = searchForRecipe(databaseFileName, ingredients);
    return render_template("recipes.html", recipes=recipesList)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
