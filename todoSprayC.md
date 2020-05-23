Spray C to do:
==============

Distinguish from SAE WCX paper by Torelli et al. (2020)
-------------------------------------------------------

- [x] Steady State Simulation is enough to capture the accurate physics
- [x] Transient LES, and HRM? vs SS RANS, and HRM [model constants tweaking?]
- [ ] Effect of EOS [David] --> look at gas layer results and then bring in DPS
- [ ] Comment on LVF vs axial profiles [non-dimensional]
- [ ] Ambient gas vs NCG gas -- comment on this (as a result of fuel I/C)
- [ ] Pressure map [averaged over clips and/or just centerline]
- [ ] Velocity Contours
- [ ] Gas layer thickness component
- [ ] Two peaks plot (comment on effect of threshold) and show similar results in CFD and work on interpretability of that.
    - [ ] Binarize CFD and Expt data?
Edge detection algorithm [already exists]

Expt data extraction:


- [x] LVF vs axial distance
- [ ] Aniket's [Edge detection algorithm][aniket image stack py]
    - [ ] Area under fuel/gas
- [ ] Thresholding comment
- [ ] More rigor in analysis
    - [ ] Pressure vs radial at clips
    - [ ] Gas layer vs radial [we already have it]
- [ ] Effect of the back pressure
    - [ ] 0.1 MPa
    - [ ] 6 MPa


Next Steps:
-----------

Michael:

- [ ] Explore Edge Detection Algorithm [from Anikets' work]
- [ ] binarizeation methods
- [ ] scikit learn [binarizer][preprocessing]
- [ ] kmeans k=3 (vapor, liquid, out of domain) set non internal=-4 or something
- [ ] [SVM][scikit svm]
- [ ] radial average top half of nozzle and bottom half of nozzle at slices

Peetak:

- [ ] Account on sailfish for Michael
- [ ] Share CFD slices data w/ Michael or use his code to extract data
- [ ] Pressure vs radial? [How to do it?]

Explore

- [ ] [Algorithmic][matlab edge detection] aspect to read/extract data from CT scans


SVM - regression tool

Next Step [after basic progress]
--------------------------------
- [ ] Use utility for mapping cells from unstructured to structured


[aniket image stack py]: https://github.com/aniketkt/ImageStackPy/blob/master/ImageStackPy/ImageProcessing.py
[preprocessing]: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Binarizer.html#sklearn.preprocessing.Binarizer
[scikit svm]: https://scikit-learn.org/stable/modules/classes.html#module-sklearn.svm
[matlab edge detection]: https://www.mathworks.com/discovery/edge-detection.html
