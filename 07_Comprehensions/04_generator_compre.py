daily_sales = [5,8,4,2,6,12,16,24]

total_cups = sum( sale for sale in daily_sales if sale>10)
print(total_cups)