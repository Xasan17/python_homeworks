#1
from datetime import datetime 
class Tasks:
    def __init__(self,title:str, description:str, due_date:datetime.date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = False
    
    def __str__(self):
        return f'Имя задачи {self.title}. Нужно сделать это {self.description}. Крайний срок {self.due_date}. Статус задачи {'✅' if self.status else '❌'}'
    
    def mark_complete(self):
        self.status=True
    def mark_incomplete(self):
        self.status=False
    def is_completed(self):
        if self.status:
            return 'Задания завершена'
        else:
            return 'Задания еще не завершена'
class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self,task):
        for existing_task in self.tasks:
            if existing_task.title ==task.title:
               return 'We have this task' 
        self.tasks.append(task)
        return 'Succesfully added'
    def mark_task_complete(self,index):
        if 1 <= index <= len(self.tasks):
            task = self.tasks[index-1]                
            task.mark_complete()
            return 'Succesfully changed'
        else:
            return f'We do not have this {index}'
    def list_all_tasks(self):
        result=[]
        for item,existing_task in enumerate(self.tasks,start=1):
            result.append(f'{item} task: {existing_task}')
        return '\n'.join(result)
    def list_incomplete_tasks(self):
        result = []
        for existing_task in self.tasks:
            if existing_task.status == False:
                result.append(str(existing_task))
        return '\n'.join(result)

def main():
    todo_list = ToDoList()

    while True:
        print("\n--- Меню ---")
        print("1. Добавить задачу")
        print("2. Отметить задачу как завершённую")
        print("3. Показать все задачи")
        print("4. Показать только незавершённые задачи")
        print("0. Выход")

        choice = input("Выберите действие: ")
        if choice == "1":
            name = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")
            due_date = input("Введите срок выполнения (например: 2025-06-10): ")
            task = Task(name, description, due_date)
            print(todo_list.add_task(task))

        elif choice == "2":
            try:
                index = int(input("Введите номер задачи для завершения: "))
                print(todo_list.mark_task_complete(index))
            except ValueError:
                print("Ошибка: Введите корректное число.")

        elif choice == "3":
            print("\n--- Все задачи ---")
            print(todo_list.list_all_tasks())

        elif choice == "4":
            print("\n--- Незавершённые задачи ---")
            print(todo_list.list_incomplete_tasks())

        elif choice == "0":
            print("Выход из программы. До свидания!")
            break

        else:
            print("Неверный ввод. Пожалуйста, выберите действие от 0 до 4.")

if __name__ == "__main__":
    main()


#2
class Post:
    def __init__(self, title,content,author):
        self.title = title
        self.content = content
        self.author = author
    def __str__(self):
        return f'Название {self.title}. Контент {self.content}. Автор: {self.author}.'
class Blog:
    def __init__(self):
        self.posts = []
    def add_post(self, post):
        for exist_post in self.posts:
            if exist_post.title == post.title:
                return 'Такой пост уже есть'
        self.posts.append(post)
        return 'Succesfully added'
    def list_all_posts(self):
        result = []
        for item,post in enumerate(self.posts, start=1):
            result.append(f'{item}: {post}')
        return '\n'.join(result)
    def get_posts_by_author(self,author_name):
        result = []
        for post in self.posts:
            if post.author == author_name:
                result.append(post)
        if result==[]:
            return 'Нет поста таким автором'
        return '\n'.join(result) 
    def delete_post(self, title):
        for post in self.posts:
            if post.title == title:
                self.posts.remove(post)
                return f'Пост "{title}" удалён.'
        return 'Пост не найден.'
    def edit_post(self, title, new_title=None, new_content=None):
        for post in self.posts:
            if post.title == title:
                if new_title:
                    post.title = new_title
                if new_content:
                    post.content = new_content
                return 'Пост успешно отредактирован.'
        return 'Пост не найден.'
    def get_latest_posts(self, n=3):
        if not self.posts:
            return 'Нет постов'
        latest = self.posts[-n:]
        return '\n\n'.join(str(post) for post in reversed(latest))
          
