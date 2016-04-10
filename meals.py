#!/usr/bin/python

class food(object):
    def __init__(self, name, calories, weight):
        self.name = name
        self.calories = calories
        self.weight = weight
        self.cpg = self.calories / self.weight
    #calculate calories by weight
    def get_calories(self, weight):
        return self.cpg*weight


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
            food = eval(foods_list[i])
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
            food = eval(foods_list[i])
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
        print '\n\n%s, %ig, %ikCal' % (self.name, self.get_total_amounts(), self.get_total_calories())
        print '%-30s %-10s %-10s' % ("Ingredient", "Amount (g)", "Calories (kcal)")
        for i in range(0, self.length):
            name = foods[i]
            amt = amounts[i]
            cal = calories[i]
            print '%-30s %-10i %-10i' % (name, amt, cal)
        print '\n'

emily_target_kcal = 300.
emily_num_meals = 3
emily_kcal = emily_target_kcal * emily_num_meals

ivan_target_kcal = 450.
ivan_num_meals = 4
ivan_kcal = ivan_target_kcal * ivan_num_meals

kcal_total = emily_kcal + ivan_kcal
ivan_proportion = ivan_kcal/kcal_total
emily_proportion = emily_kcal/kcal_total


# FOODS
#food($NAME, $CALORIES, $WEIGHT)
# pantry
#  - oils, sauces, dressings
apple_cider_vinegar = food("apple cider vinegar", 3., 15.)
bonesuckin_sauce = food("bone suckin' sauce", 40., 28.)
coleslaw_dressing = food("coleslaw dressing", 140., 30.)
soy_sauce = food("soy sauce", 30., 45.)
sunflower_oil = food("sunflower oil", 120., 100.)
vindaloo_simmer_sauce = food("vindaloo simmer sauce", 90., 106.)
#  - canned
black_beans = food("black beans", 130., 110.)
chicken_broth = food("chicken broth", 20., 237.)
diced_tomatoes = food("diced tomatoes", 30., 126.) 
#  - dry
brown_rice = food("brown rice", 600., 445.)
brown_sugar = food("brown sugar", 15., 4.)

# vegetables
cabbage = food("cabbage", 22, 89.)
carrots = food("carrots", 25., 61.)
garlic = food("garlic", 3., 4.)
onions = food("onions", 20., 80.)

# meats
chicken_breast = food("raw chicken breast", 114., 100.)
pork_tenderloin = food("pork tenderloin", 120., 112.)

# APR 3 - MEAL PREP
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
hbbi = healthy_black_beans_ingredients
hbb = healthy_black_beans

# HEALTHY PULLED PORK
pulled_tenderloin_ingredients = [
        ['pork_tenderloin', 1170.],
        ['bonesuckin_sauce', 4*28.],
        ['brown_sugar', 30.],
        ['apple_cider_vinegar', 30.]
]
pulled_tenderloin = recipe("Pulled Tenderloin", pulled_tenderloin_ingredients)
pt = pulled_tenderloin

# HEALTHY COLESLAW
coleslaw_ingredients = [
        ['cabbage', 1170.],
        ['carrots', 585.],
        ['coleslaw_dressing', 60.]
]
coleslaw = recipe("Coleslaw", coleslaw_ingredients)
cs = coleslaw

# APR 9 - DINNER
vindaloo_chicken_ingredients = [
        ['vindaloo_simmer_sauce', 6.*106],
        ['chicken_breast', 640],
        ['onions', 100],
        ['sunflower_oil', 3],
        ['brown_rice', 180]
]
vindaloo_chicken = recipe("Vindaloo Chicken", vindaloo_chicken_ingredients)
vc = vindaloo_chicken

# test methods
#healthy_black_beans.print_recipe()
#print "Ingredients list:", hbb.get_ingredients_list()
#print "Foods list:", hbb.get_foods_list()
#print "Amounts list: ", hbb.get_amounts_list()
#print "Calories list: ", hbb.get_calories_list()
#print "Total Calories: ", hbb.get_total_calories()
hbb.print_recipe()
pulled_tenderloin.print_recipe()
coleslaw.print_recipe()

ivan_hbb_kcal = hbb.get_total_calories()*ivan_proportion
emily_hbb_kcal = hbb.get_total_calories()*emily_proportion

ivan_hbb_kcal_per_meal = ivan_hbb_kcal / ivan_num_meals
emily_hbb_kcal_per_meal = emily_hbb_kcal / emily_num_meals

print "Black bean calories per meal"
print "Ivan:", ivan_hbb_kcal_per_meal
print "Emily:", emily_hbb_kcal_per_meal

ivan_pt_kcal = pt.get_total_calories()*ivan_proportion
emily_pt_kcal = pt.get_total_calories()*emily_proportion

ivan_pt_kcal_per_meal = ivan_pt_kcal / ivan_num_meals
emily_pt_kcal_per_meal = emily_pt_kcal / emily_num_meals

print "\nPulled tenderloin calories per meal"
print "Ivan:", ivan_pt_kcal_per_meal
print "Emily:", emily_pt_kcal_per_meal

emily_cs_kcal = coleslaw.get_total_calories()*emily_proportion
ivan_cs_kcal = coleslaw.get_total_calories()*ivan_proportion

emily_cs_kcal_per_meal = emily_cs_kcal / emily_num_meals
ivan_cs_kcal_per_meal = ivan_cs_kcal / ivan_num_meals

print "\nColeslaw calories per meal"
print "Ivan:", ivan_cs_kcal_per_meal
print "Emily:", emily_cs_kcal_per_meal

Ivan_calories_per_meal = ivan_hbb_kcal_per_meal + ivan_pt_kcal_per_meal + ivan_cs_kcal_per_meal
Emily_calories_per_meal = emily_hbb_kcal_per_meal + emily_pt_kcal_per_meal + emily_cs_kcal_per_meal


print "\nCalories per meal so far"
print "Ivan:" , Ivan_calories_per_meal
print "Emily:", Emily_calories_per_meal
hbb_yield = 624
pt_yield = 1210
cs_yield = 1795
