from datetime import datetime,date, timedelta
from dateutil.relativedelta import relativedelta
import pytz
import time
import re
#1
birth_date_str =input(f'Enter your birthday in format DD.MM.YYYY: ')
try:
    birth_date = datetime.strptime(birth_date_str, "%d.%m.%Y")
except ValueError:
    print('Format erroring')
    exit()
today = datetime.today()
age = relativedelta(today,birth_date)
print(f'Year: {age.years}, Month: {age.months}, Days: {age.days}')
#2
birth_date_str =input(f'Enter your birthday in format DD.MM.YYYY: ')
try:
    birth_date = datetime.strptime(birth_date_str, "%d.%m.%Y")
except ValueError:
    print('Format erroring')
    exit()
today = datetime.today()
next_birthday = datetime(today.year, birth_date.month, birth_date.day)
if next_birthday<today:
    next_birthday = datetime(today.year+1, birth_date.month, birth_date.day)
delta = next_birthday - today
print(f"До следующего дня рождения осталось: {delta.days} дней.")
#3
meet_datetime_str =input(f'Enter current date and time in format hh:mm.DD.MM.YYYY: ')
meet_time_str = input(f'Duration of a meeting in hours and minutes hh.mm:')
try:
    meet_datetime  = datetime.strptime(meet_datetime_str, "%H:%M.%d.%m.%Y")
    hours_str,minute_str = meet_time_str.split('.')
    duration = timedelta(hours=int(hours_str), minutes=int(minute_str))
    end_meet = meet_datetime + duration
    print(f"Meeting will end at: {end_meet.strftime('%H:%M on %d.%m.%Y')}")
except ValueError:
    print('Format erroring')
except Exception as e:
    print(f'Unexpected error: {e}')
#4
all_timezones = pytz.all_timezones
datetime_str = input("Enter date and time (format: DD.MM.YYYY HH:MM): ")
from_timezone_str = input("Enter your current timezone (e.g., Asia/Tashkent): ")
to_timezone_str = input("Enter target timezone (e.g., US/Eastern): ")
try:
    naive_datetime = datetime.strptime(datetime_str, "%d.%m.%Y %H:%M")
    if from_timezone_str not in all_timezones or to_timezone_str not in all_timezones:
        raise ValueError("Invalid timezone name")
    from_timezone = pytz.timezone(from_timezone_str)
    aware_datetime = from_timezone.localize(naive_datetime)
    to_timezone = pytz.timezone(to_timezone_str)
    converted_datetime = aware_datetime.astimezone(to_timezone)
    print(f"\nIn {to_timezone_str}, the time will be: {converted_datetime.strftime('%d.%m.%Y %H:%M')}")
    
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
#5
target_str = input("Enter target date and time (format: DD.MM.YYYY HH:MM:SS): ")
try:
    target_datetime = datetime.strptime(target_str, "%d.%m.%Y %H:%M:%S" )
    while True:
        now = datetime.now()
        remaining = target_datetime - now
        if remaining.total_seconds()<=0:
            print("Time's up!")
            break
        days = remaining.days
        hours,rem= divmod(remaining.seconds,3600)
        minutes,seconds = divmod(rem,60)
        print(f"Time left: {days}d {hours}h {minutes}m {seconds}s")
        time.sleep(1)
except ValueError:
    print("Invalid date format.Use: DD.MM.YYYY HH:MM:SS ")  
#6
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,}$'
email = input('Enter your email: ')
if re.fullmatch(email_pattern,email):
    print('Email correct.')
else:
    print("Your email no correct ")

#7
phone = input("Enter your phone (only numbers): ")
digits = re.sub(r'\D', '' , phone)
if len(digits)==10:
    formatted = f"({digits[:3]}){digits[3:6]}-{digits[6:]}"
    print("Форматированный номер:", formatted)
else:
    print('phone must have 10 numbers.')

#8
password = input('Enter password: ')
length_ok = len(password)>=8
has_upper = re.search(r'[A-Z]',password)
has_lower = re.search(r'[a-z]',password)
has_digit = re.search(r'\d',password)
if length_ok and has_upper and has_lower and has_digit:
    print("✅ Пароль надёжный.")
else:
    print("❌ Пароль ненадёжный. Проверьте, что он содержит:")
    if not length_ok:
        print("- минимум 8 символов")
    if not has_upper:
        print("- хотя бы одну заглавную букву")
    if not has_lower:
        print("- хотя бы одну строчную букву")
    if not has_digit:
        print("- хотя бы одну цифру")
#9
text = """
Python — это мощный язык программирования. Многие изучают Python для анализа данных, веб-разработки, автоматизации и машинного обучения.
Python прост в использовании, но очень гибкий.
"""
word = input("Введите слово для поиска: ")
matches = re.findall(rf'\b{re.escape(word)}\b',text,flags = re.IGNORECASE)
if matches:
    print(f"✅ Слово '{word}' найдено {len(matches)} раз(а) в тексте.")
else:
    print(f"❌ Слово '{word}' не найдено в тексте.")

#10
date_pattern = r'\b(?:\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}|\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s\d{4})\b'
user_text = input("Введите текст, содержащий даты: ")
found_dates= re.findall(date_pattern,user_text,re.IGNORECASE)
if found_dates:
    print("Found date")
    for date in found_dates:
        print('-',date)
else:
    print("don't found")

  
