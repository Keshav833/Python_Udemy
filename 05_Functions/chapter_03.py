# def calculate_bill(cups, price_per_cup):
#     return cups *price_per_cup

# print(f"{calculate_bill(8,20)}")
# print(f"{calculate_bill(4,30)}")
# print(f"{calculate_bill(18,10)}")


def add_vat(price, vat_rate):
    return price * ( 100 + vat_rate)/100

orders = [100, 300 , 200]
for price in orders:
    final_amt = add_vat(price,10)
    print(f"{final_amt}")