staff = [("amit" , 16), ("zara", 19) , ("raj",23)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is Elegible")
        print(f"interview ends")
        break
    else:
        print(f"{name } is Not eligible")

