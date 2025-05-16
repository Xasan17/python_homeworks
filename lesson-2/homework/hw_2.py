#1
from datetime import datetime 
name = input('Write name: ')
year = int(input('Write birth year: '))
age = datetime.now().year-year
print(f'Your age {age}')
#2
#2
txt = 'LMaasleitbtui'
car_name = input('Write car name: ')
for item in car_name:
    if item in txt:
        txt=txt.replace(item,'',1)
        
    else:
        print('No this car')
        break
else:
    print(f'Yes, this txt had {car_name}')
#3
txt = 'MsaatmiazD'
car_name = input('Write car name: ')
for item in car_name:
    if item in txt:
        txt=txt.replace(item,'',1)
        
    else:
        print('No this car')
        break
else:
    print(f'Yes, this txt had {car_name}')
#4
txt = "I'am John. I am from London"
print(txt[txt.find('I am from ')+10:])
#5
print(txt[::-1])
#6
txt = "I'am John. I am from London"
i=0
for item in txt:
    if item in ['a','e','i','u','o']:
        i+=1
print(i)
#7
while True:
    try:
        numbers = input('Write numbers separated by commas: ')
        list = []
        for item in numbers.split(','):
            list.append(int(item.strip()))
        print(max(list))
        break
    except ValueError:
        print('Error: You entered something wrong. Please enter only numbers separated by commas')
#8
text = input('Write text: ')
if text==text[::-1]:
    print(f'This word {text} is a polindrome') 
else:
    print(f'This word {text} is not a polindrome') 
#9
email = input('Write email: ')
print(email[email.find('@')+1::])
#10
import random 
import string 
password_length = int(input("Enter the desired password length: "))
all_chars = string.ascii_letters + string.digits+ string.punctuation
password = ''.join(random.choice(all_chars) for _ in range(password_length))

print("Generated password:", password)

  
