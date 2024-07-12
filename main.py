import pandas as pd
import matplotlib.pyplot as plt

# Load DataFrame
df = pd.read_csv('my_file.csv',encoding='utf-8')


# Remove non-numeric characters using a regular expression
df["All Time Peak"] = df["All Time Peak"].str.replace('[\$,e\[\]]', '', regex=True)

# Handle missing values by filling them with 0
df["All Time Peak"] = df["All Time Peak"].fillna(0)

# Convert the column to int64
df["All Time Peak"] = df["All Time Peak"].astype(int)

print(df["All Time Peak"].dtype)

# Remove non-numeric characters using a regular expression
df["Peak"] = df["Peak"].str.replace('[\$,ce\[\]]', '', regex=True)

# Handle missing values by filling them with 0
df["Peak"] = df["Peak"].fillna(0)
df["Peak"] = df["Peak"].astype(int)

df["Ref."] = df["Ref."].str.replace('[\$,ce\[\]]', '', regex=True)
df["Ref."] = df["Ref."].replace('d', 0)
df["Ref."] = df["Ref."].astype(int)

df["Actual gross"] = df["Actual gross"].str.replace('[\:$,e\[d\]bc]', '', regex=True)
df["Actual gross"] = df["Actual gross"].astype(int)

df["Tour title"] = df["Tour title"].str.replace('[\$\*\+\†\[\]‡]', '', regex=True)
df["Tour title"] = df["Tour title"].astype(str)


df["Adjusted gross (in 2022 dollars)"] = df["Adjusted gross (in 2022 dollars)"].str.replace('[\:$,e\[d\]bc]', '', regex=True)
df["Adjusted gross (in 2022 dollars)"] = df["Adjusted gross (in 2022 dollars)"].astype(int)
print(df)

plt.figure(figsize=(12, 6))
plt.bar(df['Artist'], df['Adjusted gross (in 2022 dollars)'])
plt.xlabel('Artist')
plt.ylabel('Adjusted gross (in 2022 dollars)')
plt.title('Top 10 Artists by Adjusted Gross in 2022 Dollars')
plt.xticks(rotation=90)  # Rotate artist names for better readability
plt.show()