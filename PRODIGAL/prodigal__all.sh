#!/bin/bash
cd /media/lab330/Новый\ том/EggNOG/genomes/fasta
find . -type f -exec sh -c 'prodigal -i "$0" -a "$0.faa"' {} \;
echo 'Закончено'
