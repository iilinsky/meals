class food(object):
    def __init__(self, name, calories, weight):
        self.name = name
        self.cpg = calories / weight
    #calculate calories by weight
    def get_calories(self, weight):
        return round(self.cpg*weight,2)

# USAGE: food($NAME, $CALORIES, $WEIGHT)

################################################################################
# pantry
################################################################################

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

my_pantry = {	1 : apple_cider_vinegar,
		2 : bonesuckin_sauce,
		3 : coleslaw_dressing,
		4 : soy_sauce,
		5 : sunflower_oil,
		6 : vindaloo_simmer_sauce,
		7 : black_beans,
		8 : chicken_broth,
		9 : diced_tomatoes,
		10 : brown_rice,
		11 : brown_sugar
}

################################################################################
# vegetables
################################################################################

cabbage = food("cabbage", 22, 89.)
carrots = food("carrots", 25., 61.)
garlic = food("garlic", 3., 4.)
onions = food("onions", 20., 80.)

my_vegetables = {	1: cabbage,
			2: carrots,
			3: garlic,
			4: onions
}

################################################################################
# meats
################################################################################

chicken_breast = food("raw chicken breast", 114., 100.)
pork_tenderloin = food("pork tenderloin", 120., 112.)

my_meats = { 	1 : chicken_breast,
		2 : pork_tenderloin
}
