import numpy as np
from astropy.io import fits
from astropy.table import Table, Column
from astropy.io import ascii
import matplotlib.pyplot as plt

ulim =   1   #  0.00000000000002
llim = -1 #  -0.000000000000001

uvb1= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-20T23:53:37.544/HV2112_SCI_SLIT_FLUX_MERGE1D_UVB.fits'
hdulist = fits.open(uvb1)
uvb1dataraw = hdulist[0].data
in1v = (uvb1dataraw < ulim) & (uvb1dataraw > llim)
uvb1dataclean = uvb1dataraw[in1v]
npix1 = hdulist[0].header['NAXIS1']
swave1 = hdulist[0].header['CRVAL1']
sdelt1 = hdulist[0].header['CDELT1']
ewave1 = swave1+npix1*sdelt1 
uvb1wave = np.arange(swave1,ewave1,sdelt1)
uvb1waveclean = uvb1wave[in1v]
uvb1data = np.interp(uvb1wave, uvb1waveclean, uvb1dataclean)


uvb2= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T00:04:12.425/HV2112_SCI_SLIT_FLUX_MERGE1D_UVB.fits'
hdulist = fits.open(uvb2)
uvb2dataraw = hdulist[0].data
in2v = (uvb2dataraw < ulim) & (uvb2dataraw > llim)
uvb2dataclean = uvb2dataraw[in2v]
npix2 = hdulist[0].header['NAXIS1']
swave2 = hdulist[0].header['CRVAL1']
sdelt2 = hdulist[0].header['CDELT1']
ewave2 = swave2+npix2*sdelt2 
uvb2wave = np.arange(swave2,ewave2,sdelt2)
uvb2waveclean = uvb2wave[in2v]
uvb2data = np.interp(uvb1wave, uvb2waveclean, uvb2dataclean)


uvb3= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T00:14:51.476/HV2112_SCI_SLIT_FLUX_MERGE1D_UVB.fits'
hdulist = fits.open(uvb3)
uvb3dataraw = hdulist[0].data
in3v = (uvb3dataraw < ulim) & (uvb3dataraw > llim)
uvb3dataclean = uvb3dataraw[in3v]
npix3 = hdulist[0].header['NAXIS1']
swave3 = hdulist[0].header['CRVAL1']
sdelt3 = hdulist[0].header['CDELT1']
ewave3 = swave3+npix3*sdelt3 
uvb3wave = np.arange(swave3,ewave3,sdelt3)
uvb3waveclean = uvb3wave[in3v]
uvb3data = np.interp(uvb1wave, uvb3waveclean, uvb3dataclean)

uvb4= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T00:25:24.186/HV2112_SCI_SLIT_FLUX_MERGE1D_UVB.fits'
hdulist = fits.open(uvb4)
uvb4dataraw = hdulist[0].data
in4v = (uvb4dataraw < ulim) & (uvb4dataraw > llim)
uvb4dataclean = uvb4dataraw[in4v]
npix4 = hdulist[0].header['NAXIS1']
swave4 = hdulist[0].header['CRVAL1']
sdelt4 = hdulist[0].header['CDELT1']
ewave4 = swave4+npix4*sdelt4 
uvb4wave = np.arange(swave4,ewave4,sdelt4)
uvb4waveclean = uvb4wave[in4v]
uvb4data = np.interp(uvb1wave, uvb4waveclean, uvb4dataclean)

uvb5= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T00:35:57.196/HV2112_SCI_SLIT_FLUX_MERGE1D_UVB.fits'
hdulist = fits.open(uvb5)
uvb5dataraw = hdulist[0].data
in5v = (uvb5dataraw < ulim) & (uvb5dataraw > llim)
uvb5dataclean = uvb5dataraw[in5v]
npix5 = hdulist[0].header['NAXIS1']
swave5 = hdulist[0].header['CRVAL1']
sdelt5 = hdulist[0].header['CDELT1']
ewave5 = swave5+npix5*sdelt5 
uvb5wave = np.arange(swave5,ewave5,sdelt5)
uvb5waveclean = uvb5wave[in5v]
uvb5data = np.interp(uvb1wave, uvb5waveclean, uvb5dataclean)

fntsz = 10
wlim = 350
iwlim = uvb1wave > wlim

plt.subplot(6,1,1) 
plt.ion()
plt.plot(uvb1wave[iwlim],uvb1data[iwlim],'-k')
#plt.plot([0,15000],[0.0000000000004,0.0000000000004],'-r')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('UVB 1')
plt.show()

plt.subplot(6,1,2) 
plt.ion()
plt.plot(uvb1wave[iwlim],uvb2data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('UVB 2')
plt.show()

plt.subplot(6,1,3) 
plt.ion()
plt.plot(uvb1wave[iwlim],uvb3data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('UVB 3')
plt.show()

plt.subplot(6,1,4) 
plt.ion()
plt.plot(uvb1wave[iwlim],uvb4data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('UVB 4')
plt.show()

plt.subplot(6,1,5) 
plt.ion()
plt.plot(uvb1wave[iwlim],uvb5data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('UVB 5')
plt.show()

suvbdata = uvb1data+uvb2data+uvb3data+uvb4data+uvb5data

plt.subplot(6,1,6) 
plt.ion()
plt.plot(uvb1wave[iwlim],suvbdata[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('UVB Stacked')

plt.savefig('Figures/HV2112_stacking_UVB.pdf')
plt.show()

data = Table([uvb1wave[iwlim]*10,suvbdata[iwlim]], names=['wave', 'cflux'])
ascii.write(data, 'Tables/HV2112_stacked_UVB.dat')
