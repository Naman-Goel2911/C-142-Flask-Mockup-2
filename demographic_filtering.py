import numpy
import pandas as pd

df = pd.read_csv('articles.csv')

df = df.sort_values(['total_events'], ascending = [True])

output = df[['title']].head(20).values.tolist()