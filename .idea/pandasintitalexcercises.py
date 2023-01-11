#import pandas as pd
import pandas as pd

obj=pd.Series([1,"Rohit",3,"Prateek"])
obj2=pd.Series([1,"Rohit",3,"Prateek"], index=['a',"b",'c','d'])

marks = {"rohit":100,"tushti":101,"prateek":102,"meenakshi":50}
marksDF = pd.Series(marks)
print("marksDF=",marksDF)
