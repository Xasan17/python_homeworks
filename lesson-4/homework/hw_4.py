#Dictionary tasks
#1
dict_1 = {'a':5,'b':2,'c':3}
print(f'Ascending by values: {dict(sorted(dict_1.items(), key=lambda item: item[1], reverse=False))}')
print(f'Descending by values: {dict(sorted(dict_1.items(), key=lambda item: item[1], reverse=True))}')
#2
dct={0: 10, 1: 20}
dct.update({2: 30})
print(dct)
#3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic = dic1| dic2| dic3
print(dic)
#4
x=0
n=int(input('put number: '))
dic={}
while x<n:
    x+=1
    dic.update({x: x**2})
print(dic)
#5
dic1={}
for x in range(1,16):
    dic1[x] = x**2
print(dic1)
#SET tasks
#1
import random as r
st = set({})
n=int(input('put number: '))
for _ in range(1,n):
    st.add(r.randint(1,100))
print(st)
#2
for item in st:
    print(item)
#3
st.update([12,17,17,45])
print(st)
#4
st.remove(12)
print(st)
#5
x1=len(st)
st.discard(79)
x2=len(st)
if x2==x1:
    print("This set don't have this number")
else :
    print('removed this number')
