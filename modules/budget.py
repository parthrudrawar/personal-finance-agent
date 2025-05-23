def create_budget(categories,income):
    default_percentage={
        'Rent':30,
        'Grcoceries':20,
        'Entertainment':10,
        'Transportation':10,
        'Health':5,
        'Clothing':5
        }
    budget={}
    
    for cat in categories:
        percent = default_percentage.get(cat, 5)  # default 5%
        budget[cat] = round(income * percent / 100, 2)
    return budget


def check_budget(budget,spent):
    report = {}
    
    for cat in budget:
        spent = spent.get(cat, 0)
        report[cat] = {
            'budgeted': budget[cat],
            'spent': spent,
            'difference': budget[cat] - spent,
            'status': 'Under' if spent <= budget[cat] else 'Over'
        }
    return report