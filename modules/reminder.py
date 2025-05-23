import json
from datetime import datetime, timedelta

def load_bills(config_path):
    #Load bills from JSON file.
    with open(config_path, 'r') as f:
        bills = json.load(f)
    return bills

def check_bill_reminders(bills, window_days=7):
    #Return bills due within next window_days.
    today = datetime.today().date()
    upcoming = []
    for bill in bills:
        due_date = datetime.strptime(bill['due_date'], '%Y-%m-%d').date()
        if 0 <= (due_date - today).days <= window_days:
            upcoming.append(bill)
    return upcoming

