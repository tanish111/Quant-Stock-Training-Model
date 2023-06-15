# Stock-Training-Model
The proposed approach utilizes a linear regression model to predict future stock prices based on historical data. By leveraging a dataset containing information such as open, close, high, low, and volume values from previous stock records, the model is trained to forecast the future close price of stocks.

The linear regression model analyzes the relationships between the various features and the target variable (close price) to establish a linear equation that represents the underlying patterns in the data. It identifies the correlation between the independent variables (open, close, high, low, and volume) and the dependent variable (close price), allowing for the prediction of future close prices based on these historical patterns.

The training process involves feeding the model with a substantial amount of historical stock data, allowing it to learn and capture the complex relationships between the features and the close price. Once trained, the model can effectively estimate the future close prices by inputting the relevant historical data.

It's important to note that while linear regression is a popular and widely used method for predicting stock prices, there are various other techniques and models available that can provide more accurate predictions, such as time series analysis, machine learning algorithms, or deep learning models like recurrent neural networks (RNNs) or long short-term memory (LSTM) networks. These advanced models can incorporate additional factors, such as market sentiment, news sentiment, or macroeconomic indicators, which may further enhance the accuracy of the predictions.You can create an feature request to add this models in project.

Overall, by utilizing a linear regression model trained on previous stock data, we can obtain a valuable tool for forecasting the future close prices of stocks. However, it's important to consider other advanced techniques and factors to achieve more precise predictions in real-world scenarios.

## How to use?
### Step-1
Add the historical data of stocks you want to analyse in CSV format, similar to the demo data provided in the folder. Ensure that all the columns in the CSV file are of the same type as the demo data.
### Step-2
Change no_of_stocks variable in line 7 to the number of stocks you are training.
### Step-3 
You are done run the python file it will give you 4 weights for Open,High,Low and Volume respectively.
Your required model is ready with the given weights.

