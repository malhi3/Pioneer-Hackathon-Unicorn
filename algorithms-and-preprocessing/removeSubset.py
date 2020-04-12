from collections import OrderedDict 
		

def hasAdjective(word):
	terms = ['ground', 'extra', 'fresh', 'diced', 'half', 'light', 'coarse', 'refried','heavy','crispy', 'halves','rolls', 'brewed', 'style','sweetened', 'cooked', 'white', 'yolk', 'boneless', 'granules', 'pure', 'cube', 'zest', 'cob', 'flat-leaf', 'whole', 'skin', 'shredded', 'plain', 'and', 'cracked', 'bone', 'hot', 'cold']
	for i in terms:
		if i in word:
			return True
	return False

allWords = []

f1= open("processed_food_names(0-100).txt","r")
temp = list(f1.readline().split(","))

allWords = allWords+temp

f1= open("processed_food_names(101-240).txt","r")
temp1 = list(f1.readline().split(","))

allWords = allWords+temp1

f1= open("processed_food_names(241-380).txt","r")
temp2 = list(f1.readline().split(","))

allWords = allWords+temp2

f1= open("processed_food_names(380-530).txt","r")
temp3 = list(f1.readline().split(","))

allWords = allWords+temp3




res = list(OrderedDict.fromkeys(allWords)) 
print(len(res))

res1 = list(filter(lambda x: not hasAdjective(x), res))

print(len(res1))

finalStr = ""
for count, i in enumerate(res1):
	if(count==0):
		finalStr = finalStr + i
		continue
	finalStr = finalStr + "," + i



f = open("allIngredients11dry.txt", "w")
f.write(finalStr)
f.close()




