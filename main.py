#!/usr/bin/python

import ingredients as ing
import recipes as rec

def ingredients_dictionary(dictionary):
	print "\nSelect an ingredient."
	for k,v in dictionary.items():
		print " %-3i %-30s %.1f kCal/g" % (k, v.name, v.cpg)
	uin = int(raw_input("\nChoice: "))
	weight = float(raw_input("Weight (g): "))
	print dictionary[uin].get_calories(weight),"kcal"

print "Welcome to the Meal Planner!"
print "\nWhat would you like to look up?"
print " 1. Calories in an ingredient"
print " 2. Recipe information"

uin = int(raw_input("\nChoice: "))
if uin == 1:
	print "\nSelect a category."
	print " 1. pantry"
	print " 2. vegetables"
	print " 3. meats"
	uin = raw_input("\nChoice: ")
	if uin == "1":
		ingredients_dictionary(ing.my_pantry)
	elif uin =="2":
		ingredients_dictionary(ing.my_vegetables)
	elif uin =="3":
		ingredients_dictionary(ing.my_meats)
elif uin == 2:
	print "\nSelect a recipe."
	for k,v in rec.my_recipes.items():
		print " %-3i %-30s" % (k, v.name)
	uin = int(raw_input("\nChoice: "))
	rec.my_recipes[uin].print_recipe()
else:
	print "Invalid choice. Exiting"
