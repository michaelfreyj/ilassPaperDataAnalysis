# Comment for things and stuff
from matplotlib import pyplot as plt
import numpy as np
import os

wdir        =   os.getcwd()
startPic    =   104     # start of nozzle
endPic      =   570     # last pic
threshold   =   0.5     # threshold for LVF using exp data
nBinsExp    =   1000    # number of bins for the exp histograms
figWidth    =   6.4     # hist figure width
figHeight   =   4.8     # hist figure height
expDir      =   'CT_data'
lvf         = []
axial_distance = np.arange(0,978.7,2.1)
# pics= np.array([304,354,404,454,504])
pics = np.arange(startPic, endPic+1)

# Find a threshold
# make cummulative histogram and define threshold as lowest point in the
# valley

# image_stack = np.load('CT_data.npy')
# flat_image_stack = image_stack.flatten()
# flat_image_stack = np.ma.masked_less(flat_image_stack,0.001)
# hist, bins, ignored = plt.hist(flat_image_stack1,bins=1000)
# newHist = hist[400:800]
# threshold = float(bins[np.where(hist == newHist.min())])
# plt.vlines(threshold,0,hist.max(),label='Threshold')
# plt.text(x=threshold, y=20e3, s='Threshold', alpha=0.7)
# plt.savefig('threshold.png', dpi=300)

# calculated from previous exp
threshold = 0.5545784695201038

for var in pics:
    img = plt.imread('%s/%s/CT_data%s.tif' % (wdir, expDir, var))
    img = img.flatten()
    img = img/65535.0
    img = np.ma.masked_equal(img,0)
    
    liquid_phase  = img[np.where( img >= threshold )].size
    total = np.ma.MaskedArray.count(img)
    lvf.append(liquid_phase/total)



# hist, bins, ignored = plt.hist(img,bins=nBinsExp)
plt.plot(axial_distance, lvf)
plt.xlabel("Length Along Nozzle Axis")
plt.ylim(0,1)
plt.xlim(0,axial_distance.max())
plt.ylabel("LVF [-]")
plt.title('Experimental Data')
# plt.show()
plt.grid()
plt.savefig('LVF_vs_nozzle_axis.png' % var, dpi=300)

