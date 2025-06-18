import json
import requests
import urllib3
import os
import random
#1
def import_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f'file not found')
    except json.JSONDecodeError:
        print(f'error text is not json')
d1 = import_json("students.json")
print(d1)
#2
url = r'https://api.openweathermap.org/data/2.5/find?q=Toshkent&appid=5796abbde9106b7da4febfae8c44c232&units=metric'
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
weather = requests.get(url, verify=False)
d1 = weather.json()
city = d1['list'][0]
main = city['main']
weather = city['weather'][0]
wind = city['wind']

print(f"📍 Город: {city['name']}, {city['sys']['country']}")
print(f"🌡 Температура: {main['temp']}°C")
print(f"🌡 Ощущается как: {main['feels_like']}°C")
print(f"💧 Влажность: {main['humidity']}%")
print(f"🧭 Давление: {main['pressure']} гПа")
print(f"🌬 Ветер: {wind['speed']} м/с, направление {wind['deg']}°")
print(f"🌤 Погода: {weather['main']} ({weather['description']})")
#3
file_path = "books.json"
def load_books():
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding='utf-8') as f:
        return json.load(f)
def save_books(books):
    with open(file_path,"w", encoding="utf-8") as f:
        json.dump(books,f,indent=4, ensure_ascii=False)
def add_book():
    books = load_books()
    new_id = max([b["id"] for b in books],default=0)+1
    title = input("Название книги: ")
    author = input("Автор: ")
    year = int(input("Год: "))
    books.append({"id": new_id, "title": title, "author": author, "year": year})
    save_books(books)
    print('Книга добавлена.')

def update_book():
    books = load_books()
    book_id = int(input("Введите ID книги для обновления: "))
    for book in books:
        if book["id"]==book_id:
            book["title"] = input(f"Новое название если нехотите можете пропустить  ({book['title']}): ") or book["title"]
            book["author"] = input(f"Новый автор если нехотите можете пропустить   ({book['author']}): ") or book["author"]
            book["year"] = int(input(f"Новый год если нехотите можете пропустить  ({book['year']}): ") or book["year"])
            save_books(books)
            print("Книга обновлена.")
            return
    print("Книга с таким ID не найдена.")
def delete_book():
    books = load_books()
    book_id = int(input("Введите ID книги для удаления: "))
    books = [b for b in books if b["id"]!=book_id]
    save_books(books)
    print("Книга удалена (если была).")
    return
def show_books():
    books = load_books()
    if not books:
        print("Книг пока нет.")
        return
    for book in books:
        print(f"ID: {book['id']} | {book['title']} by {book['author']} ({book['year']})")

def main_books():
        while True:
            print("\n📚 Меню:")
            print("1. Показать книги")
            print("2. Добавить книгу")
            print("3. Обновить книгу")
            print("4. Удалить книгу")
            print("0. Выход")
            choice = input("Выберите действие: ")
            if choice == "1":
                show_books()
            elif choice == "2":
                add_book()
            elif choice == "3":
                update_book()
            elif choice == "4":
                delete_book()
            elif choice == "0":
                break
            else:
                print("Неверный выбор.")    

if __name__ == "__main__":
    main_books()
#4
API_KEY = "f1511928" 
def get_movie_by_genre(genre):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&type=movie&s={genre}"
    response = requests.get(url)
    data = response.json()
    if data["Response"] =="True":
        movies = data["Search"]
        random_movie = random.choice(movies)
        print("🎬 Рекомендованный фильм:")
        print(f"Название: {random_movie['Title']}")
        print(f"Год: {random_movie['Year']}")
    else:
        print("Фильмы не найдены. Попробуйте другой жанр.")
    
genre_input = input("Введите жанр (например, action, comedy, drama): ")
get_movie_by_genre(genre_input)
