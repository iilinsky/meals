import ingredients as ing

class recipe(object):
    def __init__(self, name, items):
        self.name = name
        self.items = items
        self.length = len(self.items)
    def get_foods_list(self):
        foods = []
        for i in range(0, self.length):
            foods += [self.items[i][0]]
        return foods
    def get_ingredients_list(self):
        foods_list = self.get_foods_list()
        ingredients = []
        for i in range(0, self.length):
            food = eval("ing."+foods_list[i])
            ingredient = food.name
            ingredients += [ingredient]
        return ingredients
    def get_amounts_list(self):
        amounts = []
        for i in range(0, self.length):
            amounts += [self.items[i][1]]
        return amounts
    def get_calories_list(self):
        foods_list = self.get_foods_list()
        amounts_list = self.get_amounts_list()
        cals_list = []
        for i in range(0, self.length):
            food = eval("ing."+foods_list[i])
            weight = amounts_list[i]
            calories = food.get_calories(weight)
            cals_list += [calories]
        return cals_list
    def get_total_calories(self):
        return sum(self.get_calories_list())
    def get_total_amounts(self):
        return sum(self.get_amounts_list())
    def print_recipe(self):
        foods = self.get_ingredients_list()
        amounts = self.get_amounts_list()
        calories = self.get_calories_list()
        print '\n\n%s, %ig, %ikCal\n' % (self.name, self.get_total_amounts(), self.get_total_calories())
        print '%-30s %-10s %-10s' % ("Ingredient", "Amount (g)", "Calories (kcal)")
        for i in range(0, self.length):
            name = foods[i]
            amt = amounts[i]
            cal = calories[i]
            print '%-30s %-10i %-10i' % (name, amt, cal)
        print '\n'

################################################################################
# APR 3 - MEAL PREP
################################################################################

# HEALTHY BLACK BEANS RECIPE
healthy_black_beans_ingredients = [
        ['black_beans', 8.*28],
        ['diced_tomatoes', 14.5*28],
        ['soy_sauce', 45.],
        ['chicken_broth', 14.5*28],
        ['apple_cider_vinegar', 30.],
        ['garlic', 10.],
        ['brown_sugar', 50.]
]
healthy_black_beans = recipe("Healthy Black Beans", healthy_black_beans_ingredients)

# HEALTHY PULLED PORK
pulled_tenderloin_ingredients = [
        ['pork_tenderloin', 1170.],
        ['bonesuckin_sauce', 4*28.],
        ['brown_sugar', 30.],
        ['apple_cider_vinegar', 30.]
]
pulled_tenderloin = recipe("Pulled Tenderloin", pulled_tenderloin_ingredients)

# HEALTHY COLESLAW
coleslaw_ingredients = [
        ['cabbage', 1170.],
        ['carrots', 585.],
        ['coleslaw_dressing', 60.]
]
coleslaw = recipe("Coleslaw", coleslaw_ingredients)

################################################################################
# APR 9 - DINNER
################################################################################

vindaloo_chicken_ingredients = [
        ['vindaloo_simmer_sauce', 6.*106],
        ['chicken_breast', 640],
        ['onions', 100],
        ['sunflower_oil', 3],
        ['brown_rice', 180]
]
vindaloo_chicken = recipe("Vindaloo Chicken", vindaloo_chicken_ingredients)

################################################################################
# APR 10 - MEAL PREP 
################################################################################

split_pea_soup_ingredients = [
	['split_peas', 2*454.], #2 lbs
	['ham_steak', 2*500.], #2 steaks
	['carrots', 500.],
	['onions', 300.],
	['celery', 500.],
	['chicken_broth', 2*411.] #2 can
]
split_pea_soup = recipe("Split Pea Soup", split_pea_soup_ingredients)

my_recipes = { 	1 : healthy_black_beans,
		2 : pulled_tenderloin,
		3 : coleslaw,
		4 : vindaloo_chicken,
		5 : split_pea_soup
	}
