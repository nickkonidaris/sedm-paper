

import numpy as np
import pyfits as pf


D = pf.open("rc20130622_15_10_45.fits")[0]

thetas = np.zeros((2048, 2048))

for i in xrange(2048):
    for j in xrange(2048):
        x = i-1024
        y = j-1024
        d = np.sqrt(x*x + y*y)*.0135

        thetas[i,j] = np.arcsin(d/95)

ct4 = np.cos(thetas)**4.0

hdu = pf.PrimaryHDU(D.data/ct4)
hdu.writeto("flat_d_ct4.fits")

