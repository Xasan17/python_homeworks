#1
try:
    year = int(input("Write year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(True)
    else:
        print(False)
except ValueError:
    print("Year must be an integer.")
#2
n = int(input('Enter a number : '))
if n>=1 and n<=100 :
    if n % 2 == 1 or (n % 2 == 0 and (n>=6 and n<=20)):
        answer = 'Weird' 
    else :
        answer = 'Not Weird'
    
else :
    answer = 'Constraints 1 <= number <= 100'
print(answer)
#3
#Solution 1
a = int(input('a = '))
b = int(input('b = '))
if a > b :
    a,b = b,a
if a % 2 != 0:
    a += 1
if b % 2 != 0:
    b -= 1 
numbers = list(range(a,b+1,2))

print(numbers)
#Solution 2
a = int(input('a = '))
b = int(input('b = '))
a,b = min(a,b), max(a,b)

numbers = list(range(a + a%2 ,b + 1 - b%2,2 ))
print(numbers)
