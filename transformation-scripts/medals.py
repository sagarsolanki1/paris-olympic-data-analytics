import pandas as pd

# Load the medal data
medals_file_path = "C:\\Users\\solan\\Downloads\\master\\paris-olympic-data-analytics\\olympic-data\\medals.csv"
medals_df = pd.read_csv(medals_file_path)

# Aggregate the data by country
country_medals = medals_df.groupby('country').agg(
    Gold=('medal_type', lambda x: (x == 'Gold Medal').sum()),
    Silver=('medal_type', lambda x: (x == 'Silver Medal').sum()),
    Bronze=('medal_type', lambda x: (x == 'Bronze Medal').sum())
).reset_index()

# Calculate Total Medals
country_medals['Total'] = country_medals['Gold'] + country_medals['Silver'] + country_medals['Bronze']

# Sort the data by Gold, Silver, and Bronze for ranking
country_medals.sort_values(by=['Gold', 'Silver', 'Bronze'], ascending=False, inplace=True)

# Assign ranks based on Gold, Silver, and Bronze
country_medals['Rank'] = range(1, len(country_medals) + 1)

# To create the 'Rank by Total', we need to sort by Total medals as well
country_medals.sort_values(by=['Total'], ascending=False, inplace=True)
country_medals['Rank by Total'] = range(1, len(country_medals) + 1)

# Re-sort back to the original ranking by Gold, Silver, Bronze
country_medals.sort_values(by=['Gold', 'Silver', 'Bronze'], ascending=False, inplace=True)

# Select and reorder the columns
final_columns = ['Rank', 'country', 'Gold', 'Silver', 'Bronze', 'Total', 'Rank by Total']
final_df = country_medals[final_columns]

# Output the transformed data to a new CSV
output_file_path = "C:\\Users\\solan\\Downloads\\master\\paris-olympic-data-analytics\\transformed-data\\country_medals_summary.csv"
final_df.to_csv(output_file_path, index=False)
