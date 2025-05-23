from modules import budget

def test_create_budget():
    cats = ['Rent', 'Groceries', 'Transport', 'Dining', 'Other']
    income = 3000
    bud = budget.create_budget(cats, income)
    assert bud['Rent'] == 900  # 30% of 3000
    assert bud['Groceries'] == 600

def test_check_budget():
    budget_dict = {'Rent': 900, 'Groceries': 600}
    spending = {'Rent': 850, 'Groceries': 650}
    report = budget.check_budget(budget_dict, spending)
    assert report['Rent']['status'] == 'Under'
    assert report['Groceries']['status'] == 'Over'

