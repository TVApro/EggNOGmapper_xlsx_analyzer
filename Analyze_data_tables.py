#! /usr/bin/python3
# для исследования результатов работы EggNOG

import pandas as pd
import os
import re
from pathlib import Path

def group(j, genome_name, df):
    try:
        j_df1 = df.loc[df[j] != '-'] # возвращает DataFrame, в котором исключены все пустые значения '-'
        j_df2 = j_df1[j].value_counts() # возвращает объект Series с группировкой по названиями
        j_df3 = j_df2.to_frame() # переводит объект Series в DataFrame
        j_df3.columns = [genome_name] # назначает именем столбца имя генома
    except:
        print(genome_name, "не содержит", j)
    return j_df3

def export(name, folder_path):
    export_name = name + '.csv'
    path_export = os.path.join(folder_path, export_name)
    if os.path.isfile(path_export):
        os.remove(path_export)
    df.to_csv(path_export)

#path = input("Укажите путь до папки с таблицами: ")
path = '/media/lab330/Новый том/EggNOG/Tables'
path_up = Path(path).parent

#description = input("Введите название столбца, по которому хотите осуществить поиск? Проверьте название заранее: ")
description = 'Description'

#COG_group = input("Введите название группы COG, в пределах которой хотите осуществить поиск: ")
COG_group = 'C'

results_list = os.listdir(path)
list_X = ['COG_category', 'GOs', 'EC', 'KEGG_ko', 'KEGG_Pathway', 'KEGG_Module', 'KEGG_Reaction', 'KEGG_rclass', 'BRITE', 'KEGG_TC', 'CAZy', 'BiGG_Reaction', 'PFAMs']
for db in list_X:
    n = 0
    for i in results_list:
        n += 1
        path_i = os.path.join(path, i)
        organism_name = i.replace('.xlsx', '')
        table = pd.ExcelFile(path_i)
        df_full = table.parse('Sheet1') # исходную таблицу преобразовали в объект Pandas
        try:
            db_df = group(db, organism_name, df_full) # возвращает группировку по каждой БД в виде DataFrame
            if n == 1:
                df = db_df
            if n > 1: 
                new_db_df = db_df
                df = pd.concat([df, new_db_df], axis=1)
        except:
            if n == 1:
                n = 0
            print("пропуск")
    output_path = os.path.join(path_up, 'Output_Tables')
    if not os.path.isdir(output_path):
        os.mkdir(output_path)
    export(db, output_path)
    print("Анализ", db, 'закончен')
print("Всё закончено")