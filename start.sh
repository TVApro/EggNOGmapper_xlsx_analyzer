#!/bin/bash

folder1=Tables_Prodigal

folder2=_1_Total_number_of_genes_in_groups
folder3=_2_Quantifiably_changing_groups
python3 ADT_1.py ${folder1} && \
python3 ADT_2.py ${folder2} ${folder1} && \
python3 ADT_3.py ${folder3} ${folder1}
