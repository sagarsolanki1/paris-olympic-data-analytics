import pandas as pd
import ast

# Load the original athletes data
original_athletes_file_path = r'C:\\Users\\solan\\Downloads\\master\\paris-olympic-data-analytics\\olympic-data\\athletes.csv'
original_athletes_df = pd.read_csv(original_athletes_file_path)

# Function to safely evaluate the disciplines
def safe_eval(x):
    try:
        # Check if x is NaN, return empty list if so
        if pd.isna(x):
            return []
        # Attempt to convert the string representation of the list to an actual list
        return ast.literal_eval(x)
    except (ValueError, SyntaxError) as e:
        # If there's an error, print it and return an empty list
        print(f"Error evaluating: {x} | {e}")
        return []

# Expand the 'disciplines' column
original_athletes_df['disciplines'] = original_athletes_df['disciplines'].apply(safe_eval)

# Explode the DataFrame to separate rows for each discipline
expanded_df = original_athletes_df.explode('disciplines')

# Group by 'disciplines' and 'gender' to count athletes
gender_counts = expanded_df.groupby(['disciplines', 'gender']).size().unstack(fill_value=0)

# Create the entriesGender table
entries_gender = gender_counts.reset_index()
entries_gender.columns.name = None  # Remove the column group name
entries_gender['Total'] = entries_gender['Male'] + entries_gender['Female']  # Calculate total

# Rearranging columns for better clarity
entries_gender = entries_gender[['disciplines', 'Male', 'Female', 'Total']]
entries_gender.rename(columns={'disciplines': 'Discipline'}, inplace=True)

# Save the entriesGender table to a CSV file
output_gender_file_path = r'C:\\Users\\solan\\Downloads\\master\\paris-olympic-data-analytics\\transformed-data\\entriesGender.csv'
entries_gender.to_csv(output_gender_file_path, index=False)

print("EntriesGender table created and saved to:", output_gender_file_path)
