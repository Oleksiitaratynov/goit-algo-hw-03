import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.datetime.today()
        days_difference = (current_date - input_date).days
        
        return days_difference
    except ValueError:
        return "Неправильний формат дати. Введіть дату у форматі 'РРРР-ММ-ДД'."

today = datetime.datetime.today().strftime('%Y-%m-%d')
example_date = "2023-10-09"
result = get_days_from_today(example_date)
print(f"Різниця між {example_date} та {today}: {result} днів")
