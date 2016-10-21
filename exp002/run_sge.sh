#!/bin/bash
#
#$ -cwd
#$ -j y
#$ -S /bin/bash
#

MPI_DIR=/usr/lib64/openmpi
NSLOTS=2
MACHINEFILE=machinefile

$MPI_DIR/bin/mpirun -np $NSLOTS oceanM ocean_upwelling.in
        