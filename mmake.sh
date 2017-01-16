#!/bin/bash

BEGIN=28
END=33

EXPPATH=./experiments

case $1 in

    build)
        # zero pad $BEGIN
        printf -v N "%03g" $BEGIN
        SINGLEBUILDPATH=$EXPPATH/exp$N
        cd $SINGLEBUILDPATH
        ./build.bash
        cd ../..
        for ii in `seq -f "%03g" $(($BEGIN+1)) $END`
        do 
            cp $SINGLEBUILDPATH/oceanM $EXPPATH/exp$ii/
        done
        ;;

    run)
        for ii in `seq -f "%03g" $BEGIN $END`
        do 
            cd $EXPPATH/exp$ii
            eval `grep NSLOTS= run_sge.sh`
            qsub -N exp$ii -pe mpi $NSLOTS run_sge.sh
            cd ../..
        done
        ;;

    clean)
        for ii in `seq -f "%03g" $BEGIN $END`
        do 
            cd  $EXPPATH/exp$ii
            rm -r Build oceanM
            cd ../..
        done
        ;;

    *)
        echo "Usage: mmake build|run|clean"
        ;;
esac
