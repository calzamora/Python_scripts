#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH -c 8

conda activate bgmp_star

/usr/bin/time -v STAR --runThreadN 8 --runMode alignReads \
    --outFilterMultimapNmax 3 \
    --outSAMunmapped Within KeepPairs \
    --alignIntronMax 1000000 --alignMatesGapMax 1000000 \
    --readFilesCommand zcat \
    --readFilesIn /projects/bgmp/shared/Bi621/dre_WT_ovar12_R1.qtrim.fq.gz /projects/bgmp/shared/Bi621/dre_WT_ovar12_R2.qtrim.fq.gz\
    --genomeDir /projects/bgmp/calz/bioinfo/Bi621/PS/ps8-calzamora/Danio_rerio.GRCz11.dna.ens112.STAR_2.7.11b \
    --outFileNamePrefix Danio_rerio