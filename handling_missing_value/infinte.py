#np.isinf(array) 10*1000
#1/0

import numpy as np 

arr = np.array([1,2,np.inf,3,-np.inf,5])
print(np.isinf(arr))
#for replcement 
cleaned_arr =np.nan_to_num(arr, posinf=11, neginf=99)
print(cleaned_arr)