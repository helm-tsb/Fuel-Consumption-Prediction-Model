# Fuel Consumption Prediction Model

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-blue)](https://fuel-consumption-prediction-model.streamlit.app/)

## Overview

This project leverages machine learning to predict fuel consumption based on various vehicle features. The app is designed to be user-friendly and provides predictions using three different regression models. The web application is built with Streamlit and allows users to input specific vehicle data to receive accurate fuel consumption predictions.

You can access the deployed application [here](https://fuel-consumption-prediction-model.streamlit.app/).

## Features

- **Interactive Input Fields**: Users can enter CO2 emissions, engine displacement, number of cylinders, and transmission type to get fuel consumption predictions.
- **Multiple Models for Comparison**: The application provides predictions from three distinct machine learning models:
  - Support Vector Regression (SVR)
  - Decision Tree Regression (DT)
  - Linear Regression (LR)
- **Real-time Predictions**: The app computes and displays predictions instantaneously as the user inputs the data.
- **User-Friendly Interface**: A clean and intuitive interface ensures ease of use for all users.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Streamlit
- joblib

### Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/fuel-consumption-prediction.git
   cd fuel-consumption-prediction
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the trained model files are present in the project directory:
   - `svr_model.pkl`
   - `dt_model.pkl`
   - `lr_model.pkl`

### Running the App Locally

To run the application locally, execute the following command:
```bash
streamlit run app.py
```

This command will start a local Streamlit server and open the app in your default web browser.

## Usage

1. Open the web app in your browser.
2. Enter the required vehicle features:
   - **CO2 Emissions (g/km)**: The amount of CO2 emitted per kilometer.
   - **Engine Displacement (Litres)**: The volume of the engine.
   - **Number of Cylinders**: The total number of cylinders in the engine.
   - **Transmission Label Encoded**: The encoded value representing the transmission type.
3. Click the **Predict** button to get the fuel consumption predictions from all three models.
4. View the predictions displayed on the screen, which include:
   - SVR Prediction (L/100km)
   - Decision Tree Prediction (L/100km)
   - Linear Regression Prediction (L/100km)

## Project Structure

- `app.py`: The main Streamlit application script.
- `Cleaned dataset.xlsx`: The dataset used for cleaning and training the models.
- `Fuel Consumption Prediction Model.ipynb`: Jupyter Notebook containing the code for data preprocessing, model training, and evaluation.
- `requirements.txt`: A list of Python packages required to run the app.

## Data

The dataset used in this project includes various features related to vehicle specifications and fuel consumption. It was cleaned and preprocessed to ensure the accuracy and reliability of the predictions. The key features used for prediction include CO2 emissions, engine displacement, number of cylinders, and transmission type.

## Model Training

Three machine learning models were trained on the dataset to predict fuel consumption:
- **Support Vector Regression (SVR)**: A robust model effective in high-dimensional spaces.
- **Decision Tree Regression (DT)**: A model that splits the data into subsets based on the most significant differentiators.
- **Linear Regression (LR)**: A simple yet powerful model that assumes a linear relationship between the input features and the target variable.

The models were trained and evaluated using appropriate metrics to ensure high accuracy and reliability.

## Contributing

We welcome contributions from the community! If you have any suggestions or improvements, please feel free to open an issue or submit a pull request. Contributions can include:
- Enhancing the user interface
- Improving the prediction accuracy
- Adding new features or models
- Bug fixes and optimizations

## Acknowledgements

- **Streamlit** for providing an excellent framework for building and deploying interactive data applications.

I hope this project helps you in understanding and predicting fuel consumption using machine learning models. Feel free to reach out with any questions or feedback!
