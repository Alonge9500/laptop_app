# -*- coding: utf-8 -*-
"""laptop_details.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xNK_PV4mOl2Rj3CYn7hvhkDQdEbgBm93
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('max_colwidth', None)
import re
import csv
from sklearn.preprocessing import LabelEncoder

RESOURCES_PATH = os.path.join(os.getcwd(), 'resources')
dataPath = os.path.join(RESOURCES_PATH,'laptop_details.csv')
data = pd.read_csv(dataPath)

df = data.copy()

# df.info()

# df.isna().sum()



"""## Feature Engineering
Since, this is mainly a text data, we will use the regex function to clean the data.
We will create new features such as Ram size, Ram type, Processor, Storage type, os from the poducts and feature table
"""

def extract_features(row):
    product = row['Product']
    feature = row['Feature']
    
    ram_size = re.findall(r'(\d+) ?(?:GB|TB)', feature)
    ram_size = ram_size[0] + ' GB' if ram_size else None
    
    ram_type = re.findall(r'(?:LP)?DDR\d\S*|Unified\sMemory', feature)
    ram_type = ram_type[0] if ram_type else None
    
    processor = re.findall(r'(?:AMD|Intel|M1|Qualcomm|Apple)[\s\w]+Processor', feature)
    processor = processor[0] if processor else None

    storage = re.findall(r'[\d]+\s(?:GB|TB)\s(?:HDD|SSD|EMMC)', product)
    storage = storage[0] if storage else None
    
    os = re.findall(r'(Windows (?:10|11)|Mac OS|Linux|DOS|Chrome)[\s\w]*Operating System', feature)
    os = os[0] if os else None

    display = re.findall(r'\d+(?:\.\d+)?\s*(?:cm|inch)\s*(?:\(|:)?\s*\d+(?:\.\d+)?\s*(?:cm|inch)?', feature)
    display = display[0] if display else None
    
    brand = re.findall(r'^\w+', product)
    brand = brand[0] if brand else None
    
    return pd.Series([ram_size, ram_type, processor, storage, os, display, brand], 
                     index=['Ram Size', 'Ram Type', 'Processor', 'Storage', 'OS', 'Display', 'Brand'])

df[['Ram Size', 'Ram Type', 'Processor', 'Storage', 'OS', 'Display', 'Brand']] = df.apply(extract_features, axis=1)

## Data Cleaning
df.MRP = df.MRP.apply(lambda x : x.replace('₹', '').replace(',', '')).astype(float)

df2 = df.copy()

df2.drop(df2.columns[[0, 1, 3]], axis=1, inplace=True)
#df2.isna().sum()

df2['Ram Type'] = df2['Ram Type'].str.replace('DDR4,','DDR4')

df2['StorageType'] = df2.Storage.apply(lambda x: x.split()[-1])
df2['Storage'] = df2.Storage.apply(lambda x: " ".join(x.split()[:2]))

"""### Visualization"""

import seaborn as sns
dataviz = df2.copy()
#df2.Storage.unique()

"""### Encoding"""

ram_dict = {
    '4 GB':0,
    '8 GB':1,
    '16 GB':2,
    '32 GB':3,
    '128 GB':4
    }

ram_type_dict = {
    'LPDDR3':0,
    'Unified Memory':1,
    'LPDDR4':2,'DDR4':3,
    'LPDDR4X':4,
    'LPDDR5':5,
    'DDR5':6
    }
processor_dict = {
    'AMD Athlon Dual Core Processor':0,
    'AMD Dual Core Processor':1,
    'Intel Celeron Dual Core Processor':2,
    'Intel Celeron Quad Core Processor':3,
    'Intel Pentium Quad Core Processor':4,
    'Intel Pentium Silver Processor':5,
    'AMD Ryzen 3 Dual Core Processor':6,
    'AMD Ryzen 3 Quad Core Processor':7,
    'AMD Ryzen 3 Hexa Core Processor':8,
    'AMD Ryzen 5 Dual Core Processor':9,
    'AMD Ryzen 5 Quad Core Processor':10,
    'AMD Ryzen 5 Hexa Core Processor':11,
    'AMD Ryzen 7 Quad Core Processor':12,
    'AMD Ryzen 7 Octa Core Processor':13,
    'AMD Ryzen 9 Octa Core Processor':14,
    'Apple M1 Processor':15,
    'Apple M1 Pro Processor':16,
    'Apple M1 Max Processor':17,
    'Apple M2 Processor':18,
    'Intel Core i3 Processor':19,
    'Intel OptaneIntel Core i3 Processor':20,
    'Intel Core i5 Processor':21,
    'Intel Evo Core i5 Processor':22,
    'Intel Core i7 Processor':23,
    'Intel Core i9 Processor':24,
    'Qualcomm Snapdragon 7c Gen 2 Processor':25
}


