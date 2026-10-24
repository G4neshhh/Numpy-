import numpy as np
arr = np.array([22,445,6,77])
arr_1 = np.array([23,56,7,88])

new_arr= np.concatenate((arr,arr_1, ))
print(new_arr)