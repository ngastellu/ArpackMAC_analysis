#!/usr/bin/env python

import numpy as np
from glob import glob
import matplotlib.pyplot as plt
from qcnico.plt_utils import histogram


eigvals = np.hstack([np.load(f) for f in glob('/Users/nico/Desktop/simulation_outputs/semicircle_test/gaussian_eigvals/*npy')])
# # hvals = np.hstack([np.load(f) for f in glob('/Users/nico/Desktop/simulation_outputs/semicircle_test/gaussian_hvals/*npy')])

# histogram(hvals,nbins=500)
histogram(eigvals,nbins=500)