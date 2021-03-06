import numpy as np
from astropy.io import fits
from astropy.table import Table, Column
from astropy.io import ascii
import matplotlib.pyplot as plt

ulim = 1   #0.00000000000002
llim = -0.000000000000001

vis1= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-20T23:53:42.675/HV2112_SCI_SLIT_FLUX_MERGE1D_VIS.fits'
hdulist = fits.open(vis1)
vis1dataraw = hdulist[0].data
in1v = (vis1dataraw < ulim) & (vis1dataraw > llim)
vis1dataclean = vis1dataraw[in1v]
npix1 = hdulist[0].header['NAXIS1']
swave1 = hdulist[0].header['CRVAL1']
sdelt1 = hdulist[0].header['CDELT1']
ewave1 = swave1+npix1*sdelt1 
vis1wave = np.arange(swave1,ewave1,sdelt1)
vis1waveclean = vis1wave[in1v]
vis1data = np.interp(vis1wave, vis1waveclean, vis1dataclean)


vis2= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T00:02:58.210/HV2112_SCI_SLIT_FLUX_MERGE1D_VIS.fits'
hdulist = fits.open(vis2)
vis2dataraw = hdulist[0].data
in2v = (vis2dataraw < ulim) & (vis2dataraw > llim)
vis2dataclean = vis2dataraw[in2v]
npix2 = hdulist[0].header['NAXIS1']
swave2 = hdulist[0].header['CRVAL1']
sdelt2 = hdulist[0].header['CDELT1']
ewave2 = swave2+npix2*sdelt2 
vis2wave = np.arange(swave2,ewave2,sdelt2)
vis2waveclean = vis2wave[in2v]
vis2data = np.interp(vis1wave, vis2waveclean, vis2dataclean)


vis3= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T00:12:13.473/HV2112_SCI_SLIT_FLUX_MERGE1D_VIS.fits'
hdulist = fits.open(vis3)
vis3dataraw = hdulist[0].data
in3v = (vis3dataraw < ulim) & (vis3dataraw > llim)
vis3dataclean = vis3dataraw[in3v]
npix3 = hdulist[0].header['NAXIS1']
swave3 = hdulist[0].header['CRVAL1']
sdelt3 = hdulist[0].header['CDELT1']
ewave3 = swave3+npix3*sdelt3 
vis3wave = np.arange(swave3,ewave3,sdelt3)
vis3waveclean = vis3wave[in3v]
vis3data = np.interp(vis1wave, vis3waveclean, vis3dataclean)

vis4= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T00:21:29.277/HV2112_SCI_SLIT_FLUX_MERGE1D_VIS.fits'
hdulist = fits.open(vis4)
vis4dataraw = hdulist[0].data
in4v = (vis4dataraw < ulim) & (vis4dataraw > llim)
vis4dataclean = vis4dataraw[in4v]
npix4 = hdulist[0].header['NAXIS1']
swave4 = hdulist[0].header['CRVAL1']
sdelt4 = hdulist[0].header['CDELT1']
ewave4 = swave4+npix4*sdelt4 
vis4wave = np.arange(swave4,ewave4,sdelt4)
vis4waveclean = vis4wave[in4v]
vis4data = np.interp(vis1wave, vis4waveclean, vis4dataclean)

vis5= '/home/cclare/Stars/TZO/MARCSFLX/XShooter/Version20160802/XSHOO.2015-10-21T00:30:44.181/HV2112_SCI_SLIT_FLUX_MERGE1D_VIS.fits'
hdulist = fits.open(vis5)
vis5dataraw = hdulist[0].data
in5v = (vis5dataraw < ulim) & (vis5dataraw > llim)
vis5dataclean = vis5dataraw[in5v]
npix5 = hdulist[0].header['NAXIS1']
swave5 = hdulist[0].header['CRVAL1']
sdelt5 = hdulist[0].header['CDELT1']
ewave5 = swave5+npix5*sdelt5 
vis5wave = np.arange(swave5,ewave5,sdelt5)
vis5waveclean = vis5wave[in5v]
vis5data = np.interp(vis1wave, vis5waveclean, vis5dataclean)

fntsz = 10
wlim = 560
iwlim = vis1wave > wlim

plt.subplot(6,1,1) 
plt.ion()
plt.plot(vis1wave[iwlim],vis1data[iwlim],'-k')
#plt.plot([0,15000],[0.0000000000004,0.0000000000004],'-r')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('VIS 1')
plt.show()

plt.subplot(6,1,2) 
plt.ion()
plt.plot(vis1wave[iwlim],vis2data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('VIS 2')
plt.show()

plt.subplot(6,1,3) 
plt.ion()
plt.plot(vis1wave[iwlim],vis3data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('VIS 3')
plt.show()

plt.subplot(6,1,4) 
plt.ion()
plt.plot(vis1wave[iwlim],vis4data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('VIS 4')
plt.show()

plt.subplot(6,1,5) 
plt.ion()
plt.plot(vis1wave[iwlim],vis5data[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('VIS 5')
plt.show()

svisdata = vis1data+vis2data+vis3data+vis4data+vis5data

plt.subplot(6,1,6) 
plt.ion()
plt.plot(vis1wave[iwlim],svisdata[iwlim],'-k')
plt.xlabel('pixel',fontsize=7)
plt.ylabel('calibrated flux',fontsize=fntsz)
plt.title('VIS Stacked')

plt.savefig('Figures/HV2112_stacking_VIS.pdf')
plt.show()

data = Table([vis1wave[iwlim]*10,svisdata[iwlim]], names=['wave', 'cflux'])
ascii.write(data, 'Tables/HV2112_stacked_VIS.dat')
