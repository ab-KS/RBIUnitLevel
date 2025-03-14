import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def map_interest_rate(rate):
    if pd.isna(rate):  
        return np.nan  
    if rate.startswith('<'):  # Cases like '<1'
        return 0
    elif rate.startswith('>=') or rate.startswith('>'):  # Cases like '>=16' # or rate.startswith('>')
        return 16
    else:  # Ranges like '5-6'
        
        print(float(rate.split('-')[0]))
        return float(rate.split('-')[0])  # Take the lower bound
        # except Exception as e:
        #     return 'Missing'

year = 2008
df = pd.read_csv(fr'RBIUnitLevel\Data_{year}.csv')
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

df['Numeric_Rate'] = df["View on Current Inflation Rate"].apply(map_interest_rate)

bins = np.arange(0, 25, 5)  # [0-5], [5-10], [10-15], [15-20]
labels = [f"{bins[i]}-{bins[i+1]}" for i in range(len(bins)-1)]

# print(bins)
# print(labels)

df['New_Bin'] = pd.cut(df['Numeric_Rate'], bins=bins, labels=labels, include_lowest=True, right=False)
# print(df["View on Current Inflation Rate"].unique())
df.to_csv(fr'RBIUnitLevel\Data_{year}_irc.csv', index=False)

print(df[['View on Current Inflation Rate', 'New_Bin']].head())