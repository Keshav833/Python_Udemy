my_type = "Hot and Sweet"
drink  = "Coffee"
print( f" I want {my_type} {drink} Please !")
description = "thick and creamy"

print(f"first word: {description[:6]}")
print(f"last word: {description[10:]}")
print(f"reverse each character in word {description}: {description[::-1]}")

coupon_code = "Cold Drink"
encoded_code = coupon_code.encode("utf-8")
print(f"encoded Coupon Code : {coupon_code}")
print(f"encoded Coupon Code : {encoded_code}")
decoded_code = encoded_code.decode("utf-8")

print(f"decoded Coupon Code : {decoded_code}")