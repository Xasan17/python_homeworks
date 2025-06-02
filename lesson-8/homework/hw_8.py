#1
try:
    a = int(input('enter first number: '))
    b = int(input('enter second number: '))
    c = a/b
    print(c)
except ZeroDivisionError:
    print('nolga bolish mumkin emas')
#2
try:
    a = int(input('enter first number: '))
except ValueError:
    print('Value Error')

#3
try:
    a = open('text.csv', 'r')
except FileNotFoundError:
    print('xatolik bor')
#4
try:
    a = input('enter first number: ')
    b = input('enter second number: ')
    c = a/b
    print(c)
except TypeError:
    print('xatolik yuz berdi')
#5
try:
    with open('file.csv', 'r') as file:
        content = file.read()
        print('files data')
except PermissionError:
     print(f"Ошибка: Нет прав доступа к файлу file.csv")
except FileNotFoundError:
    print(f"Ошибка: Файл file.csv не найден")
except Exception as e:
    print(f"Произошла другая ошибка: {e}")

#6
try:
    list1 = ['xasan', 1, 2 , 6, 8]
    list1[5]=21
except IndexError:
    print('Index Error')

#7
try:
    a = input('enter first number: ')
    print({a})
except KeyboardInterrupt:
    print('You stopped program')

#8
try:
    a = int(input('enter first number: '))
    b = int(input('enter second number: '))
    c = a/b
    print(c)
except ArithmeticError as e:
    print(f'type error {e}')

#9
file_path = input("Введите путь к файлу: ")

try:
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())
except UnicodeDecodeError:
    print("Ошибка: Файл нельзя прочитать в кодировке UTF-8.")
except Exception as e:
    print(f'Произошла ошибка {e}')

#10
try:
    a = int(input('Enter number: '))
    a = a.isbig()
except AttributeError:
    print('Такое атрибута нет')

#11
file_path = input('Enter road file ')
try:
    with open(file_path, 'r',encoding='UTF-8') as file:
        content = file.read()
        print('Success upload')
except Exception as e:
    print(e)

#12
file_path = input('Enter road csv file ')
try:
    with open(file_path, 'r',encoding='UTF-8') as file:
        n = int(input('Numbers row:'))
        for _ in range(n):
            line = file.readline()
            if not line:
                break
            print(line.strip())
except Exception as e:
    print(e)

#13
file_path = input('Enter road csv file ')
text_to_add = input('Ведите текст: ')
try:
    file = open('text.csv', 'a+', encoding='utf-8')
    file.seek(0, 2)
    start_pos = file.tell()
    while True:
        file.write(text_to_add + '\n')
        answer = input('Еще хотите вводит данные: (yes/no)')
        if answer =='yes':
            text_to_add = input('Ведите текст: ')
            continue
        else:
            break   
    file.seek(start_pos)
    content = file.read()
    print(content)
except Exception as e:
    print({e})
finally:
    file.close()

#14
from collections import deque

file_path = input("Введите путь к файлу: ")
try:
    n = int(input("Сколько последних строк прочитать: "))
    
    with open(file_path, 'r', encoding='utf-8') as file:
        last_lines = deque(file, maxlen=n)  
    for line in last_lines:
        print(line.strip())
except Exception as e:
    print(f"Ошибка: {e}")
#15
file_path = input('Enter road csv file ')
try:
    with open(file_path, 'r',encoding='UTF-8') as file:
        content=[line.strip() for line in file.readlines()]
        print(content)
except Exception as e:
    print(e)
#16
file_path = input('Enter road csv file ')
try:
    with open(file_path, 'r',encoding='UTF-8') as file:
        for line in file:
            content+=' '+line.strip()
        print(content)
except Exception as e:
    print(e)

#17
import numpy as np
file_path = input('Enter road csv file ')
try:
    with open(file_path, 'r',encoding='UTF-8') as file:
        lines = [line.strip() for line in file]
        arr=np.array(lines)
    print(arr)
except Exception as e:
    print(e)

#18
file_path = input('Enter road csv file ')
try:
    with open(file_path, 'r',encoding='UTF-8') as file:
        text = file.read()
        for char in '.,;:!?()[]{}"\'':
            text = text.replace(char,' ')
        words = text.split()
        max_len = max(len(word) for word in words)
        longest_words = [word for word in words if max_len==len(word)]
        print(f'Самое большое число {longest_words}')
except Exception as e:
    print(e)