def main():
    blog = Blog()

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Добавить пост")
        print("2. Показать все посты")
        print("3. Показать посты по автору")
        print("4. Удалить пост")
        print("5. Редактировать пост")
        print("6. Показать последние посты")
        print("0. Выйти из программы")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите заголовок поста: ")
            content = input("Введите содержание поста: ")
            author = input("Введите имя автора: ")
            post = Post(title, content, author)
            print(blog.add_post(post))

        elif choice == "2":
            print("\n--- Все посты ---")
            print(blog.list_all_posts())

        elif choice == "3":
            author_name = input("Введите имя автора: ")
            print("\n--- Посты автора ---")
            print(blog.get_posts_by_author(author_name))

        elif choice == "4":
            title = input("Введите заголовок поста для удаления: ")
            print(blog.delete_post(title))

        elif choice == "5":
            title = input("Введите заголовок поста для редактирования: ")
            new_title = input("Введите новый заголовок (оставьте пустым, если не менять): ")
            new_content = input("Введите новое содержание (оставьте пустым, если не менять): ")
            new_title = new_title if new_title.strip() else None
            new_content = new_content if new_content.strip() else None
            print(blog.edit_post(title, new_title, new_content))

        elif choice == "6":
            try:
                n = int(input("Сколько последних постов показать? "))
                print(blog.get_latest_posts(n))
            except ValueError:
                print("Введите корректное число.")

        elif choice == "0":
            print("Выход из программы. До свидания!")
            break

        else:
            print("Неверный ввод. Введите число от 0 до 6.")

if __name__ == "__main__":
    main()

#3
class Account:
    def __init__(self,number, name, balance):
        self.number = number
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Пополнено на {amount}. Баланс: {self.balance}"
        return "Сумма пополнения должна быть положительной"

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f"Снято {amount}. Баланс: {self.balance}"
            else:
                return "Недостаточно средств"
        return "Сумма снятия должна быть положительной"
    def __str__(self):
        return f'Счет: {self.number}. /nИмя пользователя {self.name}. \nБаланс {self.balance}'

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        for existing_account in self.accounts:
            if existing_account.number == account.number:
                return "Счёт с таким номером уже существует"
        self.accounts.append(account)
        return f"Счёт {account.number} создан"

    def get_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            return f"Баланс счета {account_number}: {account.balance}"
        return "Счёт не найден"

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            return account.deposit(amount)
        return "Счёт не найден"

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            return account.withdraw(amount)
        return "Счёт не найден"

    def transfer(self, from_number, to_number, amount):
        from_account = self.find_account(from_number)
        to_account = self.find_account(to_number)
        
        if from_account and to_account:
            withdrawal_response = from_account.withdraw(amount)
            if "Снято" in withdrawal_response:
                to_account.deposit(amount)
                return f"Перевод {amount} с {from_number} на {to_number} выполнен"
            return withdrawal_response
        return "Один из счётов не найден"

    def show_account_details(self, account_number):
        account = self.find_account(account_number)
        if account:
            return str(account)
        return "Счёт не найден"

    def find_account(self, account_number):
        for account in self.accounts:
            if account.number == account_number:
                return account
        return None
def main():
    bank = Bank()

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Добавить счёт")
        print("2. Показать баланс")
        print("3. Пополнить счёт")
        print("4. Снять деньги")
        print("5. Перевести деньги")
        print("6. Показать информацию о счёте")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            number = input("Введите номер счёта: ")
            name = input("Введите имя владельца: ")
            balance = float(input("Введите начальный баланс (по умолчанию 0): ") or 0)
            account = Account(number, name, balance)
            print(bank.add_account(account))

        elif choice == "2":
            number = input("Введите номер счёта: ")
            print(bank.get_balance(number))

        elif choice == "3":
            number = input("Введите номер счёта: ")
            amount = float(input("Введите сумму для пополнения: "))
            print(bank.deposit(number, amount))

        elif choice == "4":
            number = input("Введите номер счёта: ")
            amount = float(input("Введите сумму для снятия: "))
            print(bank.withdraw(number, amount))

        elif choice == "5":
            from_number = input("Введите номер исходного счёта: ")
            to_number = input("Введите номер целевого счёта: ")
            amount = float(input("Введите сумму для перевода: "))
            print(bank.transfer(from_number, to_number, amount))

        elif choice == "6":
            number = input("Введите номер счёта: ")
            print(bank.show_account_details(number))

        elif choice == "0":
            print("Выход из программы. До свидания!")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите число от 0 до 6.")

if __name__ == "__main__":
    main()

