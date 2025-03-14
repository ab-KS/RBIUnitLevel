import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
year = 2008
df = pd.read_csv(fr'Data_{year}.csv')
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

#print(df.head())
# print(df.shape)
# features = df.columns
# for i in features:
#     print(i)

# Set style
sns.set_style("whitegrid")

# Plot 1: Distribution of Current Inflation Perception
plt.figure(figsize=(10, 5))
sns.countplot(y=df["Modified View on Current Inflation Rate"], 
              order=df["Modified View on Current Inflation Rate"].value_counts().index, 
              palette="Blues_r")
plt.xlabel("Count")
plt.ylabel("Inflation Rate Perception")
plt.title("Distribution of Current Inflation Rate Perception")
plt.show()

# # Plot 2: Price Expectations in Next 3 Months (General)
# plt.figure(figsize=(10, 5))
# sns.countplot(y=df["Expectations on prices in next 3 months - General"], 
#               order=df["Expectations on prices in next 3 months - General"].value_counts().index, 
#               palette="coolwarm")
# plt.xlabel("Count")
# plt.ylabel("Price Expectation (3 Months)")
# plt.title("Expectations on Prices in Next 3 Months - General")
# plt.show()

# Plot 3: Inflation Perception by Age Group
plt.figure(figsize=(10, 5))
sns.countplot(y=df["Age Group"], hue=df["Modified View on Current Inflation Rate"], palette="viridis")
plt.xlabel("Count")
plt.ylabel("Age Group")
plt.title("Inflation Perception by Age Group")
plt.legend(title="Inflation Rate Perception", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Plot 4: Inflation Perception by Category of Respondent (Employment Proxy)
plt.figure(figsize=(10, 5))
sns.countplot(y=df["Respondent_Category"], hue=df["Modified View on Current Inflation Rate"], palette="mako")
plt.xlabel("Count")
plt.ylabel("Category of Respondent")
plt.title("Inflation Perception by Category of Respondent")
plt.legend(title="Inflation Rate Perception", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Plot 5: Price Expectations Across Different Categories
# price_cols = ["Expectations on prices in next 3 months - Food products", 
#               "Expectations on prices in next 3 months - Non food products", 
#               "Expectations on prices in next 3 months - Services"]

# price_data = pd.melt(df[price_cols], var_name="Category", value_name="Expectation")
# plt.figure(figsize=(10, 5))
# sns.countplot(y=price_data["Category"], hue=price_data["Expectation"], palette="coolwarm")
# plt.xlabel("Count")
# plt.ylabel("Price Category")
# plt.title("Price Expectations Across Different Categories")
# plt.legend(title="Expectation", bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.show()

# Plot 6: Inflation Perception by City Name (Regional Proxy)
plt.figure(figsize=(10, 5))
sns.countplot(y=df["City_Tier"], hue=df["Modified View on Current Inflation Rate"], palette="rocket")
plt.xlabel("Count")
plt.ylabel("City Tier")
plt.title("Regional Variations in Inflation Perception")
plt.legend(title="Inflation Rate Perception", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


