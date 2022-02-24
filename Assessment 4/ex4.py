import pandas as pd
ddf = pd.read_csv('C:\\Users\\Admin\\Desktop\\j\\matches.csv')
ddf.head()
ddf.columns
f=ddf['win_by_wickets'].loc[ddf['win_by_wickets']!=0]
f.mean()
f.std()
grouped__df = ddf.groupby(["city", "winner"])
for key,item in grouped__df:
  a_group = grouped__df.get_group(key)
  print(a_group, "\n")
