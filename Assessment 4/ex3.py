import pandas as pd
mpg = pd.read_csv('C:\\Users\\Admin\\Desktop\\j\\nba.csv')
mpg.head()
mpg.shape
mpg.dtypes
mpg.describe()
mpg.median()
mpg['Age'].median()
