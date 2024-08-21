# Modules
import pandas as pd
import matplotlib.pyplot as plt

# Global Variables
quit = False

# Load the dataset
original_df = pd.read_csv('Part B/data/imdb_top_1000.csv')

# Update and remove the unecessary columns (remove spaces from column title)
original_df.columns = original_df.columns.str.strip()
df_updated = original_df.drop(['Poster_Link', 'Director', 'Star1', 'Star2', 'Star3', 'Star4', 'No_of_Votes', 'Gross'], axis=1,)

# Functions
def showData():
    print(original_df)

def updatedData():
    print(df_updated)

def showScatter():
    original_df.plot(
                    kind='scatter',
                    x='Series_Title',
                    y='IMDB_Rating',
                    color='blue',
                    alpha=0.1,
                    title='IMDb Ratings of Movies'
                    )
    plt.show()

def userOptions():
    global quit

    print("""

        Welcome to Alex's dataset sorter! Please select an option (use numbers to navigate):
    1: Show the original dataset
    2: Show the updated dataset
    3: Visualise x in a graph
    4: View a specific column
    10: Quit
     
    """)

    try:
        answer = int(input('Enter input: '))

        if answer == 1:
            showData()

        elif answer == 2:
            updatedData()
        
        elif answer == 3:
            showScatter()

        elif answer == 4:
            column_name = (input("""
                      
        Please choose a column from the following:
    1: Poster_Link
    2: Series_Title
    3: Released_Year
    4: Certificate
    5: Runtime
    6: Genre
    7: IMDB_Rating
    8: Overview
    9: Meta_score
    10: Director
    11: Star1
    12: Star2
    13: Star3
    14: Star4
    15: No_of_votes
    16: Gross
                      
    Enter Input (enter the column name): """))
            if column_name in original_df.columns:
                print(original_df[column_name])
            else:
                print("Column not found. Please enter the specific column name (e.g. 'Genre'). ")

        elif answer == 10:
            quit = True

        else:
            print('Incorrect syntax. Please enter a number between 1 and x.')

    except ValueError:
        print('Invalid syntax, enter a number >:(.')

while not quit:
    userOptions()