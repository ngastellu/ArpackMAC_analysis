#!/usr/bin/env python

from glob import glob
import numpy as np
import matplotlib.pyplot as plt
from qcnico.plt_utils import multiple_histograms



print('Concatenating non zero Gaussian hvals...')
gaussian_hvals = np.hstack([np.load(f) for f in glob('/Users/nico/Desktop/simulation_outputs/semicircle_test/gaussian_hvals/*npy')])


print('Concatenating non zero tb hvals...')
tb_hvals = np.hstack([np.load(f) for f in glob('/Users/nico/Desktop/simulation_outputs/semicircle_test/dense_tb_hvals/*npy')])
print('Done!')

# gaussian_hamiltonians = [np.load(f).flatten() for f in glob('/Users/nico/Desktop/simulation_outputs/semicircle_test/gaussian_hvals/*npy')]
gaussian_eigvals = np.hstack([np.load(f) for f in glob('/Users/nico/Desktop/simulation_outputs/semicircle_test/gaussian_eigvals/*npy')])

# tb_hamiltonians = [np.load(f) for f in glob('/Users/nico/Desktop/simulation_outputs/semicircle_test/dense_tb_hamiltonians/*npy')]
tb_eigvals = np.hstack([np.load(f) for f in glob('/Users/nico/Desktop/simulation_outputs/semicircle_test/dense_tb_eigvals/*npy')])

norm_hvals = np.hstack([np.load(f) for f in glob('/Users/nico/Desktop/simulation_outputs/semicircle_test/nstd_gaussian_hvals/*npy')])
norm_eigvals = np.hstack([np.load(f) for f in glob('/Users/nico/Desktop/simulation_outputs/semicircle_test/nstd_gaussian_eigvals/*npy')])

# tb_hvals = np.hstack(h[h.nonzero()].flatten() for h in tb_hamiltonians)
# del tb_hamiltonians

# gaussian_hvals = np.hstack(h[h.nonzero()] for h in gaussian_hamiltonians)
# del gaussian_hamiltonians

# multiple_histograms((gaussian_hvals, tb_hvals, norm_hvals),('$\mathcal{N}(\mu_{\\text{TB}}=-2.34, \sigma_{\\text{TB}}=0.136)$', 'Tight-binding', '$\mathcal{N}(0,1)$'),nbins=1000,xlabel='$H_{ij}$ [eV]', density=True, alpha=0.7)
# multiple_histograms((gaussian_eigvals, tb_eigvals, norm_eigvals),('$\mathcal{N}(\mu_{\\text{TB}}=-2.34, \sigma_{\\text{TB}}=0.136)$', 'Tight-binding', '$\mathcal{N}(0,1)$'),nbins=1000,xlabel='$E$ [eV]', density=True, alpha=0.7)
fig, ax = multiple_histograms((gaussian_eigvals, tb_eigvals), 
                              ('$\mathcal{N}(\mu_{\\text{TB}}=-2.34, \sigma_{\\text{TB}}=0.136)$', 'Tight-binding'),
                              nbins=1000,
                              xlabel='$E$ [eV]',
                              ylabel='Spectral density $\\rho(E)$', 
                              density=True,
                              alpha=0.5,
                              show=False)
ax.set_title('Comparing TB DOS with DOS of sparse matrix with $H_{ij}\sim\mathcal{N}(\mu_{\\text{TB}},\sigma_{\\text{TB}})$')
plt.legend()
plt.show()