#19
file_path = input('Enter road csv file ')
try:
    with open(file_path, 'r',encoding='UTF-8') as file:
        i = sum(1 for _ in file)
        print(i)
except Exception as e:
    print(e)

#20
file_path = input('Enter road csv file ')
try:
    with open(file_path, 'r',encoding='UTF-8') as file:
        text = file.read()
        for char in '.,;:!?()[]{}"\'':
            text = text.replace(char,' ')
        words = text.split()
        dict1 = {}
        for word in words :
            dict1.update([(word,words.count(word))])
        print(dict1)
except Exception as e:
    print(e)

#21
import os
file_path = input('Enter road csv file ')
try:
    file_size = os.path.getsize(file_path)
    with open(file_path, 'r',encoding='UTF-8') as file:
        text = file.read()
        print(len(text))
        print(f'{file_size} байт')
except Exception as e:
    print(e)

#22
file_path = input('Enter road csv file ')
try:
    add_list = ['Xasan','Sodiqov', 'Alisherov','Tolagan']
    with open(file_path, 'w',encoding='UTF-8') as file:
        for word in add_list:
            file.write(word + '\n')
        print('Success')
except Exception as e:
    print(e)

#23
file_read = input('Enter road csv read file ')
file_write = input('Enter road csv write file ')
try:
    with open(file_read, 'r',encoding='UTF-8') as source_file:
        text = source_file.read()
    with open(file_write, 'w',encoding='UTF-8') as dest_file:
        dest_file.write(text)
        print('Success')
except Exception as e:
    print(e)

#24
first_file = input('Enter road csv first file ')
second_file = input('Enter road csv second file ')
file_write = input('Enter road csv write file ')
try:
    first_source = open(first_file, 'r',encoding='UTF-8') 
    second_source = open(second_file, 'r',encoding='UTF-8')

    with open(file_write, 'w',encoding='UTF-8') as dest_file:
        for first, second in zip(first_source, second_source):
            dest_file.write(first.strip() +', ' + second.strip() + '\n' )
        print('Success')
except Exception as e:
    print(e)
finally:
    first_source.close()
    second_source.close()

#25
import random
file_path = input('Enter road csv file ')
try:
    with open(file_path, 'r',encoding='UTF-8') as file:
        lines = file.readlines()
        if lines:
            random_line = random.choice(lines)
            print(random_line.strip())
        else:
            print("File don't have data")
except Exception as e:
    print(e)
#26
file_path = input("Enter path to file: ")

try:
    file = open(file_path, 'r', encoding='utf-8')
    print("Файл закрыт?", file.closed)
    file.close()
    print("Файл закрыт?", file.closed) 
except Exception as e:
    print(f"Ошибка: {e}")
#27
file_path = input("Enter path to file: ")

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    cleaned_lines = [line.strip() for line in lines]
    print(cleaned_lines)

    with open(file_path, 'w', encoding='utf-8') as file:
        for line in cleaned_lines:
            file.write(line + ' ') 
    print("Символы новой строки удалены.")
except Exception as e:
    print(f"Ошибка: {e}")

#28
file_path = input('Enter road csv file ')
try:
    with open(file_path, 'r',encoding='UTF-8') as file:
        text = file.read()
        for char in '.,;:!?()[]{}"\'':
            text = text.replace(char,' ')
        words = text.split()
        i=sum(1 for _ in words)
        print(i)
except Exception as e:
    print(e)

#29
import os
file_paths = input("Введите пути к текстовым файлам через запятую: ").split(',')

characters = []

for path in file_paths:
    path = path.strip()  # Убираем пробелы
    if not os.path.exists(path):
        print(f"Файл не найден: {path}")
        continue

    try:
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
            characters.extend(list(text))  # добавляем каждый символ в список
    except Exception as e:
        print(f"Ошибка при чтении {path}: {e}")

print("Извлечённые символы:")
print(characters)

#30
list_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for name in list_name:
    filename = name + '.txt'
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            pass
    except Exception as e:
        print(f"Ошибка при создании файла {filename}: {e}")

print('Файлы успешно созданы!')

#31
ist_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
try:
    file_path = input('Enter road csv file ')
    n = int(input('напишите сколько букв должно в строке: '))
    with open(file_path, 'w+', encoding='utf-8') as file:
        for item, letter in enumerate(ist_name):
            file.write(letter)
            if item !=0 and (item+1)%(n)==0:
                file.write('\n') 
except Exception as e:
    print({e})



