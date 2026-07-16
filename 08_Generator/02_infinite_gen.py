def infinte():
    count=0
    while True:
        yield f"Refill {count}"
        count+=1
    
user1 = infinte()
user2 = infinte()

for _ in range(5):
    print(next(user1))

for _ in range(2):
    print(next(user2))