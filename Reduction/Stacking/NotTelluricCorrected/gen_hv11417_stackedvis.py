import numpy as np
from astropy.io import fits
from astropy.table import Table, Column
from astropy.io import ascii
import matplotlib.pyplot as plt

ulim = 1   #0.00000000000002
llim = -0.000000000000001

vis1= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T01:09:13.934/HV11417_SCI_SLIT_FLUX_MERGE1D_VIS.fits'
hdulist = fits.open(vis1)
vis1dataraw = hdulist[0].data
npix1 = hdulist[0].header['NAXIS1']
swave1 = hdulist[0].header['CRVAL1']
sdelt1 = hdulist[0].header['CDELT1']
ewave1 = swave1+npix1*sdelt1 
vis1wave = np.arange(swave1,ewave1,sdelt1)
in1v = (vis1dataraw < ulim) & (vis1dataraw > llim) & (vis1wave > 560)
vis1dataclean = vis1dataraw[in1v]
vis1waveclean = vis1wave[in1v]
vis1data = np.interp(vis1wave, vis1waveclean, vis1dataclean)


vis2= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T01:18:29.289/HV11417_SCI_SLIT_FLUX_MERGE1D_VIS.fits'
hdulist = fits.open(vis2)
vis2dataraw = hdulist[0].data
npix2 = hdulist[0].header['NAXIS1']
swave2 = hdulist[0].header['CRVAL1']
sdelt2 = hdulist[0].header['CDELT1']
ewave2 = swave2+npix2*sdelt2 
vis2wave = np.arange(swave2,ewave2,sdelt2)
in2v = (vis2dataraw < ulim) & (vis2dataraw > llim) & (vis2wave > 560)
vis2dataclean = vis2dataraw[in2v]
vis2waveclean = vis2wave[in2v]
vis2data = np.interp(vis1wave, vis2waveclean, vis2dataclean)


vis3= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T01:27:45.452/HV11417_SCI_SLIT_FLUX_MERGE1D_VIS.fits'
hdulist = fits.open(vis3)
vis3dataraw = hdulist[0].data
npix3 = hdulist[0].header['NAXIS1']
swave3 = hdulist[0].header['CRVAL1']
sdelt3 = hdulist[0].header['CDELT1']
ewave3 = swave3+npix3*sdelt3 
vis3wave = np.arange(swave3,ewave3,sdelt3)
in3v = (vis3dataraw < ulim) & (vis3dataraw > llim) & (vis3wave > 560)
vis3dataclean = vis3dataraw[in3v]
vis3waveclean = vis3wave[in3v]
vis3data = np.interp(vis1wave, vis3waveclean, vis3dataclean)

vis4= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T01:36:58.996/HV11417_SCI_SLIT_FLUX_MERGE1D_VIS.fits'
hdulist = fits.open(vis4)
vis4dataraw = hdulist[0].data
npix4 = hdulist[0].header['NAXIS1']
swave4 = hdulist[0].header['CRVAL1']
sdelt4 = hdulist[0].header['CDELT1']
ewave4 = swave4+npix4*sdelt4 
vis4wave = np.arange(swave4,ewave4,sdelt4)
in4v = (vis4dataraw < ulim) & (vis4dataraw > llim) & (vis4wave > 560)
vis4dataclean = vis4dataraw[in4v]
vis4waveclean = vis4wave[in4v]
vis4data = np.interp(vis1wave, vis4waveclean, vis4dataclean)

vis5= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T01:46:14.180/HV11417_SCI_SLIT_FLUX_MERGE1D_VIS.fits'
hdulist = fits.open(vis5)
vis5dataraw = hdulist[0].data
npix5 = hdulist[0].header['NAXIS1']
swave5 = hdulist[0].header['CRVAL1']
sdelt5 = hdulist[0].header['CDELT1']
ewave5 = swave5+npix5*sdelt5 
vis5wave = np.arange(swave5,ewave5,sdelt5)
in5v = (vis5dataraw < ulim) & (vis5dataraw > llim) & (vis5wave > 560)
vis5dataclean = vis5dataraw[in5v]
vis5waveclean = vis5wave[in5v]
vis5data = np.interp(vis1wave, vis5waveclean, vis5dataclean)


vis6= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T04:06:45.828/HV11417_SCI_SLIT_FLUX_MERGE1D_VIS.fits'
hdulist = fits.open(vis6)
vis6dataraw = hdulist[0].data
npix6 = hdulist[0].header['NAXIS1']
swave6 = hdulist[0].header['CRVAL1']
sdelt6 = hdulist[0].header['CDELT1']
ewave6 = swave6+npix6*sdelt6 
vis6wave = np.arange(swave6,ewave6,sdelt6)
in6v = (vis6dataraw < ulim) & (vis6dataraw > llim) & (vis6wave > 560)
vis6dataclean = vis6dataraw[in6v]
vis6waveclean = vis6wave[in6v]
vis6data = np.interp(vis1wave, vis6waveclean, vis6dataclean)


