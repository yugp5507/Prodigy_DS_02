# -*- coding: utf-8 -*-
"""Prodigy_DS_02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IBNeDPHi9hEgYjJ5_k8gY430VB4fXd4a
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

tnc = pd.read_csv(r"/content/drive/MyDrive/Colab Notebooks/Data/titanic.csv")
tnc.head()

tnc1 = tnc.isnull().sum()
# tnc1.count()
tnc1

tnc2 = tnc.columns[tnc.isnull().any()]
tnc2

tnc3 = sns.heatmap(tnc.isnull(),yticklabels = False,cbar = False,cmap = 'inferno')
plt.show()

tnc.head()

tnc4 = sns.set_style('whitegrid')
tnc5 = sns.countplot(x = 'Survived',hue = 'Pclass',data = tnc,palette = 'deep')
plt.show()

tnc6 = sns.countplot(x='Survived', hue='Sex', data=tnc)
plt.show()

tnc8 = sns.countplot(x = 'SibSp',data = tnc)

plt.figure(figsize = (12,8))
sns.boxplot(x = 'Pclass',y = 'Age', data = tnc)

