#! /usr/bin/python3
# третья часть для исследования результатов работы EggNOG

import pandas as pd
import os
import openpyxl
from pathlib import Path

# НАЧАЛО
path_3 = '/media/lab330/Новый том/EggNOG/Tables_2_Quantifiably_changing_groups' # таблицы подсчёта количеств белков
path_4 = '/media/lab330/Новый том/EggNOG/Tables' # таблица с аннотацией генома
path_up = Path(path_4).parent # исходная директория

popular_genes_list = os.listdir(path_3)
organism_list = os.listdir(path_4)

path_output = os.path.join(path_up, 'Tables_3_Genes_subsets_in_quantifiably_changing_groups')
if not os.path.isdir(path_output):
    os.mkdir(path_output) # создание папки с выходящими файлами

for i in organism_list:
    i_name = i.replace('.xlsx', '')
    path_i = os.path.join(path_4, i)
    org = pd.ExcelFile(path_i)
    organism = org.parse('Sheet1')

    for j in popular_genes_list:
        j_name = j.replace('.csv', '').replace('all_', '').replace("arctic_", '') # получение имени базы данных для анализа
        path_j = os.path.join(path_3, j)
        genes = pd.read_csv(path_j)
        control = genes.dropna()
        if control["Unnamed: 0"].empty == True:
            print("База", j, "не содержит данных для анализа")
            pass
        else:
            print('Анализирую', i_name, j_name)
            print(j)
            organism_local = organism.loc[organism[j_name].isin(genes['Unnamed: 0'])]
            subset = organism_local[organism_local['query'].str.contains('##') == False]
        if 'arctic_' in j:
            output = os.path.join(path_output, i_name+'_'+j_name+"_arctic_genes.xlsx")
            subset.to_excel(output)
            print("записан файл", output)
        if 'all_' in j:
            output = os.path.join(path_output, i_name+'_'+j_name+"_all_genes.xlsx")
            subset.to_excel(output)
            print("записан файл", output)