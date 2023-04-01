# Mushroom Edibility Classifier
This is a mushroom edibility classifier built using machine learning techniques. The classifier provides a user-friendly web interface that allows users to input mushroom features and receive a prediction on the mushroom's edibility. This can be useful in identifying potentially dangerous mushrooms in the wild.

# Dataset
The dataset used for the model is the [Mushroom dataset](https://archive.ics.uci.edu/ml/datasets/mushroom) from UCI Machine Learning Repository.

# Model
  * Pre-Processed Data: Performed Label Encoding and Normalization
  * Feature Selection: Using Chi Squared
  * Classification Model: Random Forest
  * Hyperparameter Tuning: Pipelined feature selection and model fit to get best parameters
  * Saving the Pipeline: Pre-processing and the model were saved in .pkl files
  * Accuracy: 100% accuracy was achieved
  * Cross Validation: KFold cross validation was used and best score achieved was 1
  * Libraries Used: Pandas,Numpy,Sklearn,Pickle
  
# Backend
A Flask backend was implemented in Python, integrated with a MySQL database to manage login credentials. It enables users to sign up and log in, and then accepts user input to make predictions using the trained machine learning model.

# UI/UX

  * Signup Page
  <img src="https://github.com/11acm11/Mushroom_Edibility_Classifier/blob/main/Images/signup_page.jpg?raw=true"/>
   
  * Login Page
  <img src="https://github.com/11acm11/Mushroom_Edibility_Classifier/blob/main/Images/login_page.jpg?raw=true"/>
    
  * User Input Page
  <img src="https://github.com/11acm11/Mushroom_Edibility_Classifier/blob/main/Images/user_input.jpg?raw=true"/>
  
  * Result Page
  <img src="https://github.com/11acm11/Mushroom_Edibility_Classifier/blob/main/Images/result.jpg?raw=true"/>
    
    
