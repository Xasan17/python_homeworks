#1
txt = input('Enter txt : ')
archive = ['a','e','u','i','o']
i = 0
x=0
length = len(txt)
txt_new = []
for item in txt:
    i+=1
    x+=1
    txt_new.append(item)
    if i >= 3 and item not in archive and x != length:
        archive.append(item)
        txt_new.append('_')
        i=0
txt =''.join(txt_new)    
print(str(txt))
#2
n = int(input('Enter number: '))
i=0
while i<n:
    print(i**2)
    i+=1
#3
#Exercise 1
i=1
while i<=10:
    print(i)
    i+=1
#Exercise 2
n = int(input('son kiriting: '))
i = 1
list_1 = []
while i <= n:
    list_1.append(i)
    numbers = ' '.join(str(num) for num in list_1)
    print(numbers)
    i+=1
#Exercise 3
n = int(input('Enter a number: '))
i = 0
s=0
while i<n:
    i +=1
    s = s+i
print(s)
#Exercise 4
n = int(input('Enter a number: '))
i=1
while i<=10:
    print(i*n)
    i+=1
#Exercise 5
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers :
    if num % 5 == 0 and num <=150 and num > 50:
        print(num)
#Exercise 6
n = 75869
x=0
for item in str(n):
    x+=1
print(x)
#Exercise 7
n = int(input('Enter a numbers: '))
numbers = []
i=1
while i<=n:
    numbers.append(i)
    i+=1
i-=1
numbers.reverse()

while i>0:
    print(' '.join(str(num) for num in numbers))
    numbers.remove(i)
    i-=1
#Exercise 8
list1 = [10, 20, 30, 40, 50]
list1.sort(reverse=True)
for lst in list1:
    print(lst)
#Exercise 9
for item in range(-10,0):
    print(item)
#Exercise 10
for i in range(0,5):
    print(i)
print('Done!')
#Exercise 11
for i in range(25,51):
    x=2
    a=0
    while x < i**(1/2)+1:
        if i % x == 0 :
            break
        x+=1
    if x-1 == int(i**(1/2)+1) or i==2:
        print(i)
    
#Exercise 12
n = int(input('Enter a number: '))
i = 0
n1,n2=0,1

while i< n:
    print(n1)
    nth = n1+n2
    n1 = n2
    n2=nth
    i = i+1
#Exercise 13
n = int(input('Enter a number: '))
p=1
i=0
while i<n:
    i+=1
    p = p*i
print(p)
#4
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

list_new = [x for x in list1 if x not in list2]
list_new += [x for x in list2 if x not in list1]

print(list_new)
