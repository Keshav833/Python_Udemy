# chai="adarak"
# def printThis(chai):
#     print(f"This function is printing {chai}")

# printThis(chai)

# totalCup = [1,2,3]

# def change(cup):
#     cup[1] = 32

# change(totalCup)
# print(f"{totalCup}")

# def make_order(chai , milk, sugar ):
#     print(f"A {sugar} sugar {milk} {chai} chai" )

# make_order("Kashmiri", "cream" , "low") # positional Argument
# make_order(sugar="High" , chai="Himachal" , milk="hot") # keyword Arugument

#mix arguement 

def reciepe(*ingredient , **extra):
    print(f"Ingredients: ",ingredient)
    print(f"Extras: ",extra)

reciepe("gajar", "Milk" ,"Sugar" , dry_fruits="almonds" , color="kesar")