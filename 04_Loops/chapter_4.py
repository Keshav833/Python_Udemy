#ZIP to iteate muiltiple list in parallel

name = ["Kalu", "Lala" , "Bala" , "Shala"]
bill = [40 , 22 , 50, 95]

for first , second in zip(name , bill):
    print(f"{first} : {second}")