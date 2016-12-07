## BUGS

* exp001-006 have wrong varinfo.dat path in *.in


## TODO

* T2 may be faster than C4 for a SHORT TIME due to "burstable performance". Pin that down in the experiments and interpretation.
* mkdir exp*/nc/out


## QUESTIONS

* So far sge works only with "qsub -pe mpi". "qconf -spl mpi" shows that "job_is_first_task TRUE" in the mpi parallel environment. Most instructions on the web (eg. https://www.open-mpi.org/faq/?category=sge) say have "job_is_first_task FALSE". What is the difference? According to the man page, I guess it should be FALSE, because the run_sge.sh script is not a task itself? Don't understand.