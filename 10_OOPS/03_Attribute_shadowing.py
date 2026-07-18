#varibles when comes inside class or object  its called attribute
class Chai:
    temperature = "Hot"
    strength = "strong"

cutting_chai  = Chai()
print("Class Chai temperature: ",cutting_chai.temperature)

cutting_chai.temperature = "mild"
cutting_chai.cup = "large"
print("After Changing ", cutting_chai.temperature)
print("Cup Size ", cutting_chai.temperature)

del cutting_chai.temperature

print(cutting_chai.temperature) # Hot 
#even after del object attribute it will show base class attr value 
del cutting_chai.cup
#but when we delete attribute which not present in base class it will give att(not found) error
print(cutting_chai.cup) 




