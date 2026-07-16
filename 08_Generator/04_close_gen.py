def local_chai():
    yield "Masala Chai"
    yield "Adarak Chai"

def urban_Coffe():
    yield "latte"
    yield "capochino"
    yield "black Coffee"

def full_menu():
    yield from local_chai()
    yield from urban_Coffe()

# for chai in full_menu():
#     print(chai)

def chai_stall():
    try:
        while True:
            order = yield "Waiting for the order"
    except:
        print("Stall Closed , NO more chai")

stall = chai_stall()
print(next(stall))
stall.close() #clean up
# print(next(stall))

