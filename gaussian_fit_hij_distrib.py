#!/usr/bin/env python

from glob import glob
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from qcnico.plt_utils import histogram, setup_tex


def gaussian(x,mu,sigma):
    return np.exp(-((x-mu)**2)/(2*(sigma**2))) / (sigma * np.sqrt(2*np.pi))


# hvals_npys = glob('/Users/nico/Desktop/simulation_outputs/semicircle_test/dense_tb_hamiltonians/*npy')
# eigvals_npys = glob('/Users/nico/Desktop/simulation_outputs/semicircle_test/dense_tb_eigvals/*npy')

Hdir_40x40 = '/Users/nico/Desktop/simulation_outputs/percolation/40x40/Hao_ARPACK/hvals/'
hvals_40x40 = np.hstack([np.load(f) for f in glob(Hdir_40x40 + '*.npy')]) 

Hdir_10x10 = '/Users/nico/Desktop/simulation_outputs/percolation/10x10/Hao_ARPACK/hvals/'
hvals_10x10 = np.hstack([np.load(f) for f in glob(Hdir_10x10 + '*.npy')]) 


setup_tex()
fig, ax = plt.subplots()

fig, ax, centers_10x10, hist_10x10, dx_10x10 = histogram(hvals_10x10,nbins=1000,density=True,plt_objs=(fig,ax),return_data_w_dx=True,show=False,plt_kwargs={'alpha':0.7, 'color':'b'})
# centers_40x40, hist_40x40, dx_40x40 = histogram(hvals_40x40,nbins=1000,density=True,plt_objs=(fig,ax),return_data_w_dx=True,show=False,plt_kwargs={'alpha':0.5, 'color':'r','label':'$40\\times40$'})

print('10x10 integral = ', np.sum(hist_10x10*dx_10x10))
# print('40x40 integral = ', np.sum(hist_40x40*dx_40x40))

popt_10x10, pcov_10x10 = curve_fit(gaussian,centers_10x10,hist_10x10,p0=[-2.4,0.3])
# popt_40x40, pcov_40x40 = curve_fit(gaussian,centers_40x40,hist_40x40,p0=[-2.4,0.3])

mu10x10, sigma10x10 = popt_10x10
# mu40x40, sigma    40x40 = popt_40x40

y10x10 = gaussian(centers_10x10,mu10x10, sigma10x10)
# y40x40 = gaussian(centers_40x40,mu40x40, sigma40x40)


print('10x10 fit params: ', popt_10x10)
print('errors: ', pcov_10x10.diagonal())
# print('\n40x40 fit params: ', popt_40x40)
# print('errors: ', pcov_40x40.diagonal())

ax.plot(centers_10x10,y10x10,'-',color='r',lw=1.0,label='Fit')
# ax.plot(centers_40x40,y40x40,'r-',lw=0.8)
ax.set_title('Fitting tight-binding $H_{ij}$ distribution to $\mathcal{N}(\mu,\sigma)$')
plt.legend()
plt.show()