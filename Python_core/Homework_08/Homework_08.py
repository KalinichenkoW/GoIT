from datetime import datetime, timedelta


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
    0: ["понеділок"],
    1: ["вівторок"],
    2: ["середа"],
    3: ["четвер"],
    4: ["п'ятниця"],
    5: ["субота"],
    6: ["неділя"],
}


def get_birthdays_per_week(users):
    # Яка сьогодні дата та час
    current_datetime = datetime.now()

    # порядковий номер ніділі від нуля
    num_week = current_datetime.weekday()

    # тільки дата
    current_date = current_datetime.date()

    # Вираховуємо коли початок наступного тижня з початку суботи
    start_next_week = current_date + timedelta(days=7 - num_week - 2)

    # Поточний рік
    сurrent_year = current_datetime.strftime("%Y")

    # список дат з наступного починаючи з суботи
    a = 0
    dates_week = []
    while a < 7:
        dates_week.append(start_next_week + timedelta(days=a))
        a_dates_week = start_next_week + timedelta(days=a)
        days_name[a_dates_week.weekday()].append(a_dates_week)
        a += 1

    for i in users:
        for name, birthday in i.items():
            user_dey = datetime.strptime(birthday, "%d.%m.%Y")
            user_dey_сurrent_year = user_dey.date().strftime(f"{сurrent_year}-%m-%d")
            user_dey_сurrent_year = datetime.strptime(user_dey_сurrent_year, "%Y-%m-%d")
            num_week_dey = user_dey_сurrent_year.weekday()

            if days_name[num_week_dey][1] == user_dey_сurrent_year.date():
                if num_week_dey > 0 and num_week_dey <= 4:
                    days_name[num_week_dey].append(name)
                else:
                    days_name[0].append(name)

    print("Будь ласка, привітайте з Днем народження у")

    for i, v in days_name.items():
        if v[2:] != []:
            print(f"{days_name[i][0]}: {', '.join(v[2:])}")
        if i > 3:
            break


get_birthdays_per_week(users)
