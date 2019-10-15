# LambdaLambda

Feasibility study for the new method of measuring the electrons beam polarization at a Super Charm Tau Factory (symetric e+e- collider).

The key idea is angular analysis of the process `e+e- -> [Lambda -> p pi-] [anti-Lambda -> p pi+]`

## [Lib](lib)
### [beamfield.py](lib/beamfield.py)
Estimates for beam field effect

### [bhabha.py](lib/bhabha.py)
Estimates for Bha-Bha statistics related to luminosity monitoring

### [driver.py](lib/driver.py)

### [driver2.py](lib/driver2.py)

### [fbasym.py](lib/fbasym.py)

### [pars.py](lib/pars.py)

### [pdfs.py](lib/pdfs.py)

### [reader.py](lib/reader.py)

## [Draw](draw)
### [bias.py](draw/bias.py)
* drawFitBias
* drawFitBiasXi

### [corrmtx.py](draw/corrmtx.py)
* drawCorrMtx
* drawCorrAB

### [hmap.py](draw/hmap.py)
* heatmap
* annotate_heatmap

### [plotPhi.py](draw/plotPhi.py)
* plotPhi

### [plotter.py](draw/plotter.py)
* protonMomentumSpec
* protonPolarCMS
* plot1D
* plot2D
* plotTheta
* plotPhi
* main

### [precision.py](draw/precision.py)
* drawPrecisionNevt
* drawPrecision
* asymPrecision

## [Fit](fit)
### [fitter.py](fit/fitter.py)
* class FitFull: Complete 5D fit with polarization
* class FitFullUnpolarized: 5D fit for Lambda formfactors without polarized beam
* class FitPhi: Azimuthal distribution 1D fit
* class FitFB2D: Forward-backward distribution 2D fit
* class FitSSide: Single-side full 3D fit

### [simfit.py](fit/simfit.py)
* class SimFitSS
* class SimFitFull
