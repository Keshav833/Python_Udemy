chai_order = dict(order1 = "cold coffee" , order2 = "burger")
print( f"print the chai_order: {chai_order}")

recipe = {}
recipe["first"] = "Ginger"
recipe["second"] = "MILK"
recipe["third"] = "suger"
print(f"recipe: {recipe}")
print(f"recipe  First: {recipe['first']}")
print(f"is ginger present :{"first" in recipe}") #true
print(f"is ginger present :{"Ginger" in recipe}") #false
print(f"print keys : {recipe.keys()}")
print(f"print values : {recipe.values()}")
print(f"print items : {recipe.items()}")

last_item = recipe.popitem()
print(f"recipe: {recipe}")
# last_item = recipe.popitem()
# print(f"recipe: {recipe}")

chai_order.update(recipe)
print(f"updated chai order : {chai_order}")

