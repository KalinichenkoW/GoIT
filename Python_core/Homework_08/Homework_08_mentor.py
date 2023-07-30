from datetime import datetime, timedelta, date

users = [
    {"Oleksander": "06.08.1996"},
    {"Lada": "03.08.1976"},
    {"Mariy": "02.08.2007"},
    {"Sergey": "30.07.2000"},
    {"Victoria": "31.07.1999"},
    {"Nataliy": "29.07.2007"},
    {"Volodymyr": "04.08.1975"},
    {"Євген": "01.08.2005"},
    {"Олег": "03.08.2001"},
    {"Олена": "05.08.1998"},
    {"Віктор": "06.08.2003"},
]
days_name = {
    0: {"weekday": "понеділок", "date": None, "users": []},
    1: {"weekday": "вівторок", "date": None, "users": []},
    2: {"weekday": "середа", "date": None, "users": []},
    3: {"weekday": "четвер", "date": None, "users": []},
    4: {"weekday": "ятниця", "date": None, "users": []},
    5: {"weekday": "субота", "date": None, "users": []},
    6: {"weekday": "неділя", "date": None, "users": []},
}


def get_birthdays_per_week(users):
    current_date = date.today()
    num_week = current_date.weekday()
    start_next_week = current_date + timedelta(days=7 - num_week - 2)
    # список дат з наступного починаючи з суботи добавимо до days_name
    for a in range(7):
        a_dates_week = start_next_week + timedelta(days=a)
        days_name[a_dates_week.weekday()]["date"] = a_dates_week

    for user in users:
        name, birtday = user.popitem()
        user_dey_сurrent_year = (
            datetime.strptime(birtday, "%d.%m.%Y")
            .replace(year=current_date.year)
            .date()
        )
        num_week_dey = user_dey_сurrent_year.weekday()

        if days_name[num_week_dey]["date"] == user_dey_сurrent_year:
            if num_week_dey in [5, 6]:
                num_week_dey = 0
            days_name[num_week_dey]["users"].append(name)

    print("Будь ласка, привітайте з Днем народження у")
    for data in days_name.values():
        if data["users"]:  # порожній список/словник/кортеж/cтрока завжди False
            print(f"{data['weekday']}: {', '.join(data['users'])}")


get_birthdays_per_week(users)
