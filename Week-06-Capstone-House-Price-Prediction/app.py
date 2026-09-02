import streamlit as st
import pandas as pd
import joblib


# Load model

model = joblib.load(
    "house_price_model.pkl"
)


st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠"
)


st.title(
    "🏠 House Price Prediction"
)


st.write(
    "Enter house details to estimate the median house price."
)



# Input features

MedInc = st.number_input(
    "Median Income",
    value=5.0
)


HouseAge = st.number_input(
    "House Age",
    value=20.0
)


AveRooms = st.number_input(
    "Average Rooms",
    value=5.0
)


AveBedrms = st.number_input(
    "Average Bedrooms",
    value=1.0
)


Population = st.number_input(
    "Population",
    value=1000.0
)


AveOccup = st.number_input(
    "Average Occupancy",
    value=3.0
)


Latitude = st.number_input(
    "Latitude",
    value=34.0
)


Longitude = st.number_input(
    "Longitude",
    value=-118.0
)



if st.button("Predict Price"):


    input_data = pd.DataFrame({

        "MedInc":[MedInc],

        "HouseAge":[HouseAge],

        "AveRooms":[AveRooms],

        "AveBedrms":[AveBedrms],

        "Population":[Population],

        "AveOccup":[AveOccup],

        "Latitude":[Latitude],

        "Longitude":[Longitude]

    })


    prediction = model.predict(
        input_data
    )


    st.success(
        f"Estimated House Price: ${prediction[0]*100000:.2f}"
    )