import numpy as np 
arr_2d = np.array([[2,4] , [6,7]])
print(arr_2d)
 
new_arr_2d = np.insert(arr_2d, 1, [2,4] , axis=0)
print(new_arr_2d)

#axis=0 used for row and axis = 1 used for row 


new_1= np.insert(arr_2d, 1, [3,4] , axis=1 )
print(new_1)
#its used for column 
#by using none to wo same line par print honga like stucture 
