import pandas as pd
df_original = pd.read_csv('Part B/data/imdb_top_1000.csv')

df_original['Runtime'] = df_original['Runtime'].str.replace(' min', '').astype(float)
avg_runtime = df_original['Runtime'].mean()
print(f"The average runtime of movies is {avg_runtime} minutes.")