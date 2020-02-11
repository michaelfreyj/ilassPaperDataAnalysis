# Comment for things and stuff
from matplotlib import pyplot as plt
import numpy as np
import pyvista as vtki
import os

wdir        =   os.getcwd()
startPic    =   104     # start of nozzle
endPic      =   570     # last pic
threshold   =   0.5     # threshold for LVF using exp data
nBinsExp    =   1000    # number of bins for the exp histograms
nBinsCFD    =   1000    # number of bins for the cfd histograms
figWidth    =   6.4     # hist figure width
figHeight   =   4.8     # hist figure height
caseDir     =   '6mpa'
surfaceDir  =   'postProcessing/surfaces/0.00063'
expDir      =   'CT_data'


pics= np.array([304,354,404,454,504])


for var in pics:
    img = plt.imread('%s/%s/CT_data%s.tif' % (wdir, expDir, var))
    img = img.flatten()
    img = img/65535.0
    img = np.ma.masked_equal(img,0)
    rho = vtki.PolyData('%s/%s/%s/rho_x%s.vtk' % (wdir,caseDir,surfaceDir,var)).point_arrays['rho']
    rhog = vtki.PolyData('%s/%s/%s/rhog_x%s.vtk' % (wdir,caseDir,surfaceDir,var)).point_arrays['rhog']
    alphaFrac = vtki.PolyData('%s/%s/%s/alphaFrac_x%s.vtk' % (wdir,caseDir,surfaceDir,var)).point_arrays['alphaFrac']
    y = vtki.PolyData('%s/%s/%s/y_x%s.vtk' % (wdir,caseDir,surfaceDir,var)).point_arrays['y']
    lvf = (1-alphaFrac)*(1-y*(rho/rhog))

    fig = plt.figure(figsize=[figWidth,figHeight])
    fig.suptitle('Histogram at slice %s' % var)
    fig.add_subplot(1,2,1)
    plt.xlabel("Pixel value / Intensity (i)")
    plt.ylabel("Number of pixels")
    plt.title('Experimental')
    hist, bins, ignored = plt.hist(img,bins=nBinsExp)
    fig.add_subplot(1,2,2)
    plt.xlabel("LVF")
    plt.xlim(0,1)
    plt.ylabel("Number of cells")
    plt.title('CFD')
    hist, bins, ignored = plt.hist(lvf,bins=nBinsCFD)
    plt.savefig('figs/hist%s.png' % var, dpi=300)

