from datetime import date, datetime, timedelta
from collections import defaultdict


def get_period(start_date: date, days: int) -> dict:
    result = {}
    for _ in range(days+1):
        result[start_date.day, start_date.month] = start_date.year
        start_date += timedelta(1)
    return result


def get_birthdays_per_week(users) -> dict or None:
    if not users:
        return None
    result = defaultdict(list)
    start_date = date.today()
    period = get_period(start_date, 7)
    for i in users:
        bd = i["birthday"]
        date_bd = (bd.month, bd.day)
        if date_bd in period.keys():
            if period[date_bd] == start_date.year:
                result_date = date(period[date_bd], date_bd[1], date_bd[0])
                if result_date.isoweekday() in (6, 7):
                    result["Monday"].append(i["name"])
                else:
                    result[result_date.strftime('%A')].append(i["name"])
    return result


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Bill", "birthday": datetime(1976, 11, 4).date()},
        {"name": "Baba", "birthday": datetime(1976, 11, 7).date()}
    ]

    result = get_birthdays_per_week(users)
    if result:
        print(result)
        # Виводимо результат
        for day_name, names in result.items():
            print(f"{day_name}: {', '.join(names)}")
    else:
        print("No birthdays this week")
