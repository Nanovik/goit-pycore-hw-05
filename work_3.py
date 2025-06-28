from collections import Counter
from pathlib import Path
import sys

# Створюємо функцію для парсингу рядків логу
def parse_log_line(line: str):
    parse_log = []
    line_list = line.split()
    parse_log.append(line_list[2])
    parse_log.append(' '.join(line_list).replace(line_list[2], "-"))    
    return parse_log

# Створюємо функцію для завантаження логів з файлу
def load_logs(file_path: str) -> list:
    with open(file_path, "r") as file:
        lines = [el.strip() for el in file.readlines()]
    return lines

# Створюємо функцію для фільтрації логів за рівнем
def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda x: x[0] == level, logs))

# Створюємо функцію dict для підрахунку записів за рівнем логування
def count_logs_by_level(logs: list):
    return Counter([parse_log_line(line)[0] for line in logs])

# Створюємо функцію, яка представляє результати у вигляді таблиці з кількістю записів для кожного рівня
def display_log_counts(counts: dict):
    print(f'{"-"*20:^20}|{"-"*12:^10}')
    print(f'{"Рівень логування":^20}|{"Кількість":^12}')
    print(f'{"-"*20:^20}|{"-"*12:^10}')
    for i in counts:
        print(f'{i:<20}| {counts.get(i):<10}')
    print(f'{"-"*20:^20}|{"-"*12:^10}')

def main():
    path_str, loger = "", ""
    if len(sys.argv) <=1:
        print("Недостатньо параметрів")
    else:
        if len(sys.argv) > 2:
            loger = sys.argv[2].upper()
        path_str = Path(sys.argv[1])
        if path_str.exists():
            logers_line = load_logs(path_str)
            parse_log = [parse_log_line(line) for line in logers_line]
            display_log_counts(count_logs_by_level(logers_line))
            if loger:
                filter_logs = filter_logs_by_level(parse_log, loger)
                if filter_logs:
                    print(f"\nДеталі логів для рівня {loger}:")
                    for i in filter_logs:
                        print(i[1])
                else:
                    print(f"\nДля рівня {loger} логів нема:")
        else:
            print("Файл не знайдено")

if __name__ == "__main__":
    main()