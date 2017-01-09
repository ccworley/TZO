import numpy as np
from astropy.io import fits
from astropy.table import Table, Column
from astropy.io import ascii
import matplotlib.pyplot as plt

ulim =   1   #  0.00000000000002
llim = -1 #  -0.000000000000001

uvb1= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T01:09:08.744/HV11417_SCI_SLIT_FLUX_MERGE1D_UVB.fits'
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


uvb2= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T01:19:43.444/HV11417_SCI_SLIT_FLUX_MERGE1D_UVB.fits'
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


uvb3= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T01:30:21.934/HV11417_SCI_SLIT_FLUX_MERGE1D_UVB.fits'
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

uvb4= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T01:40:54.195/HV11417_SCI_SLIT_FLUX_MERGE1D_UVB.fits'
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

uvb5= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T04:06:40.698/HV11417_SCI_SLIT_FLUX_MERGE1D_UVB.fits'
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


uvb6= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T04:17:15.608/HV11417_SCI_SLIT_FLUX_MERGE1D_UVB.fits'
hdulist = fits.open(uvb6)
uvb6dataraw = hdulist[0].data
in6v = (uvb6dataraw < ulim) & (uvb6dataraw > llim)
uvb6dataclean = uvb6dataraw[in6v]
npix6 = hdulist[0].header['NAXIS1']
swave6 = hdulist[0].header['CRVAL1']
sdelt6 = hdulist[0].header['CDELT1']
ewave6 = swave6+npix6*sdelt6 
uvb6wave = np.arange(swave6,ewave6,sdelt6)
uvb6waveclean = uvb6wave[in6v]
uvb6data = np.interp(uvb1wave, uvb6waveclean, uvb6dataclean)


uvb7= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T04:27:53.929/HV11417_SCI_SLIT_FLUX_MERGE1D_UVB.fits'
hdulist = fits.open(uvb7)
uvb7dataraw = hdulist[0].data
in7v = (uvb7dataraw < ulim) & (uvb7dataraw > llim)
uvb7dataclean = uvb7dataraw[in7v]
npix7 = hdulist[0].header['NAXIS1']
swave7 = hdulist[0].header['CRVAL1']
sdelt7 = hdulist[0].header['CDELT1']
ewave7 = swave7+npix7*sdelt7 
uvb7wave = np.arange(swave7,ewave7,sdelt7)
uvb7waveclean = uvb7wave[in7v]
uvb7data = np.interp(uvb1wave, uvb7waveclean, uvb7dataclean)


uvb8= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T04:38:27.289/HV11417_SCI_SLIT_FLUX_MERGE1D_UVB.fits'
hdulist = fits.open(uvb8)
uvb8dataraw = hdulist[0].data
in8v = (uvb8dataraw < ulim) & (uvb8dataraw > llim)
uvb8dataclean = uvb8dataraw[in8v]
npix8 = hdulist[0].header['NAXIS1']
swave8 = hdulist[0].header['CRVAL1']
sdelt8 = hdulist[0].header['CDELT1']
ewave8 = swave8+npix8*sdelt8 
uvb8wave = np.arange(swave8,ewave8,sdelt8)
uvb8waveclean = uvb8wave[in8v]
uvb8data = np.interp(uvb1wave, uvb8waveclean, uvb8dataclean)


uvb9= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T04:49:00.459/HV11417_SCI_SLIT_FLUX_MERGE1D_UVB.fits'
hdulist = fits.open(uvb9)
uvb9dataraw = hdulist[0].data
in9v = (uvb9dataraw < ulim) & (uvb9dataraw > llim)
uvb9dataclean = uvb9dataraw[in9v]
npix9 = hdulist[0].header['NAXIS1']
swave9 = hdulist[0].header['CRVAL1']
sdelt9 = hdulist[0].header['CDELT1']
ewave9 = swave9+npix9*sdelt9 
uvb9wave = np.arange(swave9,ewave9,sdelt9)
uvb9waveclean = uvb9wave[in9v]
uvb9data = np.interp(uvb1wave, uvb9waveclean, uvb9dataclean)


fntsz = 10
wlim = 350
iwlim = uvb1wave > wlim

plt.subplot(5,2,1) 
plt.ion()
plt.plot(uvb1wave[iwlim],uvb1data[iwlim],'-k')
#plt.plot([0,15000],[0.0000000000004,0.0000000000004],'-r')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('HV11417: UVB 1')
plt.show()

plt.subplot(5,2,2) 
plt.ion()
plt.plot(uvb1wave[iwlim],uvb2data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('UVB 2')
plt.show()

plt.subplot(5,2,3) 
plt.ion()
plt.plot(uvb1wave[iwlim],uvb3data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('UVB 3')
plt.show()

plt.subplot(5,2,4) 
plt.ion()
plt.plot(uvb1wave[iwlim],uvb4data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('UVB 4')
plt.show()

plt.subplot(5,2,5) 
plt.ion()
plt.plot(uvb1wave[iwlim],uvb5data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('UVB 5')
plt.show()

plt.subplot(5,2,6) 
plt.ion()
plt.plot(uvb1wave[iwlim],uvb6data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('UVB 6')
plt.show()

plt.subplot(5,2,7) 
plt.ion()
plt.plot(uvb1wave[iwlim],uvb7data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('UVB 7')
plt.show()

plt.subplot(5,2,8) 
plt.ion()
plt.plot(uvb1wave[iwlim],uvb8data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('UVB 8')
plt.show()

plt.subplot(5,2,9) 
plt.ion()
plt.plot(uvb1wave[iwlim],uvb9data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('UVB 9')
plt.show()

suvbdata = uvb1data+uvb2data+uvb3data+uvb4data+uvb5data+uvb6data+uvb7data+uvb8data+uvb9data

plt.subplot(5,2,10) 
plt.ion()
plt.plot(uvb1wave[iwlim],suvbdata[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('UVB Stacked')

plt.savefig('Figures/HV11417_stacking_UVB.pdf')
plt.show()

data = Table([uvb1wave[iwlim]*10,suvbdata[iwlim]], names=['wave', 'cflux'])
ascii.write(data, 'Tables/HV11417_stacked_UVB.dat')
