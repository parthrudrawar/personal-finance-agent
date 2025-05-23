import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from modules import expense_tracker


def test_load_transactions():
    file_path = 'test_transactions.csv'
    df = expense_tracker.load_transactions(file_path)
    assert isinstance(df, pd.DataFrame)
    assert 'Date' in df.columns
    assert 'Description' in df.columns
    assert 'Amount' in df.columns
    
def load_categories_expenses():
    df = pd.DataFrame({
        'description': ['Uber ride', 'Restaurant bill', 'Rent for May', 'Book purchase'],
        'amount': [15, 30, 1000, 20]
    })
      
    file_path = 'test_transactions.csv'
    df = expense_tracker.load_transactions(file_path)
    df = expense_tracker.categorize_expenses(df)
    assert 'Category' in df.columns
    assert df.loc[0, 'Category'] == 'Transportation'
    assert df.loc[1, 'Category'] == 'Food'
    assert df.loc[2, 'Category'] == 'Rent'
    assert df.loc[3, 'Category'] == 'Entertainment'
    assert df.loc[4, 'Category'] == 'Other'
    
    df = expense_tracker.sum_expenses_by_category(df)
    assert 'Category' in df.columns
    assert 'Amount' in df.columns
    
    return df

def test_sum_expenses_by_category():
    df = pd.DataFrame({
        'category': ['Transport', 'Dining', 'Rent', 'Other'],
        'amount': [15, 30, 1000, 20]
    })
    summary = expense_tracker.summarize_expenses(df)
    assert summary['amount'].sum() == 1065
    assert 'category' in summary.columns
    
    return df
