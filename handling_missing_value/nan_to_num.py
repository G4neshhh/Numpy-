import numpy as np

arr= np.array([12,44,55,np.nan ,3 , np.nan])

cleaned_arr=np.nan_to_num(arr ,nan=100) #defualt value is zero '0' 
print(cleaned_arr)