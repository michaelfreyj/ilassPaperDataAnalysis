# ilassPaperDataAnalysis
scripts and stuff

Need the script to be in the same directory as the CT_data directory and the OpenFOAM case directory.

The "surfaces" file can be copied into the system dir of the OpenFOAM case and the postProcessing utility will produce data the specified data from the case.
Note that the cross sections to be compared are stored in the "pics" variable in the python script.
In the following example of "pics", the CT_200.tif would be compared the the OpenFOAM slice x200.vtk slices and CT_300.tif would be compared the the OpenFOAM slice x300.vtk slices.

```
pics = np.array([200,300])
```


## Updates 2020-03-11 (MF)

Created wrote a script to get LVF vs nozzle axis, `LVF_plot.py`.

Created script to create a 3D array of the image stack, `make_3D_image_array.py`

Added the array created from aformentioned script: `CT_data.npy`

Created a small script to load the 3D image array, make a transverse slice, and display that transvers image.


