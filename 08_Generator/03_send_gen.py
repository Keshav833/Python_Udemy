def chai_customer():
    print("Welcome ! What chai would you like ")
    order = yield 
    while True:
        print(f"Preparing : {order}")
        order = yield

stall = chai_customer()
next(stall) # start the generator
next(stall) # we have given nothing so order will be none
stall.send("Masala Chai")
stall.send("Adarak Chai")
stall.send("ilaichi  Chai")

# yield pauses the generator and can both return a value to the caller and receive a value back 
# when execution resumes with send(value).

# next(generator) starts or resumes the generator by sending None,
#  while generator.send(value) resumes it and assigns that value to the variable on the left of yield (e.g., order = yield). Python really looked at "pause" and decided it should also double as a mailbox.


