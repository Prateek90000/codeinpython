# import packages
import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import seaborn as sns
#%%
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
diabetes = pd.read_csv("datasets/pima-indians-diabetes.csv",header=None,names=col_names)
#%%
diabetes.head()
#%%
x_col= ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']
y_col = ['label']

#%%
XVals = diabetes[x_col]
#%%
XVals.head()
#%%
YVales = diabetes[y_col]
#%%
YVales.head()
#%%
randomSeed=7
XVals_train, XVals_test, YVales_train, YVales_test = train_test_split(XVals,YVales,test_size=0.25,random_state=randomSeed)
#%%
lr = LogisticRegression(random_state=randomSeed)
#%%
lr.fit(XVals_train,YVales_train)
#%%
YPred = lr.predict(XVals_test)
#%%
# confusion matrix
from sklearn.metrics import confusion_matrix, classification_report
conf_matrix = confusion_matrix(YVales_test,YPred)
#%%
import matplotlib.pyplot as plt

class_names=[0,1] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(conf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()
#%%
clf = classification_report(YVales_test,YPred,target_names=["without diabetes","with diabetes"])
print("classification report=",clf)
#%%
#ROC curve
YPreds_variations = lr.predict_proba(XVals_test)
from sklearn.metrics import roc_curve
#%%
YPreds_variations = YPreds_variations[::,1]
fpr,tpr,other =roc_curve(YVales_test,YPreds_variations)
#%%
from sklearn.metrics import roc_auc_score
auc =roc_auc_score(YVales_test,YPreds_variations)
#%%
plt.plot(fpr,tpr, label="auc="+str(round(auc,2)))
plt.legend(loc=4)
plt.show()
#%%
