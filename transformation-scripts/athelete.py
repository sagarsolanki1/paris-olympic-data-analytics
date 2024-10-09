import pandas as pd
import ast

# Load your data (assuming you have it in a pandas DataFrame)
df = pd.read_csv("C:\\Users\\solan\\Downloads\\master\\paris-olympic-data-analytics\\olympic-data\\athletes.csv")

# Transform the data
df_athletes = df[['name', 'country_long', 'disciplines']].copy()

# Rename columns
df_athletes.columns = ['PersonName', 'Country', 'Discipline']

# Safe function to evaluate strings
def safe_eval(x):
    try:
        # Try to evaluate the string as a list
        return ', '.join(ast.literal_eval(x))
    except (ValueError, SyntaxError):
        # If it's not a list, return it as is
        return x

# Apply the safe_eval function to the 'Discipline' column
df_athletes['Discipline'] = df_athletes['Discipline'].apply(safe_eval)

# Save the transformed data to a new CSV file
df_athletes.to_csv("C:\\Users\\solan\\Downloads\\master\\paris-olympic-data-analytics\\transformed-data\\athletes_transformed.csv", index=False)