
import re
def clean_phone(phone):
    cleaned_phone = re.sub(r'\D', '', str(phone))
    if cleaned_phone.startswith('8'):
        cleaned_phone = '7' + cleaned_phone[1:]  
    elif not cleaned_phone.startswith(('7', '8')):
        cleaned_phone = cleaned_phone +', не соответствует телефонному номеру'
    return cleaned_phone
df = pd.read_excel('phone_numbers.xlsx')
df['phone_number'] = df['phone_number'].apply(clean_phone)
df.to_excel('new.xlsx', index=False)


