#!/bin/bash

BEGIN=7
END=7

EXPPATH=./experiments

case $1 in

    build)
        cd $EXPPATH/exp001
        ./build.bash
        cd ..

        for ii in `seq -f "%03g" $(($BEGIN+1)) $END`
        do 
            cp $EXPPATH/exp001/oceanM $EXPPATH/exp$ii/
        done
        ;;

    run)
        if [ $# -ne 2 ]; then
          echo "Usage: mmake run NSLOTS"
          exit 1
        fi
        for ii in `seq -f "%03g" $BEGIN $END`
        do 
            cd $EXPPATH/exp$ii
            qsub -N exp$ii -pe mpi $2 run_sge.sh
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
