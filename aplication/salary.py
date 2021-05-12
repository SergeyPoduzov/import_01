from aplication.db.people import get_employees


def calculate_salary():
    print("Функуия подчета заработной платы")
    n=100
    people=get_employees()
    salary = n*people
    return salary