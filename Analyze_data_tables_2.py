#! /usr/bin/python3
# вторая часть для исследования результатов работы EggNOG

import pandas as pd
import os
import re
from pathlib import Path

def export(name, df, plus, folder_path):
    export_name = plus + name
    path_export = os.path.join(folder_path, export_name)
    if os.path.isfile(path_export):
        os.remove(path_export)
    df.to_csv(path_export)

# НАЧАЛО
path_1 = '/home/trubitsyns/Рабочий стол/Кандидатская работа/Tables'
path_2 = '/home/trubitsyns/Рабочий стол/Кандидатская работа/Tables_1_Total_number_of_genes'
path_up = Path(path_2).parent
path_output = os.path.join(path_up, 'Tables_2_Quantifiably_changing_groups')

organisms_list = os.listdir(path_1)
output_tables_list = os.listdir(path_2)

if not os.path.isdir(path_output):
    os.mkdir(path_output)

for j in output_tables_list:
    path_j = os.path.join(path_2, j)
    db = pd.read_csv(path_j)
    print("Анализирую", j)
    db_arctic_plus = db[(db['MoH'] < db['M2']) & (db['MoH'] < db['MK4']) & (db['AL-21'] < db['SMA-27']) & (db['AL-21'] < db['VT'])]
    probel_1 = pd.DataFrame({'-', '-', '-', '-', '-', '-', '-'})
    db_arctic_minus = db[(db['MoH'] > db['M2']) & (db['MoH'] > db['MK4']) & (db['AL-21'] > db['SMA-27']) & (db['AL-21'] > db['VT'])]
    db_arctic = pd.concat([db_arctic_plus, probel_1, db_arctic_minus], axis=0)
    db_arctic = db_arctic[['Unnamed: 0', 'MoH', 'M2', 'MK4', 'AL-21', 'SMA-27', 'VT']]
    
    db_all_plus = db[(db['MoH'] < db['M2']) & (db['MoH'] < db['MK4']) & (db['AL-21'] < db['SMA-27']) & (db['AL-21'] < db['VT']) &
                 (db['congo'] < db['SWAN1']) & (db['E09F3'] < db['SWAN1']) & (db['BRM9'] < db['A8P']) & (db['Mic5c12T'] < db['A8P'])
                 & (db['CANT'] < db['WeN3'])]
    probel_2 = pd.DataFrame({'-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'})
    db_all_minus = db[(db['MoH'] > db['M2']) & (db['MoH'] > db['MK4']) & (db['AL-21'] > db['SMA-27']) & (db['AL-21'] > db['VT']) &
                 (db['congo'] > db['SWAN1']) & (db['E09F3'] > db['SWAN1']) & (db['BRM9'] > db['A8P']) & (db['Mic5c12T'] > db['A8P'])
                 & (db['CANT'] > db['WeN3'])]
    db_all = pd.concat([db_all_plus, probel_2, db_all_minus], axis=0)
    db_all = db_all[['Unnamed: 0', 'MoH', 'M2', 'MK4', 'AL-21', 'SMA-27', 'VT', 'congo', 'E09F3', 'SWAN1', 'BRM9', 'Mic5c12T', 'A8P', 'CANT', 'WeN3']]
    
    export(j, db_arctic, 'arctic_', path_output)
    export(j, db_all, 'all_', path_output)
