file = open("order.txt","w")

try :
    file.write("Two masala Chai -40 rupees")
finally:
    file.close()

with open("order2.txt", "w") as file2:
    file2.write("ginger chai 2 cup: 60 ruppee")

