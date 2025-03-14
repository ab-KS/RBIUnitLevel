import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

salaried = ['Financial sector employees','Self-Employed']
unorganized_workers = ['Daily workers']
retired = ['Retired persons']
homemaker = ['HOMEMAKER', 'Homemaker']
others = ['Other category', 'Other employees']

def classify_respondent(category):
    if category in salaried:
        return 'Employed'
    elif category in unorganized_workers:
        return 'Unorganized Workers'
    elif category in retired:
        return 'Retired'
    elif category in homemaker:
        return 'Homemaker'
    else:
        return 'Others'
year = 2008
df = pd.read_csv(fr'RBIUnitLevel\Data_{year}.csv')
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

df['Respondent_Category'] = df['Category of Respondent'].apply(classify_respondent)

# Save the modified file
df.to_csv(fr'RBIUnitLevel\Data_{year}_categorized.csv', index=False)

# Display sample output
print(df[['Category of Respondent', 'Respondent_Category']].head())