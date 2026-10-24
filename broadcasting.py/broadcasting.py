prices = [100,200,300]
discount= 10
final_price= []

for price in prices :
    final_prices = price - (price * discount/100)
    final_price.append(final_prices)

print(final_price)