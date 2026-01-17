import pandas as pd
from tabulate import tabulate

# --- 1. Load the Data ---
try:
    df = pd.read_csv('Sample - Superstore.csv', encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')

# --- 2. Data Cleaning ---

# Remove unnecessary columns
if 'Row ID' in df.columns:
    df = df.drop(columns=['Row ID'])

# Handle Date Formats
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Remove Duplicates
original_rows = len(df)
df = df.drop_duplicates()
print(f"Removed {original_rows - len(df)} duplicate rows.")

# --- 3. Feature Engineering ---
df['Order Year'] = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month_name()
# Profit Margin Calculation (Safe division)
df['Profit Margin'] = df.apply(lambda row: (row['Profit'] / row['Sales']) if row['Sales'] > 0 else 0, axis=1)

# --- 4. Display Results with Tabulate ---

# A. Data Overview (First 5 rows)


# B. Missing Values Summary
missing_data = df.isnull().sum().reset_index()
missing_data.columns = ['Column Name', 'Missing Values']
missing_data = missing_data[missing_data['Missing Values'] > 0]

if not missing_data.empty:
    print("\n--- Missing Values ---")
    print(tabulate(missing_data, headers='keys', tablefmt='psql', showindex=False))
else:
    print("\n--- No Missing Values Found ---")

# C. Dataset Key Statistics (Mean, Min, Max)
stats = df[['Sales', 'Quantity', 'Profit', 'Profit Margin']].describe().reset_index()
print("\n--- Key Statistics ---")
print(tabulate(stats, headers='keys', tablefmt='fancy_grid', showindex=False))

# Save the file
df.to_csv('Cleaned_Superstore_Data.csv', index=False)