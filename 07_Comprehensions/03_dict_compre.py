tea_prices = {
    "Masala_chai": 30 ,
    "Green_Chai" : 50 ,
    "Lemon Tea":200
}

tea_prices_usd = {tea:price/80 for tea ,price in tea_prices.items()}

print(tea_prices_usd)

