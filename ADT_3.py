#! /usr/bin/python3
# третья часть для исследования результатов работы EggNOG

import pandas as pd
import os
import openpyxl
import sys
from pathlib import Path

# НАЧАЛО
path_3 = os.path.join(os.getcwd(), sys.argv[2]+sys.argv[1]) # таблицы подсчёта количеств белков
path_4 = os.path.join(os.getcwd(), sys.argv[2]) # таблица с аннотацией генома
path_up = Path(path_4).parent # исходная директория

popular_genes_list = os.listdir(path_3)
organism_list = os.listdir(path_4)

path_output = os.path.join(path_up, sys.argv[2]+'_3_Genes_subsets_of_quantifiably_changing_groups')
if not os.path.isdir(path_output):
    os.mkdir(path_output) # создание папки с выходящими файлами

for i in organism_list:
    i_name = i.replace('.xlsx', '')
    path_i = os.path.join(path_4, i)
    org = pd.ExcelFile(path_i)
    organism = org.parse('Sheet1')
    n=0
    m=0

    for j in popular_genes_list:
        j_name = j.replace('.csv', '').replace('all_', '').replace("arctic_", '') # получение имени базы данных для анализа
        path_j = os.path.join(path_3, j)
        genes = pd.read_csv(path_j)
        if i_name in genes.columns:
            control = genes.dropna()
            if control["Unnamed: 0"].empty == True:
                print("\t База", j, "не содержит данных для анализа", i_name)
            if control["Unnamed: 0"].empty == False:
                print('Анализирую', i_name, j_name)
                organism_local = organism.loc[organism[j_name].isin(genes['Unnamed: 0'])]
                subset = organism_local[organism_local['query'].str.contains('##') == False]
                if 'arctic_' in j:
                    output = os.path.join(path_output, i_name+'_'+j_name+"_arctic_genes.xlsx")
                    subset.to_excel(output)
                if 'all_' in j:
                    output = os.path.join(path_output, i_name+'_'+j_name+"_all_genes.xlsx")
                    subset.to_excel(output)
