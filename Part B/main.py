import pandas as pd
import matplotlib.pylot as plt

original_df = pd.read_csv('imdb_top_1000.csv')
updated_df = original_df.loc[:,['Series_Title', 'Released_Year', 'Certificate' morees]]

welcome = """
    Welcome to my dataset sorter. Please choose the category you would like to sort (type the no. of the category, and type exit to quit).
     1: Series_Title
     2: Released_Year
     3: Certificate
     4: Runtime
     5: Genre
     6: IMDB_Rating
     7: Overview
     8: Meta_score
     9: Other (view dataset, etc.)

     Enter your input here: """
input(welcome)

title = input()
if title == 1:
    print('test')

exit = input()
if exit == "quit":
    quit