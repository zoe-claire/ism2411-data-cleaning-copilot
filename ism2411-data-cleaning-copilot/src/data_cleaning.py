import pandas as pd
import os

# Use absolute path based on script location
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "..", "data", "raw", "sales_data_raw.csv")

df = pd.read_csv(file_path)

#Standardize column names