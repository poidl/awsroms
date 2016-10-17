#!/bin/bash
#
#$ -cwd
#$ -j y
#$ -S /bin/bash
#

MPI_DIR=/usr/lib64/openmpi
MYBIN=./oceanM

$MPI_DIR/bin/mpirun -np $NSLOTS -machinefile $TMP/machines $MYBIN
        