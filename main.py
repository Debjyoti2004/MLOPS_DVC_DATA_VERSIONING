import pandas as pd
import os

# Create a sample DataFrame with column names
data = {
    'Name': ['John', 'Emma', 'David'],
    'Age': [22, 28, 31],
    'City': ['Boston', 'Seattle', 'Houston']
}

df = pd.DataFrame(data)

# Adding new row to df (V2)
new_row_loc = {'Name': 'Mike', 'Age': 26, 'City': 'Denver'}
df.loc[len(df.index)] = new_row_loc

# # Adding new row to df (V3)
# new_row_loc2 = {'Name': 'Sophia', 'Age': 24, 'City': 'Austin'}
# df.loc[len(df.index)] = new_row_loc2

# Ensure the "data" directory exists
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the DataFrame to a CSV file
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")
