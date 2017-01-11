#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 22:26:30 2017

@author: cclare
"""

import numpy as np
from astropy.io import fits
from astropy.table import Table, Column
from astropy.io import ascii
import matplotlib.pyplot as plt



llim = -0.000000000000001
print llim

version = 'Reduction/XShooter/TelluricCorrected/Version20161008/'
ext = 1

nir1= '/home/cclare/Stars/TZO/'+version+'XSHOO.2015-10-20T23:53:45.418/HV2112_SCI_SLIT_FLUX_MERGE1D_NIR_tac.fits'
print nir1

hdulist = fits.open(nir1)
nir1datatab = hdulist[ext].data

print hdulist