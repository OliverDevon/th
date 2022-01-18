import pandas as pd
import plotly.graph_objects as ga
import csv 
df = pd.read_csv("porject107.csv")
studentDf=df.loc[df['student_id']=='TRL_abc']
print(studentDf.groupby('level')['attempt'].mean())
fig=ga.Figure(ga.Bar(
    x=studentDf.groupby('level')['attempt'].mean(),
    y=["Level 1", "Level 2", "Level 3", "Level 4" ],
    orientation = 'h'
))
fig.show()