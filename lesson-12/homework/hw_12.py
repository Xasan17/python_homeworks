#1
import threading

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime(start, end, result_list):
    primes = [num for num in range(start, end) if is_prime(num)]
    result_list.extend(primes)  # Добавляем найденные числа в общий список

def main(start, end):
    result = []

    # Потоки будут записывать в общий список
    thread1 = threading.Thread(target=check_prime, args=(start, (start+end)//2, result))
    thread2 = threading.Thread(target=check_prime, args=((start+end)//2, end, result))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    return sorted(result)

# Пример использования:
if __name__ == "__main__":
    primes = main(1, 100)
    print("Простые числа:", primes)
#2
import threading
from collections import Counter
import re

# Глобальный словарь для результатов
final_result = Counter()
lock = threading.Lock()

def read_file_lines(filename):
    """Читает строки файла и возвращает список строк"""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

def count_words(lines):
    """Подсчет слов в списке строк"""
    words = re.findall(r'\b\w+\b', ' '.join(lines).lower())
    return Counter(words)

def worker(lines):
    """Функция для потока — считает слова и добавляет в итог"""
    local_result = count_words(lines)
    with lock:
        final_result.update(local_result)

def main(filename, num_threads=4):
    lines = read_file_lines(filename)
    chunk_size = len(lines) // num_threads
    threads = []

    for i in range(num_threads):
        start = i * chunk_size
        # Последний поток обрабатывает до конца
        end = (i + 1) * chunk_size if i != num_threads - 1 else len(lines)
        t = threading.Thread(target=worker, args=(lines[start:end],))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Выводим 10 самых частых слов
    print("Top 10 most frequent words:")
    for word, count in final_result.most_common(10):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main('big_text_file.txt')  # Замените на ваш путь к файлу
