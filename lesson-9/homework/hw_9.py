#1
import math
class Circle:
    @staticmethod
    def perimetr(r:float):
        return round(2*math.pi*r,2 ) 
    @staticmethod
    def area(r:float):
        return round(math.pi*r**2,2) 
xasan = Circle()
print(f'perimetr: {xasan.perimetr(10)}')
print(f'area: {xasan.area(10)}')

#2
from datetime import datetime
class People:
    def __init__(self, name:str, country:str, birthday: datetime):
        self.name = name
        self.country = country
        self.birthday = birthday
    def age(self):
        today = datetime.today()
        age = today.year - self.birthday.year
        if (today.month, today.day)<(self.birthday.month, self.birthday.day):
            age-=1
        return age

xasan = People('Xasan', 'Toshkent',datetime(1999,9,2)) 
print(f'Age {xasan.name}: {xasan.age()}')
#3
class Calculator :
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a+self.b
    
    def subtract(self):
        return self.a-self.b
    
    def multiply(self):
        return self.a*self.b
    
    def divide(self):
        if self.b == 0:
            return "Ошибка: деление на ноль"
        return self.a/self.b

calc = Calculator(5, 20)
print("Addition:", calc.add())
print("Subtraction:", calc.subtract())
print("Multiplication:", calc.multiply())
print("Division:", calc.divide())
#4
from abc import ABC, abstractmethod
import math

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Figure):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

class Square(Figure):
    def __init__(self, side: float):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return round(math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)), 2)

# Примеры использования:
circle = Circle(5)
square = Square(4)
triangle = Triangle(3, 4, 5)

print("Круг: площадь =", circle.area(), ", периметр =", circle.perimeter())
print("Квадрат: площадь =", square.area(), ", периметр =", square.perimeter())
print("Треугольник: площадь =", triangle.area(), ", периметр =", triangle.perimeter())

#5
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else :
            self._insert_recursive(self.root, value)
    def _insert_recursive(self,current,value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right=Node(value)
            else:
                self._insert_recursive(current.right, value)
    def search(self, value):
        return self._search_recursive(self.root,value)
    
    def _search_recursive(self,current, value):
        if current is None:
            return False
        if current.value==value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left,value)
        else:
            return self._search_recursive(current.right,value)
            
tree = BinarySearchTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(7)

print(tree.search(7))   # True
print(tree.search(20))  # False
#6
class Stack:
    
    def __init__(self):
        self.lst = []
    def push(self,arg):
        self.lst.append(arg)
        return arg
    def pop(self):
        if not self.is_empty():
            return self.lst.pop()
        else:
            return 'Стек пуст'
    def is_empty(self):
        return len(self.lst)==0
s = Stack()    
print(s.push('apple'))
print(s.push('banana'))
print(s.pop())
print(s.pop())
print(s.pop())
#7
class Node:
    def __init__(self,data=None,next = None):
        self.data = data
        self.next = next
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self,data):
        self.data = data
    def set_next(self,next):
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        cur_node = self.head
        if cur_node == None:
            self.head = new_node
            return
        while cur_node.get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)
        
    def display(self):
        cur_node = self.head
        output = ""
        while cur_node != None:
            output+= str(cur_node.get_data()) + '->'
            cur_node = cur_node.get_next()
        print(output)
    
    def delete(self, data):
        cur_node = self.head
        prev_node = None
        
        while cur_node is not None:
            if cur_node.get_data() == data:
                if prev_node is None:
                    self.head = cur_node.get_next()
                else:
                    prev_node.set_next(cur_node.get_next())
                return
            prev_node = cur_node
            cur_node = cur_node.get_next()
        print("Значение не найдено")

ll = LinkedList()
ll.insert(10)
ll.display()
ll.delete(10)
ll.display()
#8
class ShoppingCart:
    def __init__(self):
        self.shop_dict ={}
    def add_item(self,name, price):
        self.shop_dict[name]=price
    def remove_item(self,name):
        return self.shop_dict.pop(name, f"Товар '{name}' не найден")
    def total_price(self):
        return sum(self.shop_dict.values())
        
cart = ShoppingCart()
cart.add_item("Яблоко", 2.5)
cart.add_item("Хлеб", 1.8)
cart.add_item("Молоко", 3.2)

cart.remove_item("Хлеб")
cart.remove_item("Шоколад")  # Не существует

print("Общая стоимость:", cart.total_price())

#9
class Stack:
    
    def __init__(self):
        self.lst = []
    def push(self,arg):
        self.lst.append(arg)
        return arg
    def pop(self):
        if not self.is_empty():
            return self.lst.pop()
        else:
            return 'Стек пуст'
    def is_empty(self):
        return len(self.lst)==0
    def get_lst(self):
        return tuple(self.lst[::-1])
s = Stack()    
print(s.push('apple'))
print(s.push('banana'))
print(s.get_lst())
print(s.pop())
print(s.pop())
print(s.pop())

#10
class Queue:
    
    def __init__(self):
        self.lst = []
    def enqueue(self,arg):
        self.lst.append(arg)
        return arg
    def dequeue(self):
        if not self.is_empty():
            return self.lst.pop(0)
        else:
            return 'Стек пуст'
    def is_empty(self):
        return len(self.lst)==0
s = Queue()    
print(s.enqueue('apple'))
print(s.enqueue('banana'))
print(s.dequeue())
print(s.dequeue())
print(s.dequeue())

class Bank:
    def __init__(self):
        self.account = {}
    def add_account(self, name:str, balance:float):
        if name in self.account:
            return f"Клиент с именем {name} уже существует"
        self.account[name]=balance
        return f"Счёт для {name} успешно создан с балансом {balance}"
    def deposit(self,name:str,amount:float):
            if name in self.account:
                self.account[name] = self.account[name]+amount
                return f"{amount} успешно добавлено. Новый баланс: {self.account[name]}"
            else:
                 return f"Клиент с именем {name} нет сначала добавьте его"
    def withdraw(self,name:str,amount:float):
            try:
                if self.account[name]>=amount:
                    self.account[name] = self.account[name]-amount
                    return f"{amount} успешно снято. Остаток: {self.account[name]}"
                elif self.account[name]< amount:
                    return f'Не достаточно денег в балансе баланс {self.account[name]}'
                else:
                    return f"Клиент с именем {name} уже существует"
            except KeyError:
                return 'Таким именем не нашелся клиент сначала добавьте'
            except Exception as e:
                return str(e)
    def transfer(self,from_name:str, to_name:str, amount:float):
        if from_name not in self.account or to_name not in self.account:
            return "Один или оба клиента не найдены. Проверьте имена."
        withdraw_result = self.withdraw(from_name,amount)
        if 'успешно снято' in withdraw_result:  
            deposit_result = self.deposit(to_name,amount)
            if 'успешно добавлено' in deposit_result:
                return f'Перевод завершон. {withdraw_result} | {deposit_result}'
            else:
                self.deposit(from_name,amount)
                return f"Перевод не выполнен. {deposit_result}"
        else:
            return f"Перевод не выполнен. {withdraw_result}"
              
    def  get_balance(self,name):
        if name in self.account:
            return f"Баланс клиента {name}: {self.account[name]}"
        else:
            return f"Клиент с именем {name} не найден"  

bank = Bank()
print(bank.add_account("Charlie", 2000))
print(bank.add_account("Bob", 200))
print(bank.add_account("Alice",500))
print(bank.deposit("Charlie", 300))
print(bank.withdraw("Charlie", 0))
print(bank.transfer("Alice", "Bob", 200))
print(bank.get_balance("Charlie"))
print(bank.get_balance("Alice"))
