import numpy as np 
arr = np.array([22,4,5,666,7,4])
print(arr)
new_arr = np.delete(arr, 1)
print(new_arr)

import numpy as np 
text = "ganu"
arr = np.fromiter(text, "U2" )
print(arr)