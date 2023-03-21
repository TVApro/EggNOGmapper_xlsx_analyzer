#! /usr/bin/python3
# вторая часть для исследования результатов работы EggNOG

import pandas as pd
import openpyxl
import os
from pathlib import Path

def export(name, df, plus, folder_path):
    export_name = plus + name
    path_export = os.path.join(folder_path, export_name)
    if os.path.isfile(path_export):
        os.remove(path_export)
    df.to_csv(path_export)

# НАЧАЛО
path_1 = '/media/lab330/Новый том/EggNOG/Tables'
path_2 = '/media/lab330/Новый том/EggNOG/Tables_4_Quantifiably_changing_genes_in_quantifiably_changing__groups'
path_up = Path(path_2).parent
path_output = os.path.join(path_up, 'Tables_5_All_Quantifiably_changing_genes_in_one')

organisms_list = os.listdir(path_1)
tables_list = os.listdir(path_2)

n = 0
m = 0

if not os.path.isdir(path_output):
    os.mkdir(path_output)

for j in tables_list:
    print('Собираю совпадения из', j)
    j_name = j_name = j.replace('specific_genes_arctic_', '').replace('specific_genes_all_', '').replace('.csv', '')
    path_j = os.path.join(path_2, j)
    db1 = pd.read_csv(path_j)
    db = db1.drop(columns='Unnamed: 0')
    if 'specific_genes_arctic_' in j:
        n += 1
        if n == 1:
            db_arctic = db
            db_arctic = db_arctic.reindex(columns=['Description', 'MoH', 'M2', 'MK4', 'AL-21', 'SMA-27', 'VT', j_name])
        if n > 1:
            db_arctic = pd.merge(db_arctic, db, how = 'outer', sort=True)
            
    if 'specific_genes_all_' in j:
        m += 1
        if m == 1:
            db_all = db
        if m > 1:
            db_all = pd.merge(db_all, db, how = 'outer')

db_new1 = db_arctic.set_index('Description')
db_new2 = db_all.set_index('Description')

file1 = os.path.join(path_output, 'arctic_all.xlsx')
file2 = os.path.join(path_output, 'all_all.xlsx')

db_new1.to_excel(file1)
db_new2.to_excel(file2)