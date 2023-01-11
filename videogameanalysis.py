# import pandas as pd, numpy as np
import pandas as pd
import matplotlib
#%%
# import dataset
games = pd.read_csv("datasets/vgsales.csv")
games.head()
#%%
#find the type of columns
games.dtypes
#%%
games.Genre.describe()
#%%
games.Genre.value_counts()
#%%
games.head()
#%%
games.Platform.value_counts()
#%%
games.Year.value_counts()
#%%
games.Publisher.value_counts()
#%%
type(games.Genre.value_counts())
#%%
games.Genre.value_counts().head()
#%%
games.Genre.value_counts().head(3)
#%%
games.Genre.unique()
#%%
games.Genre.nunique()
#%%
#pivot table
pd.crosstab(games.Genre,games.Year)
#%%
pd.crosstab(games.Publisher,games.Year)
#%%
games.Global_Sales.describe()
#%%
games.Global_Sales.mean()
#%%
games.Global_Sales.stdev()
#%%
games.Global_Sales.std()
#%%
games.Year.plot(kind="hist")
#%%
games.Genre.value_counts().plot(kind="hist")
#%%
plt = games.Genre.value_counts().plot(kind="hist")
plt.savefig("output/bargraph.png")
#%%
