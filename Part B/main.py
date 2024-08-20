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

columns_to_drop = ['Poster_Link', 'Other_Column', 'Director', 'Star1', 'Star2', 'Star3', 'Star4', 'No_of_Votes', 'Gross']
updated_df = original_df.drop(columns=columns_to_drop, errors='ignore')

# Define the functions
def showData():
    print(original_df)

def updatedData():
    print(updated_df)

def userOptions():
    global quit

    print("""

     Welcome to Alex's dataset sorter! Please select an option:
     1: Show the original dataset
     2: Show the updated dataset
     3: Visualise x in a graph
     10: Quit
     
     """)

    try:
        answer = int(input('Enter input: '))

        if answer == 1:
            showData()
        elif answer == 2:
            updatedData()
        elif answer == 10:
            quit = True

        else:
            print('Incorrect syntax. Please enter a number between 1 and x.')

    except ValueError:
        print('Invalid syntax, enter a number >:(.')

while not quit:
    userOptions()