import numpy as np
from astropy.io import fits
from astropy.table import Table, Column
from astropy.io import ascii
import matplotlib.pyplot as plt

llim = -0.000000000000001

nir1= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-20T23:53:45.418/HV2112_SCI_SLIT_FLUX_MERGE1D_NIR.fits'
hdulist = fits.open(nir1)
nir1dataraw = hdulist[0].data
in1v = (nir1dataraw < 0.00000000000002) & (nir1dataraw > llim)
nir1dataclean = nir1dataraw[in1v]
npix1 = hdulist[0].header['NAXIS1']
swave1 = hdulist[0].header['CRVAL1']
sdelt1 = hdulist[0].header['CDELT1']
ewave1 = swave1+npix1*sdelt1 
nir1wave = np.arange(swave1,ewave1,sdelt1)
nir1waveclean = nir1wave[in1v]
nir1data = np.interp(nir1wave, nir1waveclean, nir1dataclean)


nir2= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T00:04:16.573/HV2112_SCI_SLIT_FLUX_MERGE1D_NIR.fits'
hdulist = fits.open(nir2)
nir2dataraw = hdulist[0].data
in2v = (nir2dataraw < 0.00000000000002) & (nir2dataraw > llim)
nir2dataclean = nir2dataraw[in2v]
npix2 = hdulist[0].header['NAXIS1']
swave2 = hdulist[0].header['CRVAL1']
sdelt2 = hdulist[0].header['CDELT1']
ewave2 = swave2+npix2*sdelt2 
nir2wave = np.arange(swave2,ewave2,sdelt2)
nir2waveclean = nir2wave[in2v]
nir2data = np.interp(nir1wave, nir2waveclean, nir2dataclean)


nir3= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T00:14:41.737/HV2112_SCI_SLIT_FLUX_MERGE1D_NIR.fits'
hdulist = fits.open(nir3)
nir3dataraw = hdulist[0].data
in3v = (nir3dataraw < 0.00000000000002) & (nir3dataraw > llim)
nir3dataclean = nir3dataraw[in3v]
npix3 = hdulist[0].header['NAXIS1']
swave3 = hdulist[0].header['CRVAL1']
sdelt3 = hdulist[0].header['CDELT1']
ewave3 = swave3+npix3*sdelt3 
nir3wave = np.arange(swave3,ewave3,sdelt3)
nir3waveclean = nir3wave[in3v]
nir3data = np.interp(nir1wave, nir3waveclean, nir3dataclean)

nir4= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T00:25:06.237/HV2112_SCI_SLIT_FLUX_MERGE1D_NIR.fits'
hdulist = fits.open(nir4)
nir4dataraw = hdulist[0].data
in4v = (nir4dataraw < 0.00000000000002) & (nir4dataraw > llim)
nir4dataclean = nir4dataraw[in4v]
npix4 = hdulist[0].header['NAXIS1']
swave4 = hdulist[0].header['CRVAL1']
sdelt4 = hdulist[0].header['CDELT1']
ewave4 = swave4+npix4*sdelt4 
nir4wave = np.arange(swave4,ewave4,sdelt4)
nir4waveclean = nir4wave[in4v]
nir4data = np.interp(nir1wave, nir4waveclean, nir4dataclean)

nir5= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T00:35:30.070/HV2112_SCI_SLIT_FLUX_MERGE1D_NIR.fits'
hdulist = fits.open(nir5)
nir5dataraw = hdulist[0].data
in5v = (nir5dataraw < 0.00000000000002) & (nir5dataraw > llim)
nir5dataclean = nir5dataraw[in5v]
npix5 = hdulist[0].header['NAXIS1']
swave5 = hdulist[0].header['CRVAL1']
sdelt5 = hdulist[0].header['CDELT1']
ewave5 = swave5+npix5*sdelt5 
nir5wave = np.arange(swave5,ewave5,sdelt5)
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
plt.show()

plt.subplot(6,1,2) 
plt.ion()
plt.plot(nir1wave,nir2data,'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('NIR 2')
plt.show()

plt.subplot(6,1,3) 
plt.ion()
plt.plot(nir1wave,nir3data,'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('NIR 3')
plt.show()

plt.subplot(6,1,4) 
plt.ion()
plt.plot(nir1wave,nir4data,'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('NIR 4')
plt.show()

plt.subplot(6,1,5) 
plt.ion()
plt.plot(nir1wave,nir5data,'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('NIR 5')
plt.show()

snirdata = nir1data+nir2data+nir3data+nir4data+nir5data

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
