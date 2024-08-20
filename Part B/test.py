# Modules
import pandas as pd
import matplotlib as plt

# Global Variables
quit = False

# Set up the df
original_df = pd.read_csv('Part B/data/imdb_top_1000.csv')
updated_df = pd.read_csv('Part B/data/imdb_top_1000.csv',
                            header=None,
                            names=['Series_Title', 'Released_Year', 'Certificate', 'Runtime', 'Genre', 'IMDB_Rating', 'Overview', 'Meta_score'])

updated_df = updated_df.drop(columns=['Poster_link', 'Director', 'Star1', 'Star2', 'Star3', 'Star4', 'No_of_votes', 'Gross'], axis=1, inplace=True)
print(updated_df)