#1
def is_prime(n:int)->bool:
    i=2
    j = int(n**(0.5)+1)
    if n==1:
        return False
    while i< j  and n!=2:
        if n%i!=0:
            i+=1
        else :
            return False
    return True
#2
def digit_sum(k):
    total = 0
    while k > 0:
        total += k % 10
        k //= 10
    return total
#3
def power_of_two(n: int)->list:
    i=1
    while 2**i<= n:
        print(2 ** i,end=' ')
        i+=1
  
