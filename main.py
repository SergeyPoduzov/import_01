from datetime import datetime

from aplication.salary import calculate_salary


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    current_datetime = datetime.now()
    print("Текущая дата и время: ",current_datetime)
    current_date = datetime.now().date()
    print("Текущая дата: ", current_date)

    print("\nВывод отдельных атрибут:")
    print("год: ", current_datetime.year)  # 2019
    print("месяц: ",current_datetime.month)  # 12
    print("день: ",current_datetime.day)  # 13
    print("часы: ",current_datetime.hour)  # 12
    print("минуты: ",current_datetime.minute)  # 18
    print("секунды: ",current_datetime.second)  # 18
    print("Микросекунды: ",current_datetime.microsecond)  # 290623

    print("Общая сумма заработной платы в рублях: ", calculate_salary())