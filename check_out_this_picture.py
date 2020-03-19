import numpy as np
import matplotlib.pyplot as plt

try:
    image_stack = np.load('CT_data.npy')
except FileNotFoundError:
    try:
        startPic    =   104     # start of nozzle
        endPic      =   570     # last pic
        pics = np.arange(startPic, endPic+1)
        image_stack = np.zeros([pics.size,328,328])

        for i, var in enumerate(pics):
            img = plt.imread('CT_data/CT_data%s.tif' % var)
            img = img/65535.0
            img = np.ma.masked_equal(img,0)
            
            image_stack[i,:,:] = img

        np.save('CT_data.npy', image_stack)
    except FileNotFoundError:
        exit("Please make sure the CT_data files are in the right location")

image_stack.shape

# slice at the midpoint
trans_slice = image_stack[:,:,164]

# transpose to show flow from left to right
# instead of top to bottom
trans_slice_T = trans_slice.transpose()
trans_slice_T = np.ma.masked_where(trans_slice_T < 0.001, trans_slice_T)

plt.imshow(trans_slice_T, cmap='gray')
plt.xlabel('Axial')
plt.ylabel('Radial')
plt.title('XRay Data: Transverse Slice')
plt.colorbar()
plt.savefig('nozzle_transverse_slice_gray.png', dpi=300)
# plt.show()
