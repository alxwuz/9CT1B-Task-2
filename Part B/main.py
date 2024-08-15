welcome = """
    Welcome to my dataset sorter. Please choose the category you would like to sort (enter a number for each category, and type exit to quit).
     1: Series_Title
     2: Released_Year
     3: Certificate
     4: Runtime
     5: Genre
     6: IMDB_Rating
     7: Overview
     8: Meta_score
     """
input(welcome)
Series_Title = input()
if Series_Title == 1:
    print('test')
exit = input()
if exit == "quit":
    quit