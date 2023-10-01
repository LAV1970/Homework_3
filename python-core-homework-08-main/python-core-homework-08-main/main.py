from datetime import date, timedelta, datetime
from collections import defaultdict


start_date = date.today()
end_date = start_date + timedelta(7)


def get_period(start_date: date, days: int):  # функция периода всех дат от текущей ,
    # дельтой 7 дней, на выходе словарь {(число,дата):тек.год}
    result = {}
    for _ in range(days + 1):
        result[start_date.day, start_date.month] = start_date.year
        start_date += timedelta(1)

    return result


def get_birthdays_per_week(users: list) -> list:
    # res = {"Monday" : [], "Tuesday" : [], "Wednesday" : [], "Thursday" : [], "Friday" : []}
    res = defaultdict(list)

    start_date = date.today()
    period = get_period(start_date, 7)

    # end_date = start_date + timedelta(7)
    if not users:
        res = {}
        return res

    for user in users:
        bd: date = user["birthday"]
        date_bd = bd.day, bd.month

        if date_bd in list(period):
            date_bd_week = bd.replace(
                year=period[date_bd]
            )  # замена в ДР года из периода

            bd__weekday = date_bd_week.weekday()

            if bd__weekday in (5, 6):
                res["Monday"].append(user["name"])
            else:
                res[date_bd_week.strftime("%A")].append(user["name"])

    return res


if __name__ == "__main__":
    users = [
        {"name": "Bill", "birthday": date(1990, 9, 1)},
        {"name": "Marry", "birthday": date(2000, 10, 2)},
        {"name": "John", "birthday": date(2003, 10, 5)},
        {"name": "Jack", "birthday": date(2005, 10, 1)},
    ]
    result = get_birthdays_per_week(users)

    print(result)
    # Виводимо результат

    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
    get_period(start_date, 7)
