# -*- coding: utf-8 -*-
"""linearrgression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12ir6AimA3vHVt24g1yqizI0OwABibBW7

**Importing required libraries and setting up the environment.**
"""

import numpy  as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

house_dat=pd.read_csv('/content/USA_Housing.csv')

house_dat.head(3)

"""**To train out the regression model, we will split up our data into "X" list that contains features to train on and "Y" list that contains target variable(price).**"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

x = house_dat[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]
Y = house_dat['Price']

"""**now we split datset into training set and testing set.**"""

X_train, X_test, y_train, y_test = train_test_split(x, Y, test_size=0.4, random_state=101)

"""**Creating linearregression object and fitting training set in it.**"""

lmr=LinearRegression()
y_pred=lmr.fit(X_train, y_train)

predictions=lmr.predict(X_test)
print(predictions)

plt.scatter(y_test,predictions)

sns.displot((y_test-predictions),bins=50)

"""**Evaluating metrics**
-->Mean absolute error
-->Mean squared error
-->Root mean squared error

All of these are loss functions because we want to minimize them.
"""

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, predictions))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, predictions))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

sns.distplot(house_dat['Price'])



sns.pairplot(house_dat)
sns.heatmap(house_dat.corr(), annot=True)





