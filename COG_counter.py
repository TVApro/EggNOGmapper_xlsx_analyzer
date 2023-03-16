#! /usr/bin/python3
# Программа для исследования результатов работы EggNOG

import re
from re import sub
import textwrap as tw
import pandas as pd
import openpyxl
import os
from collections import Counter

#path = input("Укажите путь до папки с таблицами: ")
path = '/media/lab330/Новый том/EggNOG/Tables'
strange = input("Считать функциональные группы COG? (y/n) ")
results_list = os.listdir(path)
n = 0
for i in results_list:
    n += 1
    path_i = os.path.join(path, i)
    i_name = i.replace('.xlsx', '')
    table = pd.ExcelFile(path_i)
    df1 = table.parse('Sheet1') # исходную таблицу преобразовали в объект Pandas
    if strange == 'y':
        COG_df = df1['COG_category'].value_counts() # подсчёт значений в столбце COG_category
    if strange == 'n':
        COG_df = df1['Preferred_name'].value_counts() # подсчёт значений в столбце Description
    if n == 1:
        df = COG_df.to_frame()  # превращаем Series в DataFrame (создаём заново)
        df.columns = [i_name] # имя колонки - название таблицы
    if n > 1:
        new_df = COG_df.to_frame() # превращаем Series в DataFrame (доращиваем)
        new_df.columns = [i_name] # имя колонки - название таблицы
        df = pd.concat([df, new_df], axis = 1) # объединяем датафреймы
print(df)
if strange == 'n':
    export = input('Под каким именем вы хотите сохранить результат?')
    path_export = os.path.join(path, export)
    df.to_csv(path_export)