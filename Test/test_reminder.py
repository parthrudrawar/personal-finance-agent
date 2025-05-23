import tempfile
import json
from modules import reminder

def test_load_bills(tmp_path):
    data = [
        {"name": "Electricity", "due_date": "2025-05-30"},
        {"name": "Water", "due_date": "2025-06-05"}
    ]
    file = " "
    file.write_text(json.dumps(data))

    bills = reminder.load_bills(str(file))
    assert len(bills) == 2

def test_check_bill_reminders():
    bills = [
        {"name": "Electricity", "due_date": "2099-12-31"},
        {"name": "Water", "due_date": "2000-01-01"},
        {"name": "Internet", "due_date": "2100-01-01"}
    ]
    upcoming = reminder.check_bill_reminders(bills, window_days=36500)  # Very large window
    assert len(upcoming) == 3

