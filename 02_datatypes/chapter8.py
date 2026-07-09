#List (mutable) using '[]'
ingredients = ["Milk", "ginger", "water", "Tea_leaves"]
print(f"print ingredients of tea :{ingredients}")
ingredients.append("cardimon")
print(f"print ingredients of tea :{ingredients}")
ingredients.insert(2,"suger")
# print(f"print ingredients of tea :{ingredients}")

coffee_ingredient = ["Milk","Coffee_beans", "Suger"]
Chai_ingredient = ["Milk", "ginger", "water", "Tea_leaves"]

coffee_ingredient.extend(Chai_ingredient)
print(f"print ingredients of tea :{coffee_ingredient}")

coffee_ingredient.pop();
print(f"print after pop() ingredients of tea :{coffee_ingredient}")
coffee_ingredient.sort()
print(f"print sort ingredients of tea :{coffee_ingredient}")
coffee_ingredient.reverse()
print(f"print reverse ingredients of tea :{coffee_ingredient}")
print(f"count  milk ingredients in coffee :{coffee_ingredient.count("Milk")}")

num = [1,2,3,4,5,6,8,9]
print(f"num: {num}")
print(f"Max in num: {max(num)}")
print(f"Min in num: {min(num)}")

classA = ["sneha" , "kamal"]
classB = ["ayush"  ]
print(f"mixing both classA and B: {classA + classB}")

strong_coffee = ["Milk","Coffee_beans", "Suger"] * 3
print(f"print string coffee ingredient : {strong_coffee}")

raw_spice = bytearray(b"Cinnimon")
raw_spice = raw_spice.replace(b"Cinn" , b"Card")
print(f"print rawspice: {raw_spice}")

