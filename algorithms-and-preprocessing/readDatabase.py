import csv

def atLeast(ingredients,recipe):

	count = 0
	for recipeIngredient in ingredients:

		for temp in recipe:

			if(recipeIngredient in temp):
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


databaseFileName = "recipe"

ingredients = ['butter', 'sugar', 'corn syrup', 'salt', 'baking soda', 'vanilla extract', 'popcorn', 'dough', 'nuts', 'cinnamon', 'water', 'honey', 'onion']

print(searchForRecipe(databaseFileName, ingredients))
