from modules import suggestion

def test_generate_suggestions():
    report = {
        'Rent': {'status': 'Under', 'difference': 50, 'spent': 850, 'budgeted': 900},
        'Dining': {'status': 'Over', 'difference': -20, 'spent': 120, 'budgeted': 100}
    }
    sugg = suggestion.generate_suggestions(report)
    assert any("Reduce spending on Dining" in s for s in sugg)
    assert any("Good job on Rent" in s for s in sugg)
