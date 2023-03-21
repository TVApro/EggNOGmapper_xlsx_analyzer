#! /usr/bin/python3
# третья часть для исследования результатов работы EggNOG

import pandas as pd
import os
import openpyxl
from pathlib import Path

# НАЧАЛО
path_3 = '/media/lab330/Новый том/EggNOG/Tables_3_Genes_subsets_in_quantifiably_changing_groups' # таблицы подсчёта количеств белков
path_4 = '/media/lab330/Новый том/EggNOG/Tables' # таблица с аннотацией генома
path_up = Path(path_4).parent # исходная директория

genes_of_organism_list = os.listdir(path_3)
organism_list = os.listdir(path_4)

path_output = os.path.join(path_up, 'Tables_4_I_dont_know_for_what_it_is')
if not os.path.isdir(path_output):
    os.mkdir(path_output) # создание папки с выходящими файлами

for i in organism_list:
    i_name = i.replace('.xlsx', '')
    path_i = os.path.join(path_4, i)
    org = pd.ExcelFile(path_i)
    organism = org.parse('Sheet1')
    n = 0
    for j in genes_of_organism_list:
        if i_name in j:
            j_name = j.replace(i_name, '').replace('genes.xlsx', '').replace('arctic', '').replace('all', '').replace('_', '')
            print('Соединяю', i_name, j_name)
            path_j = os.path.join(path_3, j)
            db_genes = pd.ExcelFile(path_j)
            genes_1 = db_genes.parse('Sheet1')
            genes = genes_1.drop(genes_1.columns[0], axis=1)
            if n == 1:
                subset = genes
            if n > 1:
                subset = pd.merge(subset, genes, how = 'outer')
    if 'arctic_' in j:
        output = os.path.join(path_output, i_name+'_'+j_name+"_arctic_genes.xlsx")
        subset.to_excel(output)
    if 'all_' in j:
        output = os.path.join(path_output, i_name+'_'+j_name+"_all_genes.xlsx")
        subset.to_excel(output)