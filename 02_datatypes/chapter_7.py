#Tuples
masalas = ("ginger", "Garlic" , "chilli")
(spice1 , spice2 , spice3) = masalas
print(f"spice1 : {spice1}\n spice2 : {spice2}\n spice3: {spice3}")

organic_ratio , inorganic_ratio = 2, 1

print( f" organic_ratio before swap: {organic_ratio}, inorganic_ratio : {inorganic_ratio} ")

organic_ratio , inorganic_ratio =   inorganic_ratio , organic_ratio

print( f" organic_ratio after swap : {organic_ratio}, inorganic_ratio : {inorganic_ratio} ")
print(f"check chilli in massala : {"chilli" in  masalas}")
print(f"check CHILII in massala : {"CHILLI" in  masalas}")
print(f"check  in tomato massala : {"tomato" in  masalas}")