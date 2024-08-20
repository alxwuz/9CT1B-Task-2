# Modules
import pandas as pd
import matplotlib as plt

# Global Variables
quit = False

# Set up the df
original_df = pd.read_csv('Part B/data/imdb_top_1000.csv')
3
updated_df = pd.read_csv('Part B/data/imdb_top_1000.csv',
                            header=None,
                            names=['Poster_link', 'Series_Title', 'Released_Year', 'Certificate', 'Runtime', 'Genre', 'IMDB_Rating', 'Overview', 'Meta_score', 'Director', 'Star1', 'Star2', 'Star3', 'Star4', 'No_of_votes', 'Gross'])
updated_df = updated_df.drop(columns=['Poster_link', 'Director', 'Star1', 'Star2', 'Star3', 'Star4', 'No_of_votes', 'Gross'])

# Define the functions
def showData():
    original_df

def updatedData():
    updated_df

def userOptions():
    global quit

    print("""

     Welcome to Alex's dataset sorter! Please select an option:
     1: Show the original dataset
     2: Show the updated dataset
     10: Quit
     
     """)

    try:
        answer = int(input('Enter input: '))

        if answer == 1:
            print(showData)
        elif answer == 2:
            print(updatedData)
        elif answer == 10:
            quit = True
        else:
            print('Incorrect syntax. Please enter a number between 1 and x.')

    except:
        print('Invalid syntax, enter a number >:(.')

while not quit:
    userOptions()