from datetime import date


def get_next_date(month, day):
    today = date.today()

    current_month = today.month
    current_day = today.day

    if current_month <= month and current_day <= day:
        year = today.year
    else:
        year = today.year + 1

    return date(year, month, day)
