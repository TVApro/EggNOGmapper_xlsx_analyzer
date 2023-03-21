#! /usr/bin/python3
# третья часть для исследования результатов работы EggNOG

import pandas as pd
import os
import openpyxl
from pathlib import Path

# НАЧАЛО
path_3 = '/home/trubitsyns/Рабочий стол/Кандидатская работа/Tables_3+_Genes_subsets_in_quantifiably_changing_groups' # таблицы подсчёта количеств белков
path_4 = '/home/trubitsyns/Рабочий стол/Кандидатская работа/Tables' # таблица с аннотацией генома
path_up = Path(path_4).parent # исходная директория

genes_of_organism_list = os.listdir(path_3)
organism_list = os.listdir(path_4)

path_output = os.path.join(path_up, 'Tables_4+_I_dont_know_for_what_it_is')
if not os.path.isdir(path_output):
    os.mkdir(path_output) # создание папки с выходящими файлами

for i in organism_list:
    i_name = i.replace('.xlsx', '')
    path_i = os.path.join(path_4, i)
    org = pd.ExcelFile(path_i)
    organism = org.parse('Sheet1')
    n = 0
    m = 0
    for j in genes_of_organism_list:
        j_name = j.replace(i_name, '').replace('genes.xlsx', '').replace('arctic', '').replace('all', '').replace('_', '')
        path_j = os.path.join(path_3, j)
        db_genes = pd.ExcelFile(path_j)
        genes_1 = db_genes.parse('Sheet1')
        genes = genes_1.drop(genes_1.columns[0], axis=1)
        if '_arctic_' in j:
            if i_name in j:
                print('Соединяю', i_name, j_name)   
                n += 1
                if n == 1:
                    subset_X = genes
                if n > 1:
                    subset_X = pd.merge(subset_X, genes, how = 'outer')
        if '_all_' in j:
            if i_name in j:
                print('Соединяю', i_name, j_name)
                print(j)
                m += 1
                if m == 1:
                    subset_Y = genes
                if m > 1:
                    subset_Y = pd.merge(subset_Y, genes, how = 'outer')
    if n >= 1:
        output_1 = os.path.join(path_output, i_name+"_arctic_genes.xlsx")
        subset_X.to_excel(output_1)
    
    if m >= 1:
        output_2 = os.path.join(path_output, i_name+"_all_genes.xlsx")
        subset_Y.to_excel(output_2)
print("Бессмысленная работа закончена")
