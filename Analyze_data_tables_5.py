#! /usr/bin/python3
# вторая часть для исследования результатов работы EggNOG

import pandas as pd
import os
from pathlib import Path

def export(name, df, plus, folder_path):
    export_name = plus + name
    path_export = os.path.join(folder_path, export_name)
    if os.path.isfile(path_export):
        os.remove(path_export)
    df.to_csv(path_export)

# НАЧАЛО
path_1 = '/home/trubitsyns/Рабочий стол/Кандидатская работа/Tables'
path_2 = '/home/trubitsyns/Рабочий стол/Кандидатская работа/Tables_4_Quantifiably_changing_genes_in_quantifiably_changing__groups'
path_up = Path(path_2).parent
path_output = os.path.join(path_up, 'Tables_5_All_Quantifiably_changing_genes_in_one')

organisms_list = os.listdir(path_1)
tables_list = os.listdir(path_2)

file1 = os.path.join(path_output, 'arctic_all.csv')
file2 = os.path.join(path_output, 'all_all.csv')
n = 0
m = 0

if not os.path.isdir(path_output):
    os.mkdir(path_output)

for j in tables_list:
    print('Собираю совпадения из', j)
    path_j = os.path.join(path_2, j)
    db1 = pd.read_csv(path_j)
    db = db1.drop(columns='Unnamed: 0')
    if 'specific_genes_arctic_' in j:
        n += 1
        if n == 1:
            db_arctic = db
        if n > 1:
            db_arctic = pd.merge(db_arctic, db, how = 'outer')
    if 'specific_genes_all_' in j:
        m += 1
        if m == 1:
            db_all = db
        if m > 1:
            db_all = pd.merge(db_all, db, how = 'outer')
db_arctic.to_csv(file1)
db_all.to_csv(file2)
        
    
