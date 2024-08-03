import streamlit as st
import joblib

# Load your trained models
svr_model = joblib.load('svr_model.pkl')
dt_model = joblib.load('dt_model.pkl')
lr_model = joblib.load('lr_model.pkl')

# Define function for making predictions
def predict_fuel_consumption(model, data):
    prediction = model.predict(data)
    # Round prediction to 2 decimal places
    rounded_prediction = round(prediction[0], 2)
    return rounded_prediction

# Streamlit app
# Page configuration
st.set_page_config(page_title="Fuel Consumption Prediction Model", page_icon="📈", layout="wide")

def main():
    st.title("Fuel Consumption Prediction Model📈")
    st.write("Enter the features to predict fuel consumption.")

    # Input fields for user data
    co2_emissions = st.number_input("CO2 Emissions (g/km)")
    eng_displacement = st.number_input("Engine Displacement (Litres)")
    num_cylinders = st.number_input("Number of Cylinders", step=1)  # Specify step=1 for whole numbers
    transmission = st.number_input("Transmission Label Encoded", step=1)  # Specify step=1 for whole numbers

    user_data = [[co2_emissions, eng_displacement, num_cylinders, transmission]]

    # Button to trigger predictions
    if st.button("Predict🔍"):
        # Check if any input field is empty
        if any(x == 0 for x in user_data[0]):
            st.warning("Please enter values for all features.")
        else:
            # Make predictions using each model
            svr_prediction = predict_fuel_consumption(svr_model, user_data)
            dt_prediction = predict_fuel_consumption(dt_model, user_data)
            lr_prediction = predict_fuel_consumption(lr_model, user_data)

            # Display predictions with units
            st.write("SVR Prediction (L/100km):", svr_prediction)
            st.write("Decision Tree Prediction (L/100km):", dt_prediction)
            st.write("Linear Regression Prediction (L/100km):", lr_prediction)

# Run the app
if __name__ == "__main__":
    main()
