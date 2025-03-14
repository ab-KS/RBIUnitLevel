import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define city tiers
tier_1 = ['Ahmedabad', 'Bangalore', 'Bengaluru', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai']
tier_2 = ['Bhopal', 'Bhubaneswar', 'Chandigarh', 'Guwahati', 'Jaipur', 'Jammu', 'Lucknow', 'Nagpur', 'Patna', 'Raipur', 'Ranchi', 'Thiruvananthapuram']

# Function to classify cities
def classify_city(city):
    if city in tier_1:
        return 'Tier 1'
    elif city in tier_2:
        return 'Tier 2'
    else:
        return 'Tier 3'
year = 2024
df = pd.read_csv(fr'RBIUnitLevel\Data_{year}.csv')
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

# Add a new column 'City_Tier'
df['City_Tier'] = df['City Name'].apply(classify_city)

# Save the modified file
df.to_csv(fr'RBIUnitLevel\Data_{year}.csv', index=False)

# Display sample output
print(df[['City Name', 'City_Tier']].head())

# print(df['City Name'].unique())