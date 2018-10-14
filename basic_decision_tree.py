import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

main_file_path = '../input/house-prices-advanced-regression-techniques/train.csv' # this is the path to the Iowa data that you will use
data = pd.read_csv(main_file_path)

# Run this code block with the control-enter keys on your keyboard. Or click the blue botton on the left
print('Some output from running this cell')
#print(data.head())
#print(data.describe())
#print(data.columns)
y=data.SalePrice

data_predictors = ['LotArea','YearBuilt','1stFlrSF','2ndFlrSF','FullBath','BedroomAbvGr','TotRmsAbvGrd']
x=data[data_predictors]

train_x,val_x,train_y,val_y = train_test_split(x,y,random_state=0)

data_model = DecisionTreeRegressor()
data_model.fit(train_x, train_y)

print("Making predictions for the following 5 houses:")
print(x.head())
print("The predictions are")
data_predicted = data_model.predict(val_x)
mean_absolute_error(val_y,data_predicted)