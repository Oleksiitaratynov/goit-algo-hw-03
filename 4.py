from datetime import datetime, timedelta

def find_next_weekday(date, weekday):
    days_ahead = weekday - date.weekday()
    if days_ahead <= 0: 
        days_ahead += 7
    return date + timedelta(days_ahead)

def prepare_users(users):
    prepared_users = []  
    for user in users:  
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()  
            prepared_users.append({"name": user['name'], 'birthday': birthday}) 
        except ValueError:
            print(f'Некоректна дата народження для користувача {user["name"]}')  
    return prepared_users

def get_upcoming_birthdays(users, days=7):
    prepared_users = prepare_users(users)
    today = datetime.today().date()  

    upcoming_birthdays = []  
    for user in prepared_users:  
        birthday_this_year = user["birthday"].replace(year=today.year)  

        if birthday_this_year < today:  
            birthday_this_year = birthday_this_year.replace(year=today.year + 1) 

        if 0 <= (birthday_this_year - today).days <= days: 
            if birthday_this_year.weekday() >= 5:  
                birthday_this_year = find_next_weekday(birthday_this_year, 0) 
            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')  
            upcoming_birthdays.append({  
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })
    return upcoming_birthdays

users = [  
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Smith1", "birthday": "1990.03.05"},
    {"name": "Jane Smith1", "birthday": "1990.03.15"},
    {"name": "Jane Smith1", "birthday": "1990.03.11"},
]

print("Список майбутніх днів народження:", get_upcoming_birthdays(users))
