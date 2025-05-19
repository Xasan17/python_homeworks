#1
list = ['banana', 'apple', 'abrikos', 'orange', 'water meloun']
print(list[2])
#2
l1 = [1, 2, 3, 4, 5]
l2 = [5, 6, 7, 8, 9]
l = l1+l2
print(l)
#3
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
l = l1[0]+l1[len(l1)//2]+l1[-1]
print(l)
#4
list1 = ['olmas', 'Tolmas', 'Ketmas', 'Yurmas', 'Kochmas']
tuple1 = tuple(list1)
print(tuple1)
#5
lists = ['London', 'Paris', 'Moscow', 'Manchester', 'Chicaco']
if lists.count('Paris') == 0:
    print('Not found')
else:
    print(f'Paris founded {lists.count('Paris')}')
  #6
list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
duplicated_list = list1*2
print(duplicated_list)
#7
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
list1 = []
list1 = l[0]
l[0] = l[-1] 
l[-1] = list1
print(l)
#8
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuple1[3:7]
#9
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white"]
print(colors.count('blue'))
#10
animals = ("cat", "dog", "elephant", "lion", "tiger", "giraffe", "zebra", "panda", "bear", "monkey")
print(animals.index('lion'))
#11
tup1 = (1, 2, 3, 4, 5)
tup2 = (5, 6, 7, 8, 9)
tup = tup1 + tup2
print(tup)
#12
list1 = [1, 2, 3, 4, 5]
tup2 = (5, 6, 7, 8, 9,2,2,2)
print(f'length list {len(list1)} and length tuple {len(tup2)}')
#13
tup = (5, 6, 7, 8, 9)
my_list  = list(tup)
print(my_list )
#14
tup2 = (5, 6, 7, 8, 9,2,2,2)
print(f'Max number in tuple {max(tup2)} and min number in tuple {min(tup2)}')
#15
words = ('apple', 'banana', 'cherry', 'date', 'elderberry')
words_list = list(words)
words_list.reverse()
words = tuple(words_list)
print(words)








