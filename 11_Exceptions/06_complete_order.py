class InvalidChaiError(Exception):pass

def bill(flavour,cups):
    menu= {"masala" : 20 , "ginger":40}
    try:
        if flavour not in menu:
            raise InvalidChaiError("that flavour is not available")
        if not isinstance(cups,int):
            raise TypeError("number of cups must be an integer")
        total = menu[flavour] * cups
        print(f"Your bill for {cups} cups of {flavour} chai : rupees {total} ")
    except Exception as e:
        print("Error :" ,e)
    finally:
        print("Thanks for coming....")

bill("mint",2)
bill("masala",2)
bill("masala","two")


