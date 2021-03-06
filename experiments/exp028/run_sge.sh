#!/bin/bash
#
#$ -cwd
#$ -j y
#$ -S /bin/bash
#

mkdir -p nc/out

MPI_DIR=/usr/lib64/openmpi
NSLOTS=32
MACHINEFILE=machinefile

$MPI_DIR/bin/mpirun -np $NSLOTS oceanM ocean_benchmark3.in
        