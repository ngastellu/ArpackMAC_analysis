#!/usr/bin/env python

from glob import glob
import numpy as np
import matplotlib.pyplot as plt
from qcnico.plt_utils import multiple_histograms, histogram



def semicircle(x,sigma=0.13658531,N=3600):
    J = np.sqrt(N) * sigma
    return np.sqrt(4*J*J - x*x)/(2*np.pi*J*J)


gaussian_eigvals = np.hstack([np.load(f) for f in glob('/Users/nico/Desktop/simulation_outputs/semicircle_test/gaussian_eigvals_dense/*npy')])

delta_bools = np.abs(gaussian_eigvals) > 100

print("Contribution to delta function peak for finite mean = ", np.sum(delta_bools))

norm_eigvals = np.hstack([np.load(f) for f in glob('/Users/nico/Desktop/simulation_outputs/semicircle_test/nstd_gaussian_eigvals_dense/*npy')])

# tb_hvals = np.hstack(h[h.nonzero()].flatten() for h in tb_hamiltonians)
# del tb_hamiltonians

# gaussian_hvals = np.hstack(h[h.nonzero()] for h in gaussian_hamiltonians)
# del gaussian_hamiltonians

multiple_histograms((gaussian_eigvals[~delta_bools], norm_eigvals),('$\mathcal{N}(\mu_{\\text{TB}}=-2.34, \sigma_{\\text{TB}}=0.136)$', '$\mathcal{N}(0,1)$'),nbins=1000,xlabel='$E$ [eV]', density=True, alpha=0.7)
fig, ax, x, _ = histogram(gaussian_eigvals[~delta_bools],nbins=1000,show=False,xlabel='Eigenvalue $\lambda$',ylabel='Spectral density $\\rho(\lambda)$',density=True, return_data=True)
ax.plot(x,semicircle(x),'k-',lw=2.0,label='Expected $\\rho(\lambda)$')
ax.set_title('Non-sparse matrices')
plt.legend()
plt.show()

# histogram(gaussian_eigvals[delta_bools],nbins=20)