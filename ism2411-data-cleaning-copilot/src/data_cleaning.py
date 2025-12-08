import pandas as pd
import os

# Use absolute path based on script location
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "..", "data", "raw", "sales_data_raw.csv")

#df = pd.read_csv(file_path)

def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

def clean_column_names(df):
    """Standardize column names to lowercase with underscores."""
    # Strip whitespace, remove quotes, and convert to lowercase
    df.columns = (df.columns.str.strip()
                  .str.replace('"', '')
                  .str.lower()
                  .str.replace(' ', '_'))
    
    # Also clean category column values
    if 'category' in df.columns:
        df['category'] = df['category'].astype(str).str.strip().str.replace('"', '')
    
    return df

def handle_missing_values(df):
    """Fill missing values in price and qty columns with mean values."""
    # Clean and convert price to numeric
    if 'price' in df.columns:
        df['price'] = pd.to_numeric(df['price'].astype(str).str.strip().str.replace('"', ''), errors='coerce')
        mean_price = df['price'].mean()
        df['price'] = df['price'].fillna(mean_price)
    
    # Clean and convert qty to numeric
    if 'qty' in df.columns:
        df['qty'] = pd.to_numeric(df['qty'].astype(str).str.strip().str.replace('"', ''), errors='coerce')
        mean_qty = df['qty'].mean()
        df['qty'] = df['qty'].fillna(mean_qty)
    
    return df

def remove_invalid_rows(df):
    """Remove rows with negative prices or quantities."""
    if 'price' in df.columns:
        df = df[df['price'] >= 0]
    if 'qty' in df.columns:
        df = df[df['qty'] >= 0]
    return df

if __name__ == "__main__":
    raw_path = os.path.join(script_dir, "..", "data", "raw", "sales_data_raw.csv")
    cleaned_path = os.path.join(script_dir, "..", "data", "processed", "sales_data_clean.csv")

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())