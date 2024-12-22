import re
text = "Мій номер телефону: +380 (067) 123-45-67, а також +380987654321."
phone_pattern = r'(\+?\d{1,3}[\s\-]?\(?\d{2,3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2})'
phone_numbers = re.findall(phone_pattern,text)

for phone in phone_numbers:
    print(''.join(phone))
