def serve_chai(flavor):
    try :
        print(f"preparing {flavor } Chai ...")
        if flavor == "unknown":
            raise ValueError("We dont know that flavour")
    except ValueError as e:
        print("Error:" , e)
    else:
        print( f"{flavor} chai is served")
    finally:
        print("next customer please")

serve_chai("unknown")
        