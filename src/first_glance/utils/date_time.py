from datetime import datetime, timedelta


def generate_date_range(days: int = 365, format: str = "%Y-%m-%d"):

    # Calculate the start date (365 days ago) and current date
    start_date = datetime.now() - timedelta(days=days)
    current_date_str = datetime.now().strftime(format=format)
    start_date_str = start_date.strftime(format)

    return start_date_str, current_date_str
