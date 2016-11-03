#!/bin/bash

BEGIN=7
END=12

EXPPATH=./experiments

case $1 in

    build)
        cd $EXPPATH/exp007
        ./build.bash
        cd ..

        for ii in `seq -f "%03g" $(($BEGIN+1)) $END`
        do 
            cp $EXPPATH/exp007/oceanM $EXPPATH/exp$ii/
        done
        ;;

    run)
        for ii in `seq -f "%03g" $BEGIN $END`
        do 
            cd $EXPPATH/exp$ii
            eval `grep NSLOTS= run_sge.sh`
            qsub -N $EXPPATH/exp$ii -pe mpi $NSLOTS run_sge.sh
            cd ..
        done
        ;;

    clean)
        for ii in `seq -f "%03g" $BEGIN $END`
        do 
            cd  $EXPPATH/exp$ii
            rm -r Build oceanM
            cd ..
        done
        ;;

    *)
        echo "Usage: mmake build|run|clean"
        ;;
esac
