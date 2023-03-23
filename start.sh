#!/bin/bash

folder1=Tables_Prodigal

folder2=_1_Total_number_of_genes_in_groups
folder3=_2_Quantifiably_changing_groups
folder4=_3_Genes_subsets_in_quantifiably_changing_groups

if [! -d {pwd}/${folder2}]; then
	python3 ADT_1.py ${folder1}
else
	echo 'Папка ${folder2} уже существует. Пропуск'
fi

if [! -d {pwd}/${folder3}]; then
	python3 ADT_2.py ${folder2} ${folder1}
else
	echo 'Папка ${folder3} уже существует. Пропуск'
fi

if [! -d {pwd}/${folder4}]; then
	python3 ADT_3.py ${folder3} ${folder1}
else
	echo 'Папка ${folder3} уже существует. Пропуск'
fi

python3 ADT_4.py ${folder4} ${folder1}
