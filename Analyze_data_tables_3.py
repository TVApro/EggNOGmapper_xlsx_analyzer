#! /usr/bin/python3
# третья часть для исследования результатов работы EggNOG

import pandas as pd
import os
from pathlib import Path

# НАЧАЛО
path_3 = '/media/lab330/Новый том/EggNOG/Tables_2_Quantifiably_changing_groups' # таблицы подсчёта количеств белков
path_4 = '/media/lab330/Новый том/EggNOG/Tables' # таблица с аннотацией генома
path_up = Path(path_4).parent # исходная директория

popular_genes_list = os.listdir(path_3)
organism_list = os.listdir(path_4)

path_output = os.path.join(path_up, 'Tables_3_Genes_of_quantifiably_changing_groups')
if not os.path.isdir(path_output):
    os.mkdir(path_output) # создание папки с выходящими файлами

for j in popular_genes_list:
    path_j = os.path.join(path_3, j)
    POP_genes = pd.read_csv(path_j)
    POP = POP_genes.dropna()
    if POP["Unnamed: 0"].empty == True:
        print("База", j, "не содержит данных для анализа")
        pass
    else:
        j_name = j.replace('.csv', '').replace('all_', '').replace("arctic_", '') # получение имени базы данных для анализа
        n=0
        m=0
        print("Начинаю поиск генов для", j)
        
        for i in organism_list:
            i_name = i.replace('.xlsx', '')
            try:
                if POP[i_name].empty == False:
                    path_i = os.path.join(path_4, i)
                    path_arctic = os.path.join(path_output, 'arctic_'+i)
                    path_all = os.path.join(path_output, 'all_'+i)
                    org = pd.ExcelFile(path_i)
                    organism = org.parse('Sheet1')
                    
                    db_organism = organism.loc[organism[j_name].isin(POP['Unnamed: 0'])]
                    db_organism_2 = db_organism.value_counts('Description')
                    db_organism_3 = db_organism_2.to_frame() # переводит объект Series в DataFrame
                    db_organism_3.reset_index(inplace = True) # при сравнении он считал, что Description - индекс, это мешало работе
                    db_organism_3.columns = ['Description', i_name] # назначает именем столбца имя генома
                    db_organism_sub = pd.DataFrame()
                    db_organism_sub[j_name] = db_organism[j_name]
                    db_organism_sub['Description'] = db_organism['Description']
                    db_category = pd.merge(db_organism_sub, db_organism_3, how = 'right')
                    db = db_category.drop_duplicates(subset='Description')
                    if 'arctic_' in j:
                        n += 1
                        if n == 1:
                            db_arctic = db
                        if n > 1:
                            db_arctic = pd.merge(db_arctic, db, how='outer')
                    if 'all_' in j:
                        m += 1
                        if m == 1:
                            db_all = db
                        if m > 1:
                            db_all = pd.merge(db_all, db, how='outer')
            except:
                pass

    output = os.path.join(path_output, "genes_"+j)
    if POP["Unnamed: 0"].empty == False:
        if 'arctic_' in j:
            db_arctic.to_csv(output)
            db_arctic = pd.DataFrame()
        if 'all_' in j:
            db_all.to_csv(output)
            db_all = pd.DataFrame()