from datetime import datetime, date

def get_days_from_today(date_string):
    try:
        given_date = datetime.strptime(date_string, "%Y-%m-%d").date()

        today = date.today()

        difference = today - given_date

        return difference.days

    except ValueError:
        return "Error: Plese enter the date in the correct formate YYYY-MM-DD"


