import numpy as np
from astropy.io import fits
from astropy.table import Table, Column
from astropy.io import ascii
import matplotlib.pyplot as plt

llim = -0.000000000000001

nir1= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T01:09:17.293/HV11417_SCI_SLIT_FLUX_MERGE1D_NIR.fits'
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


nir2= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T01:19:47.118/HV11417_SCI_SLIT_FLUX_MERGE1D_NIR.fits'
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


nir3= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T01:30:12.282/HV11417_SCI_SLIT_FLUX_MERGE1D_NIR.fits'
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

nir4= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T04:06:48.628/HV11417_SCI_SLIT_FLUX_MERGE1D_NIR.fits'
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

nir5= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T04:17:19.780/HV11417_SCI_SLIT_FLUX_MERGE1D_NIR.fits'
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


nir6= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T04:27:44.279/HV11417_SCI_SLIT_FLUX_MERGE1D_NIR.fits'
hdulist = fits.open(nir6)
nir6dataraw = hdulist[0].data
in6v = (nir6dataraw < 0.00000000000002) & (nir6dataraw > llim)
nir6dataclean = nir6dataraw[in6v]
npix6 = hdulist[0].header['NAXIS1']
swave6 = hdulist[0].header['CRVAL1']
sdelt6 = hdulist[0].header['CDELT1']
ewave6 = swave6+npix6*sdelt6 
nir6wave = np.arange(swave6,ewave6,sdelt6)
nir6waveclean = nir6wave[in6v]
nir6data = np.interp(nir1wave, nir6waveclean, nir6dataclean)



nir7= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T04:38:08.778/HV11417_SCI_SLIT_FLUX_MERGE1D_NIR.fits'
hdulist = fits.open(nir7)
nir7dataraw = hdulist[0].data
in7v = (nir7dataraw < 0.00000000000002) & (nir7dataraw > llim)
nir7dataclean = nir7dataraw[in7v]
npix7 = hdulist[0].header['NAXIS1']
swave7 = hdulist[0].header['CRVAL1']
sdelt7 = hdulist[0].header['CDELT1']
ewave7 = swave7+npix7*sdelt7 
nir7wave = np.arange(swave7,ewave7,sdelt7)
nir7waveclean = nir7wave[in7v]
nir7data = np.interp(nir1wave, nir7waveclean, nir7dataclean)



nir8= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T04:48:33.275/HV11417_SCI_SLIT_FLUX_MERGE1D_NIR.fits'
hdulist = fits.open(nir8)
nir8dataraw = hdulist[0].data
in8v = (nir8dataraw < 0.00000000000002) & (nir8dataraw > llim)
nir8dataclean = nir8dataraw[in8v]
npix8 = hdulist[0].header['NAXIS1']
swave8 = hdulist[0].header['CRVAL1']
sdelt8 = hdulist[0].header['CDELT1']
ewave8 = swave8+npix8*sdelt8 
nir8wave = np.arange(swave8,ewave8,sdelt8)
nir8waveclean = nir8wave[in8v]
nir8data = np.interp(nir1wave, nir8waveclean, nir8dataclean)


fntsz = 10
wlim = 998
iwlim = nir1wave > wlim

plt.subplot(9,1,1) 
plt.ion()
plt.plot(nir1wave,nir1data,'-k')
#plt.plot([0,15000],[0.0000000000004,0.0000000000004],'-r')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('HV11417: NIR 1')
plt.show()

plt.subplot(9,1,2) 
plt.ion()
plt.plot(nir1wave,nir2data,'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('NIR 2')
plt.show()

plt.subplot(9,1,3) 
plt.ion()
plt.plot(nir1wave,nir3data,'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('NIR 3')
plt.show()

plt.subplot(9,1,4) 
plt.ion()
plt.plot(nir1wave,nir4data,'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('NIR 4')
plt.show()

plt.subplot(9,1,5) 
plt.ion()
plt.plot(nir1wave,nir5data,'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('NIR 5')
plt.show()

plt.subplot(9,1,6) 
plt.ion()
plt.plot(nir1wave,nir6data,'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('NIR 6')
plt.show()

plt.subplot(9,1,7) 
plt.ion()
plt.plot(nir1wave,nir7data,'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('NIR 7')
plt.show()

plt.subplot(9,1,8) 
plt.ion()
plt.plot(nir1wave,nir8data,'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('NIR 8')
plt.show()

snirdata = nir1data+nir2data+nir3data+nir4data+nir5data+nir6data+nir7data+nir8data

plt.subplot(9,1,9) 
plt.ion()
plt.plot(nir1wave,snirdata,'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('NIR Stacked')

plt.savefig('Figures/HV11417_stacking_NIR.pdf')
plt.show()

data = Table([nir1wave[iwlim]*10,snirdata[iwlim]], names=['wave', 'cflux'])
ascii.write(data, 'Tables/HV11417_stacked_NIR.dat')
