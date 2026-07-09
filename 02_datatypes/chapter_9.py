#Sets - using {} and are mutable
essential_spices = {"ginger", "chilli" , "cinnimon"}
optional_spices = {"cloves", "ginger" , "cardimon" , "black pepper"}

all_spices = essential_spices | optional_spices
print(f"All Spices: {all_spices}")

common_spices = essential_spices & optional_spices

print(f"Common Spices: {common_spices}")

Only_in_essential = essential_spices - optional_spices
print(f"Only in essential Spices: {Only_in_essential}")

print(f"is ginger present in essential spices : { "ginger" in essential_spices}")

