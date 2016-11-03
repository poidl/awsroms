#!/bin/python
# pylint: disable=C0103

"""Plot elapsed CPU time"""

import os as os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


START = 1
STOP = 6
figname = 'figures/met_t2micro.png'

# START = 7
# STOP = 12
# figname = 'figures/met_c4large.png'

# mean elapsed time
met = np.zeros(STOP-START+1)
# number of vcpus
nvcpu = np.zeros(STOP-START+1, dtype=int)
ntilei = np.zeros(STOP-START+1, dtype=int)
ntilej = np.zeros(STOP-START+1, dtype=int)

def readarray(fname):
    """Read newline separated values from file into numpy array"""
    file = open(fname, 'r')
    n = file.read()
    return np.fromstring(n, sep='\n')

jj = 0
for ii in range(START, STOP+1):
    jj += 1
    cmdstr = ('grep "NtileI =" ../experiments/exp%03d/ocean_benchmark1.in |'
              'awk \'{print $3}\' >./.tmp')
    os.system(cmdstr % (ii))
    ntilei[jj-1] = readarray('.tmp')
    cmdstr = ('grep "NtileJ =" ../experiments/exp%03d/ocean_benchmark1.in |'
              'awk \'{print $3}\' >./.tmp')
    os.system(cmdstr % (ii))
    ntilej[jj-1] = readarray('.tmp')

    cmdstr = '''grep "Node   #" ../experiments/exp%03d/out/exp%03d.o* |awk \'{print $5}\' >./.tmp'''
    # print(cmdstr % (ii, ii))
    os.system(cmdstr % (ii, ii))
    a = readarray('.tmp')
    met[jj-1] = np.mean(a)
    nvcpu[jj-1] = a.size


myx = 'x'*(STOP-START+1)
z = list(zip(ntilei, myx, ntilej))
labels = [''.join(str(x) for x in z[jj]) for jj in range(STOP-START+1)]
print(labels)

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111)
ax.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%d'))
# ax.plot(nvcpu, met)
for i, j in zip(nvcpu, met):
    ax.plot(i, j, 'x', markersize=15, markeredgewidth=3)
ax.legend(labels, numpoints=1)
ax.text(-0.12, 1.02, '1)', fontsize=15, transform=ax.transAxes)
plt.xticks(nvcpu)
plt.xlim(np.min(nvcpu)-0.5, np.max(nvcpu)+0.5)
plt.ylim(40, 180)
plt.xlabel('Number of vCPUs')
plt.ylabel('Mean elapsed CPU time (s)')
plt.grid()
fig.savefig(figname)
