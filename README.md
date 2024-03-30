# MLOPS_A1

Umer Iftikhar - 20i0784
Usman babar - 20i1784

DS-N

# Mobile Price Range Prediction

# Overview

This project provides a machine learning solution to predict the price range of mobile phones based on their specifications. The dataset used for this purpose has been taken from Kaggle's Mobile Price Classification, and contains a variety of features that describe the phones' characteristics.

Two models were experimented with:

Support Vector Machine (SVM)
Decision Tree Classifier

# Dataset

The dataset comprises several features that are influential in determining the price category of a mobile phone. These include technical specifications such as battery power, clock speed, presence of a touchscreen, and more.

# Models

SVM Classifier

The SVM Classifier is chosen for its effectiveness in high-dimensional spaces and its ability to model non-linear decision boundaries. 

Decision Tree Classifier

The Decision Tree Classifier provides a more interpretable model, using a tree-like model of decisions and their possible consequences. 

# Model Performance

The models were evaluated based on accuracy:

SVM Classifier:
Accuracy: 96%

Decision Tree Classifier:
Accuracy: 88%

# API Usage

The Flask API serves as an interface to interact with the trained models. Users can send HTTP POST requests with mobile phone specifications to receive predicted price ranges.

Endpoint
POST /predict

Payload
The request should include a JSON object with the following structure:

{
  "battery_power": 842,
  "blue": 0,
  "clock_speed": 2.2,
  "dual_sim": 0,
  "fc": 1,
  "four_g": 0,
  "int_memory": 7,
  "m_dep": 0.6,
  "mobile_wt": 188,
  "n_cores": 2,
  "pc": 2,
  "px_height": 20,
  "px_width": 756,
  "ram": 2549,
  "sc_h": 9,
  "sc_w": 7,
  "talk_time": 19,
  "three_g": 0,
  "touch_screen": 0,
  "wifi": 1
}

Response

The API response will include the predicted price range:
{
  "price_range": 1
}

# Installation

To run the API locally, follow these steps:

Clone the repository
Navigate to the cloned directory.
Install the required dependencies: pip install -r requirements.txt
Launch the Flask server: python app.py


