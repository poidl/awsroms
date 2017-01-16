# ROMS benchmarks

ROMS provides 3 "ocean_benchmark{1,2,3}.in" files, differing only in horizontal
domain size.

* benchmark1:  
Lm == 512           ! Number of I-direction INTERIOR RHO-points  
Mm == 64            ! Number of J-direction INTERIOR RHO-points

* benchmark2:  
Lm == 1024  
Mm == 128  

* benchmark3:  
Lm == 2048  
Mm == 256  

# The following are "benchmark1.in" runs on t2.micro. They differ only in number of cores and tiling.

exp001: 1x1  
exp002: 1x2  
exp003: 2x1  
exp004: 2x2  
exp005: 1x4  
exp006: 4x1  

# "benchmark1.in" runs on c4.large

exp007: 1x1  
exp008: 1x2  
exp009: 2x1  
exp010: 2x2  
exp011: 1x4  
exp012: 4x1  

# "benchmark2.in" runs on c4.4xlarge

exp013: 1x1  
exp014: 1x2  
exp015: 2x1  
exp016: 2x2  
exp017: 1x4  
exp018: 4x1  
exp019: 2x4  
exp020: 4x2  
exp021: 1x8  
exp022: 8x1  
exp023: 4x4  
exp024: 2x8  
exp025: 8x2  
exp026: 1x16  
exp027: 16x1  

```bash
ntilei=(1 1 2 2 1 4 2 4 1 8 4 2 8 1 16)  
ntilej=(1 2 1 2 4 1 4 2 8 1 4 8 2 16 1)
slots=(1 2 2 4 4 4 8 8 8 8 16 16 16 16 16)  
dirs=$(seq -f "%03g" 13 27)

for i in $dirs; do cp -r experiments/exp001 experiments/exp$i; done

for i in $dirs; do cp ../roms/ROMS/External/ocean_benchmark2.in experiments/exp$i/; done

for i in $dirs; do sed -i  s/benchmark1\.in/benchmark2\.in/g  experiments/exp$i/run_sge.sh; done

dirs_array=($dirs)

for i in "${!slots[@]}"; do sed -i s/SLOTS=.*/SLOTS="${slots[$i]}"/g  experiments/exp${dirs_array[$i]}/run_sge.sh; done

for i in "${!ntilei[@]}"; do sed -i s/"NtileI == .*"/"NtileI == ${ntilei[$i]}"/g  experiments/exp${dirs_array[$i]}/ocean_benchmark2.in; done  
for i in "${!ntilei[@]}"; do sed -i s/"NtileJ == .*"/"NtileJ == ${ntilej[$i]}"/g  experiments/exp${dirs_array[$i]}/ocean_benchmark2.in; done

for i in $dirs; do sed -i s/"VARNAME = .*"/"VARNAME = \.\.\/\.\.\/\.\.\/roms\/ROMS\/External\/varinfo.dat"/g experiments/exp$i/ocean_benchmark2.in; done
```

# "benchmark3.in" runs on c4.8xlarge

exp028: 16x2 = 32
exp029: 32x2 = 64 
exp030: 16x4 = 64
exp031: 32x4 = 128
exp032: 32x8 = 256
exp033: 32x16 = 512

```bash
ntilei=(16 32 16 32 32 32)  
ntilej=(2 2 4 4 8 16)
slots=(32 64 64 128 256 512)  
dirs=$(seq -f "%03g" 28 33)

for i in $dirs; do cp -r experiments/exp001 experiments/exp$i; done

for i in $dirs; do cp ../roms/ROMS/External/ocean_benchmark3.in experiments/exp$i/; done

for i in $dirs; do sed -i  s/benchmark1\.in/benchmark3\.in/g  experiments/exp$i/run_sge.sh; done

dirs_array=($dirs)

for i in "${!slots[@]}"; do sed -i s/SLOTS=.*/SLOTS="${slots[$i]}"/g  experiments/exp${dirs_array[$i]}/run_sge.sh; done

for i in "${!ntilei[@]}"; do sed -i s/"NtileI == .*"/"NtileI == ${ntilei[$i]}"/g  experiments/exp${dirs_array[$i]}/ocean_benchmark3.in; done  
for i in "${!ntilei[@]}"; do sed -i s/"NtileJ == .*"/"NtileJ == ${ntilej[$i]}"/g  experiments/exp${dirs_array[$i]}/ocean_benchmark3.in; done
for i in $dirs; do sed -i s/"VARNAME = .*"/"VARNAME = \.\.\/\.\.\/\.\.\/roms\/ROMS\/External\/varinfo.dat"/g experiments/exp$i/ocean_benchmark3.in; done
```