vis7= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T04:16:01.293/HV11417_SCI_SLIT_FLUX_MERGE1D_VIS.fits'
hdulist = fits.open(vis7)
vis7dataraw = hdulist[0].data
npix7 = hdulist[0].header['NAXIS1']
swave7 = hdulist[0].header['CRVAL1']
sdelt7 = hdulist[0].header['CDELT1']
ewave7 = swave7+npix7*sdelt7 
vis7wave = np.arange(swave7,ewave7,sdelt7)
in7v = (vis7dataraw < ulim) & (vis7dataraw > llim) & (vis7wave > 560)
vis7dataclean = vis7dataraw[in7v]
vis7waveclean = vis7wave[in7v]
vis7data = np.interp(vis1wave, vis7waveclean, vis7dataclean)


vis8= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T04:25:17.186/HV11417_SCI_SLIT_FLUX_MERGE1D_VIS.fits'
hdulist = fits.open(vis8)
vis8dataraw = hdulist[0].data
npix8 = hdulist[0].header['NAXIS1']
swave8 = hdulist[0].header['CRVAL1']
sdelt8 = hdulist[0].header['CDELT1']
ewave8 = swave8+npix8*sdelt8 
vis8wave = np.arange(swave8,ewave8,sdelt8)
in8v = (vis8dataraw < ulim) & (vis8dataraw > llim) & (vis8wave > 560)
vis8dataclean = vis8dataraw[in8v]
vis8waveclean = vis8wave[in8v]
vis8data = np.interp(vis1wave, vis8waveclean, vis8dataclean)


vis9= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T04:34:31.960/HV11417_SCI_SLIT_FLUX_MERGE1D_VIS.fits'
hdulist = fits.open(vis9)
vis9dataraw = hdulist[0].data
npix9 = hdulist[0].header['NAXIS1']
swave9 = hdulist[0].header['CRVAL1']
sdelt9 = hdulist[0].header['CDELT1']
ewave9 = swave9+npix9*sdelt9 
vis9wave = np.arange(swave9,ewave9,sdelt9)
in9v = (vis9dataraw < ulim) & (vis9dataraw > llim) & (vis9wave > 560)
vis9dataclean = vis9dataraw[in9v]
vis9waveclean = vis9wave[in9v]
vis9data = np.interp(vis1wave, vis9waveclean, vis9dataclean)


vis10= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T04:43:47.284/HV11417_SCI_SLIT_FLUX_MERGE1D_VIS.fits'
hdulist = fits.open(vis10)
vis10dataraw = hdulist[0].data
npix10 = hdulist[0].header['NAXIS1']
swave10 = hdulist[0].header['CRVAL1']
sdelt10 = hdulist[0].header['CDELT1']
ewave10 = swave10+npix10*sdelt10 
vis10wave = np.arange(swave10,ewave10,sdelt10)
in10v = (vis10dataraw < ulim) & (vis10dataraw > llim) & (vis10wave > 560)
vis10dataclean = vis10dataraw[in10v]
vis10waveclean = vis10wave[in10v]
vis10data = np.interp(vis1wave, vis10waveclean, vis10dataclean)


fntsz = 10
wlim = 560
iwlim = vis1wave > wlim

plt.subplot(6,2,1) 
plt.ion()
plt.plot(vis1wave[iwlim],vis1data[iwlim],'-k')
#plt.plot([0,15000],[0.0000000000004,0.0000000000004],'-r')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('HV11417: VIS 1')
plt.show()

plt.subplot(6,2,2) 
plt.ion()
plt.plot(vis1wave[iwlim],vis2data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('VIS 2')
plt.show()

plt.subplot(6,2,3) 
plt.ion()
plt.plot(vis1wave[iwlim],vis3data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('VIS 3')
plt.show()

plt.subplot(6,2,4) 
plt.ion()
plt.plot(vis1wave[iwlim],vis4data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('VIS 4')
plt.show()

plt.subplot(6,2,5) 
plt.ion()
plt.plot(vis1wave[iwlim],vis5data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('VIS 5')
plt.show()

plt.subplot(6,2,6) 
plt.ion()
plt.plot(vis1wave[iwlim],vis6data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('VIS 6')
plt.show()

plt.subplot(6,2,7) 
plt.ion()
plt.plot(vis1wave[iwlim],vis7data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('VIS 7')
plt.show()

plt.subplot(6,2,8) 
plt.ion()
plt.plot(vis1wave[iwlim],vis8data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('VIS 8')
plt.show()

plt.subplot(6,2,9) 
plt.ion()
plt.plot(vis1wave[iwlim],vis9data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('VIS 9')
plt.show()

plt.subplot(6,2,10) 
plt.ion()
plt.plot(vis1wave[iwlim],vis10data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('VIS 10')
plt.show()


svisdata = vis1data+vis2data+vis3data+vis4data+vis5data+vis6data+vis7data+vis8data+vis9data+vis10data

plt.subplot(6,2,12) 
plt.ion()
plt.plot(vis1wave[iwlim],svisdata[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('VIS Stacked')

plt.savefig('Figures/HV11417_stacking_VIS.pdf')
plt.show()

data = Table([vis1wave[iwlim]*10,svisdata[iwlim]], names=['wave', 'cflux'])
ascii.write(data, 'Tables/HV11417_stacked_VIS.dat')
