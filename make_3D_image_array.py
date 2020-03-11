# Comment for things and stuff
from matplotlib import pyplot as plt
import numpy as np
import os

wdir        =   os.getcwd()
startPic    =   104     # start of nozzle
endPic      =   570     # last pic
# pics= np.array([304,354,404,454,504])
pics = np.arange(startPic, endPic+1)

image_stack = np.zeros([pics.size,328,328])

# for i, var in enumerate(pics):
#     img = plt.imread('CT_data/CT_data%s.tif' % var)
#     img = img/65535.0
#     img = np.ma.masked_equal(img,0)
#     
#     image_stack[i,:,:] = img
# 
# np.save('CT_data.npy', image_stack)


image_stack = np.load('CT_data.npy')


