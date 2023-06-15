import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import os
directory = 'data2'
#Importing Stock Data 
no_of_stocks = 15 #Change 15 to the number of stocks you want to analyze.
coeffs = np.zeros((no_of_stocks+10,4)) 
counts = 0
for filename in os.listdir(directory):
    aapl_df = pd.read_csv('data2/x.us.csv')
    if filename.endswith('.csv'):
        data = "data2/" + filename
        aapl_df = pd.read_csv(data)
        #Normalizing each parameter to 0 to 1
    for row in aapl_df:
        if(row in ['Open','High','Low','Volume','Close']):
            max_r = max(aapl_df[row]) + max(aapl_df[row])*0.1
            for i in range(0,len(aapl_df[row])):
                try:
                    aapl_df.loc[i,row] = (aapl_df.loc[i,row]/max_r)
                except:
                    pass
    #Normalizing each parameter to 0 to 1
    for row in aapl_df:
        if(row in ['Open','High','Low','Volume','Close']):
            max_r = max(aapl_df[row]) + max(aapl_df[row])*0.1
            for i in range(0,len(aapl_df[row])):
                try:
                    aapl_df.loc[i,row] = (aapl_df.loc[i,row]/max_r)
                except:
                    pass
    #Identify features and making array of feature and target variable and set delay
    fetures = ['Open','High','Low','Volume']
    delay = 1
    input = aapl_df[fetures]
    X = input.loc[0:len(input)-2].to_numpy()
    target_shifted_df = aapl_df['Close']
    target_shifted_df = target_shifted_df.tail(-1)
    Y = target_shifted_df.to_numpy()
    #Training data with linear regression(batch gradient desent) using scikit
    model = LinearRegression().fit(X,Y)
    r_sq = model.score(X, Y)
    coeffs[counts] = model.coef_
    counts=counts+1
    print(counts)
for j in range(0,4):
    val = 0
    for i in range(0,no_of_stocks):
        val = val + coeffs[i][j]
    print(val/no_of_stocks)




