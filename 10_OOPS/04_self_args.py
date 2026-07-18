#self : refer to variable in class 

class ChaiCup:
    size = 200 #ml

    def describe(self):
        return f"A {self.size}ml Chai Cup"
    
cup = ChaiCup()
print(cup.describe())
print(ChaiCup.describe(cup))

cup_twp = ChaiCup()
cup_twp.size = 100
print(cup_twp.describe())
print(ChaiCup.describe(cup_twp))