storage = [
    '32 GB',
    '64 GB',
    '128 GB',
    '256 GB',
    '512 GB',
    '1 TB',
    '2 TB'
]
storage_dict = {s: i for i, s in enumerate(storage)}

storage_type_dict = {
    'EMMC':0,
    'HDD':1,
    'SSD':2
}


column_dicts = {
    'Ram Size':ram_dict,
    'Ram Type':ram_type_dict,
    'Processor':processor_dict,
    'Storage':storage_dict,
    'StorageType':storage_type_dict
}



for col,col_dict in column_dicts.items():
  le = LabelEncoder().fit([*col_dict.keys()])

  #df2[col] = df2[col].map(col_dict).astype(int)
  le.classes_ = np.array([key for key in sorted(col_dict, key=col_dict.get)])
  df2[col] = le.transform(df2[col])
  df2[col] = pd.Categorical(df2[col], categories=col_dict.values(), ordered=True)

#df2.head()

le2 = LabelEncoder()

propertydict = []
label_encoding_categorical_columns = ['OS', 'Display','Brand']

for column in label_encoding_categorical_columns:
  encoded = le2.fit_transform(df2[column])
  df2.drop(column, axis=1, inplace=True)
  df2[column] = encoded
  df2[column] = df2[column].astype('category')
  feature_dict = dict(zip(range(len(le2.classes_)), le2.classes_))
  propertydict.append(feature_dict)

propertydict.append([ram_dict,ram_type_dict,storage_dict,processor_dict,storage_type_dict])

#np.quantile(df2.MRP,0.80)

"""### Model Building"""

# Split Data Set
from sklearn.model_selection import train_test_split 
import scipy.stats as stats


y = np.log(df2['MRP'])
x = df2.drop('MRP', axis =1)

#sns.distplot(y)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor


model = LinearRegression()
GBR = GradientBoostingRegressor()

GBR.fit(X_train,y_train)

prediction = GBR.predict(X_test)

from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error



# evaluate the model
mse = mean_squared_error(y_test, prediction)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, prediction)
mae = mean_absolute_error(y_test, prediction)

# print("MSE: ", mse)
# print("RMSE: ", rmse)
# print("R-squared: ", r2)

# sns.boxplot(data=df2,y='MRP', x='OS')

"""## Hyper Parameter Tuning"""

# parameters = {'learning_rate': [0.01,0.02,0.03,0.04],
#                'subsample'    : [0.9, 0.5, 0.2, 0.1],
#                'n_estimators' : [100,500,1000, 1500],
#                'max_depth'    : [4,6,8,10]
#                }

# from sklearn.model_selection import GridSearchCV

# grid_GBR = GridSearchCV(estimator=GBR, param_grid = parameters, cv = 2, n_jobs=-1)
# grid_GBR.fit(X_train, y_train)

# print(" Results from Grid Search " )
# print("\n The best estimator across ALL searched params:\n",grid_GBR.best_estimator_)
# print("\n The best score across ALL searched params:\n",grid_GBR.best_score_)
# print("\n The best parameters across ALL searched params:\n",grid_GBR.best_params_)

mainModel = GradientBoostingRegressor(learning_rate=0.02, max_depth=8, n_estimators=500,subsample=0.1)

mainModel.fit(X_train,y_train)

pred =mainModel.predict(X_test)

# evaluate the model
mse = mean_squared_error(y_test, pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, pred)
mae = mean_absolute_error(y_test, pred)

# print("MSE: ", mse)
# print("RMSE: ", rmse)
# print("R-squared: ", r2)

# X_train.head()

# import joblib

# joblib.dump(mainModel,'model.pkl')

