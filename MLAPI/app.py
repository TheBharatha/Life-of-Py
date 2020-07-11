# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#Necessary libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics


# %%
##Get the dataset
from sklearn.datasets import load_boston
bos = load_boston()


# %%
##Initialize dataset
bos_init = pd.DataFrame(bos.data)


# %%
###Preview of the top five rows
bos_init.head()


# %%
##Import feature names from the dataset
bos_init.colums = bos.feature_names
bos_init.head()


# %%
##Further need to predict price, create a target variable for the ML model
bos_init['Price'] = bos.target


# %%
##The ML model will need a numerical value rather than categorical value for the predection of price; check if there are any NULL values
bos_init.isnull().sum()


# %%
##Check if the values are categorical
bos_init.info()


# %%
#Creating the ML model for the Price prediction
##Step 1: Separate features and target variables
##Step 2: Split the dataset into training and testing dataset
##Continue creating the ML model


# %%
##Separate features and target variables
x = bos_init.drop(['Price'], axis = 1)
y = bos_init['Price'] 


# %%
##Split the dataset into training and testing dataset
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)
print('Shape of x_train \n', x_train.shape, '\n\n Shape of x_test \n', x_test.shape, '\n-------------\n')
print('Shape of y_train \n', y_train.shape, '\n\n Shape of y_test \n', y_test.shape)


# %%
##Creating the ML model
from sklearn.ensemble import RandomForestRegressor
classifier = RandomForestRegressor()
classifier.fit(x_train, y_train)


# %%
#Model evaluation; evaluate the model performance for training and test dataset


# %%
##Training dataset model evaluation
print('Training dataset model evaluation results \n')
prediction = classifier.predict(x_train)
print('R^2: ', metrics.r2_score(y_train, prediction))
print('Mean Abs Error: ', metrics.mean_absolute_error(y_train, prediction))
print('Mean Squared Error: ', metrics.mean_squared_error(y_train, prediction))
print('Root Mean Square Error: ', np.sqrt(metrics.mean_squared_error(y_train, prediction)), '\n')

##Test dataset model evaluation
print('\nTraining dataset model evaluation results \n')
prediction_test = classifier.predict(x_test)
print('R^2: ', metrics.r2_score(y_test, prediction_test))
print('Mean Abs Error: ', metrics.mean_absolute_error(y_test, prediction_test))
print('Mean Squared Error: ', metrics.mean_squared_error(y_test, prediction_test))
print('Root Mean Square Error: ', np.sqrt(metrics.mean_squared_error(y_test, prediction_test)))


# %%
#Save and use the ML model.
#Serialization and Deserialization mechanism will be useful to store the ML object model in byte system and the other way round


# %%
#Save the model to a file
import pickle
with open('model/model.pkl', 'wb') as file:
    pickle.dump(classifier, file)

#Save the Columns
model_columns = list(x.columns)
with open('model/model_columns.pkl', 'wb') as file:
    pickle.dump(model_columns, file)


# %%
#API Creation for the ML model


# %%
#Step 1: pip install Flask
#Step 2: Create a web server in Flask, and REST API
#Step 3: Create driectories 'model' and 'templates' within the root directory
#Step 4: Create two empty files within 'model' folder with the following file name and extension 'model.pkl' and 'model_columns.pkl'
#Step 5: Create a Python script file with the name 'app.py'
#Step 6: Test the API with Postman | Download and Install POSTMAN


# %%
#Once the app.py script is complete, run the below commands in the root directory to start the flask server
#% export FLASK_APP=app.py
#% export FLASK_ENV=development
#% flask run


from flask import render_template, request, jsonify
import flask
import traceback
import pickle
 
 
# App definition
app = Flask(__name__,template_folder='templates')
 
# importing models
with open('model/model.pkl', 'rb') as f:
   classifier = pickle.load (f)
 
with open('model/model_columns.pkl', 'rb') as f:
   model_columns = pickle.load (f)
 
 
@app.route('/')
def welcome():
   return "Price Prediction for the Boston Housing"
 
@app.route('/predict', methods=['POST','GET'])
def predict():
  
   if flask.request.method == 'GET':
       return "Prediction page"
 
   if flask.request.method == 'POST':
       try:
           json_ = request.json
           print(json_)
           query_ = pd.get_dummies(pd.DataFrame(json_))
           query = query_.reindex(columns = model_columns, fill_value = 0)
           prediction = list(classifier.predict(query))
 
           return jsonify({
               "prediction":str(prediction)
           })
 
       except:
           return jsonify({
               "trace": traceback.format_exc()
               })
      
 
if __name__ == "__main__":
   app.run()