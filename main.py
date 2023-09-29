from datetime import date, datetime, timedelta
from collections import defaultdict


def get_period(start_date: date, days: int):
    result = {}
    for _ in range(days+1):
        result[start_date.day, start_date.month] = start_date.year
        start_date += timedelta(1)
    return result


def get_birthdays_per_week(users):
    if not users:
        return None
    result = defaultdict([])
    start_date = date.today()
    period = get_period(start_date, 7)
    for i in users:
        bd = i["birthday"]
        date_bd = bd.day, bd.month
        if date_bd in list(period):
            if 
    if result:
        return result
    else:
        None


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
