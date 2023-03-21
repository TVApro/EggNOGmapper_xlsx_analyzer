#! /usr/bin/python3
# третья часть для исследования результатов работы EggNOG

import pandas as pd
import os
import re
import openpyxl
from pathlib import Path

# НАЧАЛО
path = '/home/trubitsyns/Рабочий стол/Кандидатская работа/Tables_4+_I_dont_know_for_what_it_is'
path_up = Path(path_4).parent # исходная директория
input_list = os.listdir(path)
path_output = os.path.join(path_up, 'Tables_5+_I_dont_know_for_what_it_is')
if not os.path.isdir(path_output):
    os.mkdir(path_output) # создание папки с выходящими файлами

def to_pandas(x, path):
    path_input = os.path.join(path, x)
    df = pd.ExcelFile(path_input)
    df_df = df.parse('Sheet1')
    return df_df

arctic_list = ['VT', 'SMA-27', 'AL-21', 'MK4', 'M2', 'MoH']
all_list = ['VT', 'SMA-27', 'AL-21', 'MK4', 'M2', 'MoH',
           'SWAN1', 'E09F3', 'congo', 'BRM9', 'Mic5c12T', 'A8P',
           'WeN3', 'CANT']
listX = ['query']

n=0
m=0
for t in listX:
    for i in input_list:
        if '_arctic_' in i:
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

                
    if '_all_' in i:
        for j in all_list:
            if j in i:
                j=to_pandas(i, path_up)
