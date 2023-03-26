# EggNOGmapper_xlsx_analyzer
Extracting data from an Excel output files of EggNog-mapper v.2.0

## Requirements

Python3 (modules pandas, openpxl, pathlib)

bash (Linux OS)

Prodigal (not required, if you previously annotate whole genomes on eggNog_mapper with option "Prodigal")

## Steps for analysis

1. Obtain .faa files fron the genomes FASTA (I strongly recommend Prodigal for this)

2. Load each .faa file into eggNog_mapper (http://eggnog-mapper.embl.de/), get Excel files as the output

3. Remove the top two "technical" lines from each table

4. Put all tables in one folder (as in the example "Tables..." folders)

5. Run the whole program (for Linux - "start.sh")

6. You may use any IDE for using any part of programm

## Program files

ADT_1 - Counts the number of annotations of each type for each specified database

ADT_2 - Calculates those groups of annotations, the change in the number of which satisfies the conditions (the conditions are written in the file, they can be changed by indicating the names of the corresponding genomes without ".xlsx" and the required ratio)

ADT_3 - Finds genes corresponding to the selected groups from the previous program, and writes out each group of genes for each organism separately

ADT_4 - Consolidates all genes from the output of the previous program into one file

Faa_control.py - a small piece of code for pairwise comparison of FAA file sizes

single_group_analyzer.py - the first version of the program, able to search for the genes of one specific group (by default - COG). Don't finished yet

/PRODIGAL/prodigal__all.sh - a small script for annotating a large number of genomes using Prodigal

start.sh - script that runs the program in the sequence ADT_1, ADT_2, ADT_3, ADT_4


