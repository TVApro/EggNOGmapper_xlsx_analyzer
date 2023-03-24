#!/bin/bash
path=$(pwd)
folder1=Tables_Prodigal
folder2=_1_Total_number_of_genes_in_groups
folder3=_2_Quantifiably_changing_groups
folder4=_3_Genes_subsets_in_quantifiably_changing_groups

if [ ! -d "${path}"/$folder1${folder2} ]; then
	echo Выполняется скрипт 1
	python3 ADT_1.py ${folder1}
else 
	echo Папка ${folder1}${folder2} уже существует. Пропуск
fi
echo -n '////////'

if [ ! -d "${path}"/${folder1}${folder3} ]; then
	echo Выполняется скрипт 2
	python3 ADT_2.py ${folder2} ${folder1}
else
	echo Папка ${folder1}${folder3} уже существует. Пропуск
fi
echo -n '////////'

if [ ! -d "${path}"/${folder1}${folder4} ]; then
	python3 ADT_3.py ${folder3} ${folder1}
else
	echo Папка ${folder1}${folder3} уже существует. Пропуск
fi

echo end!
