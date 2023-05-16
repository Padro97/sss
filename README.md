import pandas as pd
import re

excel_data_df = pd.read_excel('phone_numbers.xlsx')
print(excel_data_df)

Первые две строки импортируют две библиотеки: pandas и re. 
Далее, с помощью команды excel_data_df = pd.read_excel('phone_numbers.xlsx') открывается и считывается таблица 'phone_nembers.xlsx',
и следующей же командой выводится содержимре этого файла

def clean_phone(phone):
    cleaned_phone = re.sub(r'\D', '', str(phone))
    if cleaned_phone.startswith('8'):
        cleaned_phone = '7' + cleaned_phone[1:]

Затем, создаётся функция 'clean_phone' для сортировки номеров от ненужных символов

cleaned_phone = re.sub(r'\D', '', str(phone))
    if cleaned_phone.startswith('8'):
        cleaned_phone = '7' + cleaned_phone[1:] 

Этими командами создаются условия для сортировки

df = pd.read_excel('phone_numbers.xlsx')
df['phone_number'] = df['phone_number'].apply(clean_phone)
df.to_excel('new.xlsx', index=False)

Далее, первой же командной программа снова считывает содержимое файла 'phone_numbers.xlsx' 
Вторая команда считывает значения из столбца 'phone_number' и применяет к ним функци. 'clean_phone'
Заключительная команда переносит очищенные номера телефонов в новую таблицу 'new.xlsx.
