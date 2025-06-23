import numpy as np
#1
lis = [12.23, 13.32, 100, 36.32]  
arr1 =np.array(lis) 
print(arr1)
#2
arr2 = np.arange(2,11).reshape(3,3)
print(arr2)
#3
arr3 = np.zeros(10)
arr3[6]=11
print(arr3)
#4
arr4 = np.arange(12,38)
print(arr4)
#5
arr5 = np.array([1, 2, 3, 4],dtype=float)
print(arr5)
#6
fahrenheit = np.array([0, 12, 45.21, 34, 99.91, 0.])
celsius = (fahrenheit - 32) * 5 / 9
print("Значения в градусах Цельсия:", np.round(celsius, 2))
print("Значения в градусах Фаренгейта:", fahrenheit)
#7
arr7 = np.array([10,20,30])
arr = np.append(arr7,np.arange(40,100,10))
print(arr)
#8
arr8 = np.random.randn(10)
arr_mean = arr8.mean()
arr_medin = np.median(arr8)
arr_standar_dev = np.std(arr8)
print(f'Mean: {arr_mean}')
print(f'Median: {arr_medin}')
print(f'Standard deviation: {arr_standar_dev}')
#9
arr9 = np.random.randn(10,10)
arr_min = np.min(arr9)
arr_max = np.max(arr9)
print(f'min: {arr_min}\nmax: {arr_max}')
#10
arr10 = np.random.rand(3,3,3)
print(arr10)
