import numpy as np
import matplotlib.pyplot as plt

image_stack = np.load('CT_data.npy')
image_stack.shape

# slice at the midpoint
trans_slice = image_stack[:,:,164]

# transpose to show flow from left to right
# instead of top to bottom
trans_slice_T = trans_slice.transpose()
trans_slice_T = np.ma.masked_where(trans_slice_T < 0.001, trans_slice_T)

plt.imshow(trans_slice_T, cmap='gray')
plt.show()
