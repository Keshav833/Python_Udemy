def serve_chai():
    yield "Cup1 : Masala Chai"
    yield "Cup2 : Masala Chai"
    yield "Cup3 : Masala Chai"

stall = serve_chai()

# for cup in stall:
#     print(cup)

def get_chai_list():
    return ["cup 1" ,"cup 2" , "cup 3"]

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()

print(next(chai))
print(next(chai))
print(next(chai))
# print(next(chai)) # will give error 