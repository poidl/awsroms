#!/bin/python
# pylint: disable=C0103

"""Plot elapsed CPU time"""

import os as os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# START = 1
# STOP = 6
# FIGNO = 1
# FIGNAME = '../doc/figures/met_t2micro.svg'
# infile = "ocean_benchmark1.in"
# ylim = (40, 180)

# START = 7
# STOP = 12
# FIGNO = 2
# FIGNAME = '../doc/figures/met_c4large.svg'
# infile = "ocean_benchmark1.in"
# ylim = (40, 180)

# START = 13
# STOP = 27
# FIGNO = 3
# FIGNAME = '../doc/figures/met_c44xlarge.svg'
# infile = "ocean_benchmark2.in"
# ylim = (0, 2000)

START = 28
STOP = 33
FIGNO = 4
FIGNAME = '../doc/figures/met_c48xlarge.svg'
infile = "ocean_benchmark3.in"
ylim = (0, 300)

# mean elapsed time
met = np.zeros(STOP - START + 1)
# number of procs
nproc = np.zeros(STOP - START + 1, dtype=int)
ntilei = np.zeros(STOP - START + 1, dtype=int)
ntilej = np.zeros(STOP - START + 1, dtype=int)


def readarray(fname):
    """Read newline separated values from file into numpy array"""
    file = open(fname, 'r')
    n = file.read()
    return np.fromstring(n, sep='\n')

jj = 0
for ii in range(START, STOP + 1):
    jj += 1
    cmdstr = ('grep "NtileI =" ../experiments/exp%03d/' + infile + ' |'
              'awk \'{print $3}\' >./.tmp')
    os.system(cmdstr % (ii))
    ntilei[jj - 1] = readarray('.tmp')
    cmdstr = ('grep "NtileJ =" ../experiments/exp%03d/' + infile + ' |'
              'awk \'{print $3}\' >./.tmp')
    os.system(cmdstr % (ii))
    ntilej[jj - 1] = readarray('.tmp')

    cmdstr = '''grep "Node   #" ../experiments/exp%03d/out/exp%03d.o* |awk \'{print $NF}\' >./.tmp'''
    # print(cmdstr % (ii, ii))
    os.system(cmdstr % (ii, ii))
    a = readarray('.tmp')
    met[jj - 1] = np.mean(a)
    nproc[jj - 1] = a.size


myx = 'x' * (STOP - START + 1)
z = list(zip(ntilei, myx, ntilej))
labels = [''.join(str(x) for x in z[jj]) for jj in range(STOP - START + 1)]
print(labels)

# where plot ideal lines?
pideal = np.diff(nproc) != 0
if pideal[0]:
    pideal = np.insert(pideal, 0, True)
else:
    pideal = np.insert(pideal, 0, False)
ideal = met / (nproc / nproc)


fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111)
for i, j in zip(nproc, met):
    plt.loglog(i, j, 'x',  markersize=15, markeredgewidth=3, basex=2, basey=2)


# ax.loglog(nproc, ideal, basex=2, basey=2)
ax.legend(labels, numpoints=1, fontsize=10)

for i in range(len(nproc)):
    if pideal[i]:
        ax.loglog(nproc, met[i] / (nproc / nproc[i]),
                  basex=2, basey=2, linestyle='dashed', color='black')

ax.text(-0.12, 1.02, str(FIGNO) + ')', fontsize=15, transform=ax.transAxes)
plt.xticks(nproc)
plt.xlim(np.min(nproc) - 0.2, np.max(nproc) + 5)
plt.ylim(ylim)
ax.xaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.yaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
plt.xlabel('Number of processes')
plt.ylabel('Mean elapsed "CPU time" (s)')
plt.grid()
fig.savefig(FIGNAME)
