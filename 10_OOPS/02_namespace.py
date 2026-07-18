class Chai:
    origin = "India"

print(Chai.origin)
Chai.is_Hot = True 
print(Chai.is_Hot)

masala = Chai()
print(masala.origin)
print(masala.is_Hot)

masala.is_Hot = False


print( Chai.is_Hot)#True  # chanage in instance  property dont effect the class itself 
print( masala.is_Hot)#False

masala.Flavour = "masala"
print( masala.Flavour)
print( Chai.Flavour) # give error 
