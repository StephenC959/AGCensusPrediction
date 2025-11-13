#link to NASS database https://www.nass.usda.gov/datasets/

import pandas as pd
import gzip
import os

# List of NASS Census files to combine
files = [
    "qs.census2022.txt.gz",
    "qs.census2017.txt.gz",
    "qs.census2012.txt.gz"
]

# Initialize an empty list to hold filtered DataFrames
dfs = []

for file_path in files:
    if not os.path.exists(file_path):
        print(f"⚠️ Skipping missing file: {file_path}")
        continue

    print(f"📂 Processing: {file_path}")

    # Open and read the compressed file
    with gzip.open(file_path, mode='rt', encoding='utf-8') as f:
        df = pd.read_csv(f, sep='\t', low_memory=False)

    # Filter for Texas only (case-insensitive)
    df_tx = df.loc[df['STATE_NAME'].str.upper() == 'TEXAS'].copy()

    # Add a "CENSUS_YEAR" column (in case not included)
    if 'YEAR' in df_tx.columns:
        df_tx['CENSUS_YEAR'] = df_tx['YEAR']
    else:
        # Extract from filename as fallback
        year = ''.join(filter(str.isdigit, file_path))
        df_tx['CENSUS_YEAR'] = year

    # Convert numeric columns safely
    numeric_cols = df_tx.select_dtypes(include=['int64', 'float64']).columns
    df_tx.loc[:, numeric_cols] = df_tx[numeric_cols].astype(float)

    # Append to list
    dfs.append(df_tx)

# Combine all years into one DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Save as a single CSV
output_file = "Texas_AgCensus_2012_2017_2022.csv"
combined_df.to_csv(output_file, index=False)

print(f"\n✅ Combined CSV saved as: {output_file}")
print(f"📊 Total rows: {len(combined_df):,}")

