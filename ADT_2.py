#! /usr/bin/python3
# вторая часть для исследования результатов работы EggNOG

import pandas as pd
import os
import sys
from pathlib import Path

def export(name, df, plus, folder_path):
    export_name = plus + name
    path_export = os.path.join(folder_path, export_name)
    if os.path.isfile(path_export):
        os.remove(path_export)
    df.to_csv(path_export)

# НАЧАЛО
path_2 = os.path.join(os.getcwd(), sys.argv[2]+sys.argv[1])
path_up = Path(path_2).parent
path_output = os.path.join(path_up, sys.argv[2]+'_2_Quantifiably_changing_groups')

output_tables_list = os.listdir(path_2)

if not os.path.isdir(path_output):
    os.mkdir(path_output)

for j in output_tables_list:
    path_j = os.path.join(path_2, j)
    db = pd.read_csv(path_j)
    print("Ищу закономерности в", j)
    db_arctic_plus = db[(db['MoH'] < db['M2']) & (db['MoH'] < db['MK4']) & (db['AL-21'] < db['SMA-27']) & (db['AL-21'] < db['VT'])]
    probel_1 = pd.DataFrame({'-', '-', '-', '-', '-', '-', '-'})
    db_arctic_minus = db[(db['MoH'] > db['M2']) & (db['MoH'] > db['MK4']) & (db['AL-21'] > db['SMA-27']) & (db['AL-21'] > db['VT'])]
    db_arctic = pd.concat([db_arctic_plus, probel_1, db_arctic_minus], axis=0)
    db_arctic = db_arctic[['Unnamed: 0', 'MoH', 'M2', 'MK4', 'AL-21', 'SMA-27', 'VT']]
    
    db_all_plus = db[(db['MoH'] < db['M2']) & (db['MoH'] < db['MK4']) & (db['AL-21'] < db['SMA-27']) & (db['AL-21'] < db['VT']) &
                 (db['congo'] < db['SWAN-1']) & (db['E09F3'] < db['SWAN-1']) & (db['BRM9'] < db['A8P']) & (db['petro'] < db['A8P'])
                 & (db['CANT'] < db['WeN3'])]
    probel_2 = pd.DataFrame({'-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'})
    db_all_minus = db[(db['MoH'] > db['M2']) & (db['MoH'] > db['MK4']) & (db['AL-21'] > db['SMA-27']) & (db['AL-21'] > db['VT']) &
                 (db['congo'] > db['SWAN-1']) & (db['E09F3'] > db['SWAN-1']) & (db['BRM9'] > db['A8P']) & (db['petro'] > db['A8P'])
                 & (db['CANT'] > db['WeN3'])]
    db_all = pd.concat([db_all_plus, probel_2, db_all_minus], axis=0)
    db_all = db_all[['Unnamed: 0', 'MoH', 'M2', 'MK4', 'AL-21', 'SMA-27', 'VT', 'congo', 'E09F3', 'SWAN-1', 'BRM9', 'petro', 'A8P', 'CANT', 'WeN3']]
    
    db_control_1 = db_arctic.dropna(axis = 0)
    db_control_2 = db_all.dropna(axis = 0)
    
    if db_control_1.empty == False:
        export(j, db_arctic, 'arctic_', path_output)
        print('   у арктических - есть закономерности. Файл записан')
    else:
        print('   у арктических - закономерности нет')

    if db_control_2.empty == False:
        export(j, db_all, 'all_', path_output)
        print("   у всех - есть закономерности. Файл записан")
    else:
        print('   у всех - закономерности нет')
   