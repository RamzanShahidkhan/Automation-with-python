import pandas as pd

# Reading Excel File
df = pd.read_excel('supermarket_sales.xlsx')

# selecting columns: 'Gender', 'Product line', 'Total'
df = df[['Gender', 'Product line', 'Total']]
# print(df)

# Make pivot table
pivot_table = df.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum').round(0)
# print(pivot_table)

# Export pivot table to Excel file
pivot_table.to_excel('pivot_table.xlsx', 'Report', startrow=4)
