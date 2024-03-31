#!/usr/bin/env python

from glob import glob
import numpy as np
import matplotlib.pyplot as plt
from qcnico.plt_utils import multiple_histograms





print('Concatenating non zero tb hvals...')
eigvals10x10 = np.hstack([np.load(f) for f in glob('/Users/nico/Desktop/simulation_outputs/semicircle_test/10x10/dense_tb_eigvals/*npy')])
eigvals20x20 = np.hstack([np.load(f) for f in glob('/Users/nico/Desktop/simulation_outputs/semicircle_test/20x20/dense_tb_eigvals/*npy')])
print('Done!')

# gaussian_hamiltonians = [np.load(f).flatten() for f in glob('/Users/nico/Desktop/simulation_outputs/semicircle_test/gaussian_hvals/*npy')]
fig, ax = multiple_histograms((eigvals10x10, eigvals20x20), 
                              ('$10\\text{nm}\\times10\\text{nm}$ ($N\\approx3500\,$atoms)', '$20\\text{nm}\\times20\\text{nm}$ ($N\\approx14500\,$atoms)'),
                              nbins=1000,
                              xlabel='$E$ [eV]',
                              ylabel='Spectral density $\\rho(E)$', 
                              density=True,
                              alpha=0.5,
                              show=False)
ax.set_title('TB DOS for systems of different sizes')
plt.legend()
plt.show()