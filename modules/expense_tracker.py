import pandas as pd
def load_transactions(file_path):
    df = pd.read_csv(file_path)
    return df
def categorize_expenses(df):
    
    def categorize(description):
        description = description.lower()
        
        if 'groceries' in description or 'supermarket' in description:
            return 'Groceries'
        elif 'restaurant' in description or 'dining' in description:
            return 'Restaurants'
        elif 'gas' in description:
            return 'Gas'
        elif 'entertainment' in description or 'movie' in description or 'theater' in description:
            return 'Entertainment'
        elif 'transportation' in description or 'bus' in description or 'car' in description:
            return 'Transportation'
        elif 'health' in description or 'doctor' in description or 'pharmacy' in description:
            return 'Health'
        elif 'clothing' in description or 'shoes' in description or 'dress' in description:
            return 'Clothing'
        else:
            return 'Other'
        
    df['Category'] = df['Description'].apply(categorize)
        
    return df


def sum_expenses_by_category(df):
    expenses_by_category = df.groupby('Category')['Amount'].sum().reset_index()
    return expenses_by_category