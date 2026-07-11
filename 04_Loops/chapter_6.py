order  = ["Ginger","Out of Stock" ,"lemon" , "sugar", "discontinued" ,"onion" ]
for ord in order:
    if ord == "Out of Stock":
        continue
    if ord == "discontinued":
        break
    print(f"{ord} found \n")

print(f"Out of loop")

