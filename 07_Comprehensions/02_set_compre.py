favourite_chais = [
    "Masala Chai ", "green Chai" ,"adrak Chai"
    ,"Lemon Chai" ,"green Chai"
]
# unique_Chai = {chai for chai in favourite_chais}
unique_Chai = {chai for chai in favourite_chais if len(chai) < 11}

# print(unique_Chai)

recipes = {
    "simple chai": ["milk", "Chai Patti"],
    "elaichi Chai":["milk", "Elaichi Powder" , "Chai Patti"],
    "Kadak chai": ["milk", "Chai Patti" , "Adarak"]
}
unique_Chai = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_Chai)

