chai_menu = {"masala":30 , "ginger":40}

try:
    chai_menu["Elaichi"]
except KeyError:
    print("The key that u are trying to access doesnt exist")

print( "Hello Chikne")