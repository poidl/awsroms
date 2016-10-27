#!/bin/python
# pylint: disable=C0103

"""Plot elapsed CPU time"""

import os as os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

START = 1
STOP = 4

# mean elapsed time
met = np.zeros(STOP-START)
# number of processors/cores
nproc = np.zeros(STOP-START, dtype=int)

for ii in range(START, STOP):
    os.system('grep "Node   #" ../exp%03d/run_sge.sh.* |awk \'{print $5}\' >./.tmp' % (ii))
    file = open('./.tmp', 'r')
    n = file.read()
    a = np.fromstring(n, sep='\n')
    met[ii-1] = np.mean(a)
    nproc[ii-1] = a.size
    print(n)
    print("")

fig = plt.figure()
ax = fig.add_subplot(111)
ax.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%d'))
ax.plot(nproc, met)
ax.plot(nproc, met, 'xb', markersize=15, markeredgewidth=3)
plt.xticks(nproc)
plt.xlabel('Number of cores')
plt.ylabel('Mean elapsed CPU time (s)')
fig.savefig('figures/met.png')
