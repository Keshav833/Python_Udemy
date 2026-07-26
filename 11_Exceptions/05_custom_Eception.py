class OutOfIngredientsError(Exception):
    pass

def make_chai(milk , suger):
    if milk == 0 or suger==0:
        raise OutOfIngredientsError("missing milk or suger")
    print("Chai is ready ...." )

make_chai(1,0)



#custome Error with Value Error
def brew_Chai(flavour):
    if flavour not in ["masala", "ginger", "elaichi", "kadak"]:
        raise ValueError("Unsupported Chai Flavour")
    print(f"Here is you order :{flavour} Chai ..")

brew_Chai("masala")
# brew_Chai("chilli")

