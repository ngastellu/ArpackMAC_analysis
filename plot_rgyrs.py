#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from qcnico.plt_utils import histogram, setup_tex, get_cm
from os import path



percdir = path.expanduser('~/Desktop/simulation_outputs/percolation/')
datadirs = ['40x40/', 'Ata_structures/tempdot6/', 'Ata_structures/tempdot5/']

ringsdir = path.expanduser('~/Desktop/simulation_outputs/ring_stats_40x40_pCNN_MAC/')
rings_files = ['avg_ring_counts_normalised.npy', 'avg_ring_counts_tempdot6_new_model_relaxed.npy', 'avg_ring_counts_tempdot5_new_model_relaxed.npy']

ringdats = [np.load(ringsdir+f) for f in rings_files]
ringdats[1] = ringdats[1] / ringdats[1].sum()
ringdats[2] = ringdats[2] / ringdats[2].sum()


p6cs = [r[4] for r in ringdats]
p6cs.extend([0,1])

clrs = get_cm(p6cs,cmap_str='inferno')

labels = ['PixelCNN', '$\\tilde{T} = 0.6$', '$\\tilde{T} = 0.5$']

setup_tex()
fig, ax = plt.subplots()

for d, c, l in zip(datadirs,clrs,labels):
    rgyrs = np.hstack([np.load(f) for f in glob(percdir+d+'rgyrs/*npy')])
    fig, ax = histogram(rgyrs,nbins=100,plt_objs=(fig,ax),show=False,xlabel='$R_g$ [\AA]', kwargs={'alpha':0.6, 'color':c, 'label':l},density=True)

plt.show()