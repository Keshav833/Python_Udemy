#recursion
def count(n):
    print(n)

    if( n == 0):
        return "count down ends"
    
    return count(n-1)

print(count(9))

#lambda

chai_type = ["adrak", "ginger", "ilaichi", "plain"]

simple_chai = list(filter(lambda chai : chai!="adrak", chai_type))

print(simple_chai)