import numpy as np 

price = np.array([100,200,300,500,800])
discount = 20
new_price = price - (price * discount/100)
print(new_price)
