from appliances import Dishwasher, Washer, Dryer, Refrigerator, CoffeeMaker, CanOpener


whirlpool_dishwasher = Dishwasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red", "gas")
samsung_dryer = Dryer("red", "electric")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

new_can_opener = CanOpener("blue")
new_can_opener.open_can()




# how did I fix?
# changed several defs to class
# added (self) to all the defs functions that were missing it
# created __init__.py file and added imports to all the files
# ensured that all the subclasses had appropriate reference to parent class
# made sure that the required initialization inputs were there
# DishWasher changed to Dishwasher in multiple places
# many references to super were missing ()

