import pandas as pd

# File paths
input_file_path = r'C:\\Users\\solan\\Downloads\\master\\paris-olympic-data-analytics\\olympic-data\\coaches.csv'
output_file_path = r'C:\\Users\\solan\\Downloads\\master\\paris-olympic-data-analytics\\transformed-data\\transformed_coaches.csv'

# Load the data
df_coaches = pd.read_csv(input_file_path)

# Transform the data
df_coaches_transformed = pd.DataFrame()
df_coaches_transformed['Name'] = df_coaches['name']
df_coaches_transformed['Country'] = df_coaches['country']
df_coaches_transformed['Discipline'] = df_coaches['disciplines']

# Handle the Event column (considering it might be empty)
# If the event information is not provided, we can set it to NaN or a placeholder
df_coaches_transformed['Event'] = df_coaches['events'].fillna('')

# Save the transformed data
df_coaches_transformed.to_csv(output_file_path, index=False)

print("Transformed coaches data saved to:", output_file_path)
