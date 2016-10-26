#!/bin/bash

BEGIN=1
END=3

case $1 in

    build)
        cd exp001
        ./build.bash
        cd ..

        for ii in `seq -f "%03g" $(($BEGIN+1)) $END`
        do 
            cp exp001/oceanM exp$ii/
        done
        ;;

    run)
        for ii in `seq -f "%03g" $BEGIN $END`
        do 
            cd exp$ii
            eval `grep NSLOTS= run_sge.sh`
            qsub -N exp$ii -pe mpi $NSLOTS run_sge.sh
            cd ..
        done
        ;;

    clean)
        for ii in `seq -f "%03g" $BEGIN $END`
        do 
            cd  exp$ii
            rm -r Build oceanM
            cd ..
        done
        ;;

    *)
        echo "Usage: mmake build|run|clean"
        ;;
esac
