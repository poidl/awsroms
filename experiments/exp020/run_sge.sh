#!/bin/bash
#
#$ -cwd
#$ -j y
#$ -S /bin/bash
#

mkdir -p nc/out

MPI_DIR=/usr/lib64/openmpi
NSLOTS=8
MACHINEFILE=machinefile

$MPI_DIR/bin/mpirun -np $NSLOTS oceanM ocean_benchmark2.in
        