#! /usr/bin/python3
# Программа для исследования результатов работы EggNOG

import pandas as pd
import os
from collections import Counter

#path = input("Укажите путь до папки с таблицами: ")
path = '/EggNOG/Tables'
#description = input("Введите название столбца, по которому хотите осуществить поиск? Проверьте название заранее: ")
description = 'Description'
#COG_group = input("Введите название группы COG, в пределах которой хотите осуществить поиск: ")
COG_group = 'C'
results_list = os.listdir(path)
n = 0
for i in results_list:
    n += 1
    path_i = os.path.join(path, i)
    i_name = i.replace('.xlsx', '')
    table = pd.ExcelFile(path_i)
    df1 = table.parse('Sheet1') # исходную таблицу преобразовали в объект Pandas
    if COG_group:
        COG_df1 = df1.loc[df1['COG_category'] == COG_group]
        COG_df2 = COG_df1[description].value_counts() # подсчёт значений в столбце COG_category
    else:
        COG_df2=df1[description].value_counts()
    if n == 1:
        df = COG_df2.to_frame()  # превращаем Series в DataFrame (создаём заново)
        df.columns = [i_name] # имя колонки - название таблицы
    if n > 1:
        new_df = COG_df2.to_frame() # превращаем Series в DataFrame (доращиваем)
        new_df.columns = [i_name] # имя колонки - название таблицы
        df = pd.concat([df, new_df], axis = 1) # объединяем датафреймы
print(df)

export = input('Имя для сохранения (если нужно):')
if export:
    export_name = export + '.csv'
    path_export = os.path.join(path, export_name)
    df.to_csv(path_export)
    print('Сохранён файл', path_export)
