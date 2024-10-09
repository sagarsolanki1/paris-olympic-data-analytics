import pandas as pd

# Load the team data
team_file_path = "C:\\Users\\solan\\Downloads\\master\\paris-olympic-data-analytics\\olympic-data\\teams.csv"
team_df = pd.read_csv(team_file_path)

# Preview the dataset (optional)
# print(team_df.head())

# Select the relevant columns: team, discipline, country, and events
transformed_team_df = team_df[['team', 'discipline', 'country', 'events']]

# Rename columns to match your desired output
transformed_team_df.columns = ['Team Name', 'Discipline', 'Country', 'Event']

# Output the transformed data to a new CSV
output_team_file_path = "C:\\Users\\solan\\Downloads\\master\\paris-olympic-data-analytics\\transformed-data\\transformed_teams.csv"
transformed_team_df.to_csv(output_team_file_path, index=False)

print("Team dataset transformed and saved successfully.")
