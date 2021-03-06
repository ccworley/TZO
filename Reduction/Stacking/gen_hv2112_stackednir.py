import numpy as np
from astropy.io import fits
from astropy.table import Table, Column
from astropy.io import ascii
import matplotlib.pyplot as plt

llim = -0.000000000000001

#version = 'MARCSFLX/XShooter/Version20160802/'
#ext = 0
version = 'Reduction/XShooter/TelluricCorrected/Version20161008/'
ext = 1

#python has 'lambda' reserved so it wont read in data.lambda. Need to rethink this.

nir1= '/home/cclare/Stars/TZO/'+version+'XSHOO.2015-10-20T23:53:45.418/HV2112_SCI_SLIT_FLUX_MERGE1D_NIR_tac.fits'
hdulist = fits.open(nir1)
nir1datatab = hdulist[ext].data
nir1dataraw = nir1datatab.cflux
in1v = (nir1dataraw < 0.00000000000002) & (nir1dataraw > llim)
nir1dataclean = nir1dataraw[in1v]
#npix1 = hdulist[ext].header['NAXIS1']
#swave1 = hdulist[ext].header['CRVAL1']
#sdelt1 = hdulist[ext].header['CDELT1']
#ewave1 = swave1+npix1*sdelt1 
nir1wave = nir1datatab.mlambda   #np.arange(swave1,ewave1,sdelt1)
nir1waveclean = nir1wave[in1v]
nir1data = np.interp(nir1wave, nir1waveclean, nir1dataclean)


nir2= '/home/cclare/Stars/TZO/'+version+'XSHOO.2015-10-21T00:04:16.573/HV2112_SCI_SLIT_FLUX_MERGE1D_NIR_tac.fits'
hdulist = fits.open(nir2)
nir2datatab = hdulist[ext].data
nir2dataraw = nir2datatab.cflux
in2v = (nir2dataraw < 0.00000000000002) & (nir2dataraw > llim)
nir2dataclean = nir2dataraw[in2v]
#npix2 = hdulist[ext].header['NAXIS1']
#swave2 = hdulist[ext].header['CRVAL1']
#sdelt2 = hdulist[ext].header['CDELT1']
#ewave2 = swave2+npix2*sdelt2 
nir2wave = nir2datatab.mlambda   #np.arange(swave2,ewave2,sdelt2)
nir2waveclean = nir2wave[in2v]
nir2data = np.interp(nir1wave, nir2waveclean, nir2dataclean)


nir3= '/home/cclare/Stars/TZO/'+version+'XSHOO.2015-10-21T00:14:41.737/HV2112_SCI_SLIT_FLUX_MERGE1D_NIR_tac.fits'
hdulist = fits.open(nir3)
nir3datatab = hdulist[ext].data
nir3dataraw = nir3datatab.cflux
in3v = (nir3dataraw < 0.00000000000002) & (nir3dataraw > llim)
nir3dataclean = nir3dataraw[in3v]
#npix3 = hdulist[ext].header['NAXIS1']
#swave3 = hdulist[ext].header['CRVAL1']
#sdelt3 = hdulist[ext].header['CDELT1']
#ewave3 = swave3+npix3*sdelt3 
nir3wave = nir3datatab.mlambda   #np.arange(swave3,ewave3,sdelt3)
nir3waveclean = nir3wave[in3v]
nir3data = np.interp(nir1wave, nir3waveclean, nir3dataclean)

nir4= '/home/cclare/Stars/TZO/'+version+'XSHOO.2015-10-21T00:25:06.237/HV2112_SCI_SLIT_FLUX_MERGE1D_NIR_tac.fits'
hdulist = fits.open(nir4)
nir4datatab = hdulist[ext].data
nir4dataraw = nir4datatab.cflux
in4v = (nir4dataraw < 0.00000000000002) & (nir4dataraw > llim)
nir4dataclean = nir4dataraw[in4v]
#npix4 = hdulist[ext].header['NAXIS1']
#swave4 = hdulist[ext].header['CRVAL1']
#sdelt4 = hdulist[ext].header['CDELT1']
#ewave4 = swave4+npix4*sdelt4 
nir4wave = nir4datatab.mlambda   #np.arange(swave4,ewave4,sdelt4)
nir4waveclean = nir4wave[in4v]
nir4data = np.interp(nir1wave, nir4waveclean, nir4dataclean)

nir5= '/home/cclare/Stars/TZO/'+version+'XSHOO.2015-10-21T00:35:30.070/HV2112_SCI_SLIT_FLUX_MERGE1D_NIR_tac.fits'
hdulist = fits.open(nir5)
nir5datatab = hdulist[ext].data
nir5dataraw = nir5datatab.cflux
in5v = (nir5dataraw < 0.00000000000002) & (nir5dataraw > llim)
nir5dataclean = nir5dataraw[in5v]
#npix5 = hdulist[ext].header['NAXIS1']
#swave5 = hdulist[ext].header['CRVAL1']
#sdelt5 = hdulist[ext].header['CDELT1']
#ewave5 = swave5+npix5*sdelt5 
nir5wave = nir5datatab.mlambda  #np.arange(swave5,ewave5,sdelt5)
nir5waveclean = nir5wave[in5v]
nir5data = np.interp(nir1wave, nir5waveclean, nir5dataclean)

fntsz = 10
wlim = 998
iwlim = nir1wave > wlim

plt.subplot(6,1,1) 
plt.ion()
plt.plot(nir1wave,nir1data,'-k')
#plt.plot([0,15000],[0.0000000000004,0.0000000000004],'-r')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('NIR 1')
#plt.show()

plt.subplot(6,1,2) 
plt.ion()
plt.plot(nir1wave,nir2data,'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('NIR 2')
#plt.show()

plt.subplot(6,1,3) 
plt.ion()
plt.plot(nir1wave,nir3data,'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('NIR 3')
#plt.show()

plt.subplot(6,1,4) 
plt.ion()
plt.plot(nir1wave,nir4data,'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('NIR 4')
#plt.show()

plt.subplot(6,1,5) 
plt.ion()
plt.plot(nir1wave,nir5data,'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('NIR 5')
#plt.show()

snirdata = nir1data+nir2data+nir3data+nir4data+nir5data
vnirdata = snirdata*0.02   #Need better account for variance

plt.subplot(6,1,6) 
plt.ion()
plt.plot(nir1wave,snirdata,'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('NIR Stacked')

plt.savefig('Figures/HV2112_stacking_NIR.pdf')
plt.show()

data = Table([nir1wave[iwlim]*10,snirdata[iwlim]], names=['wave', 'cflux'])
ascii.write(data, 'Tables/HV2112_stacked_NIR.dat')
