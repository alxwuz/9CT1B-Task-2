# Modules
import pandas as pd
import matplotlib.pyplot as plt

# Global Variables
quit = False

# Load the dataset
df_original = pd.read_csv('Part B/data/imdb_top_1000.csv')

# Update and remove the unecessary columns (remove spaces from column title, so it works)
df_original.columns = df_original.columns.str.strip()

df_updated = df_original.drop(['Poster_Link', 'Director', 'Star1', 'Star2', 'Star3', 'Star4', 'No_of_Votes', 'Gross'], axis=1,)
df_updated.to_csv('Part B/data/imdb_top_1000_updated.csv')

# Functions
def showData():
    print(df_original)

def updatedData():
    print(df_updated)

def showScatter():
    df_original.plot(
                    kind='scatter',
                    x='Series_Title',
                    y='IMDB_Rating',
                    color='green',
                    alpha=0.1,
                    title='IMDb Ratings of Movies'
                    )
    plt.show()

def top20Movies():
    topmovies = df_original.sort_values(by='No_of_Votes', ascending=False).head(50)
    topmovies = topmovies.drop(['Poster_Link', 'Released_Year', 'Certificate', 'Runtime', 'Genre', 'Overview', 'Meta_score', 'Director', 'Star1', 'Star2', 'Star3', 'Star4', 'Gross'], axis=1)
    print(topmovies)

def bottom20Movies():
     bottommovies = df_original.sort_values(by='No_of_Votes', ascending=True).head(50)
     bottommovies = bottommovies.drop(['Poster_Link', 'Released_Year', 'Certificate', 'Runtime', 'Genre', 'Overview', 'Meta_score', 'Director', 'Star1', 'Star2', 'Star3', 'Star4', 'Gross'], axis=1)
     print(bottommovies)


def mainUI():
    global quit

    print("""

        Welcome to Alex's dataset program! Please use numbers to navigate the following options:
    [1] -> Show the original dataset
    [2] -> Show the updated dataset
    [3] -> Visualise IMDb ratings in a graph (hard to view because of giant dataset)
    [4] -> View a specific column
    [5] -> View the top 50 most popular movies
    [6] -> View the lowest 50 movies in the dataset (1000 - 950 ranking)
    [9] -> Quit
     
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
    1: Poster_Link (most may not work due to dataframe being outdated)
    2: Series_Title
    3: Released_Year
    4: Certificate
    5: Runtime
    6: Genre
    7: IMDB_Rating
    8: Overview
    9: Meta_score
    10: Director, Star1, Star2, Star3, Star4
    15: No_of_votes
    16: Gross
                      
    Enter column name: """))
            if column_name in df_original.columns:
                print(df_original[column_name])
            else:
                print("Column not found. Did you forget to enter the specific column name? ")

        elif answer == 5:
            top20Movies()

        elif answer == 6:
            bottom20Movies()

        elif answer == 9:
            quit = True

        else:
            print('Incorrect syntax. Please enter a number between 1 and x.')

    except ValueError:
        print('Invalid syntax, enter a number >:(.')

# Main Program
while not quit:
    mainUI()