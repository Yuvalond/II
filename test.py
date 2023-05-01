from datetime import datetime, timedelta

def get_mondays_of_quarter(quarter):
    year = int(quarter.split()[-1])
    quarter_num = int(quarter.split()[0])
    if quarter_num == 1:
        start_date = datetime(year, 1, 1)
    elif quarter_num == 2:
        start_date = datetime(year, 4, 1)
    elif quarter_num == 3:
        start_date = datetime(year, 7, 1)
    elif quarter_num == 4:
        start_date = datetime(year, 10, 1)
    else:
        return []
    end_date = start_date + timedelta(days=91)
    monday_dates = []
    while start_date <= end_date:
        if start_date.weekday() == 0: # если это понедельник
            monday_dates.append(start_date.strftime('%d/%m/%Y'))
        start_date += timedelta(days=1)
    return monday_dates



print(get_mondays_of_quarter("2 квартал 2022"))

