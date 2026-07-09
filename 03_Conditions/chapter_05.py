train_seat  = input("Enter TRain Seat name - ")

match train_seat:
    case "general":
        print( f"seat nahi hai garib")
    case "sleeper":
        print( f"Aaye apne  seat legiye")
    case "AC3":
        print( f"Aye apne ac seat ka anand ligiye")
    case "AC1":
        print( f"Aree sir mere sir  pai bhaithine")
    case _:
        print(f"Tu to gaya bete - nikal 2000 Ka fine")
