import streamlit as st
import pandas as pd
import joblib


# Page Configuration
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="wide"
)


# Load model
model = joblib.load("churn_model.pkl")
model_columns = joblib.load("model_columns.pkl")


# Custom CSS

st.markdown(
    """
    <style>

    .main-title {
        font-size:40px;
        font-weight:bold;
        text-align:center;
        color:#1f4e79;
    }

    .sub-title {
        text-align:center;
        font-size:18px;
        color:gray;
    }

    .result-box {
        padding:20px;
        border-radius:10px;
        text-align:center;
        font-size:25px;
        font-weight:bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# Header

st.markdown(
    '<p class="main-title">📊 Customer Churn Prediction</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Machine Learning powered customer retention analysis</p>',
    unsafe_allow_html=True
)


st.divider()


# Sidebar

st.sidebar.header("👤 Customer Information")


SeniorCitizen = st.sidebar.selectbox(
    "Senior Citizen",
    [0,1]
)


tenure = st.sidebar.slider(
    "Tenure (Months)",
    0,
    100,
    12
)


MonthlyCharges = st.sidebar.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)


TotalCharges = st.sidebar.number_input(
    "Total Charges",
    min_value=0.0,
    value=800.0
)


Contract = st.sidebar.selectbox(
    "Contract Type",
    [
        "Month-to-month",
        "One year",
        "Two year"
    ]
)


InternetService = st.sidebar.selectbox(
    "Internet Service",
    [
        "DSL",
        "Fiber optic",
        "No"
    ]
)


PaymentMethod = st.sidebar.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)



# Main Section

col1, col2 = st.columns(2)


with col1:

    st.info(
        """
        ### 🤖 Model Information

        **Algorithm:** Decision Tree Classifier

        **Task:** Customer Churn Prediction

        **Goal:** Identify customers who may leave the service.
        """
    )


with col2:

    st.success(
        """
        ### 📌 How it works

        1. Enter customer details
        2. Click Predict
        3. Get churn prediction instantly
        """
    )



st.divider()



if st.button(
    "🚀 Predict Customer Status",
    use_container_width=True
):


    input_data = pd.DataFrame(
        columns=model_columns
    )


    input_data.loc[0] = 0


    input_data["SeniorCitizen"] = SeniorCitizen
    input_data["tenure"] = tenure
    input_data["MonthlyCharges"] = MonthlyCharges
    input_data["TotalCharges"] = TotalCharges



    if Contract == "One year":
        input_data["Contract_One year"] = 1

    elif Contract == "Two year":
        input_data["Contract_Two year"] = 1



    if InternetService == "Fiber optic":
        input_data["InternetService_Fiber optic"] = 1

    elif InternetService == "No":
        input_data["InternetService_No"] = 1



    if PaymentMethod == "Electronic check":
        input_data["PaymentMethod_Electronic check"] = 1

    elif PaymentMethod == "Mailed check":
        input_data["PaymentMethod_Mailed check"] = 1

    elif PaymentMethod == "Credit card (automatic)":
        input_data["PaymentMethod_Credit card (automatic)"] = 1



    prediction = model.predict(input_data)



    st.divider()


    if prediction[0] == 1:

        st.markdown(
            """
            <div class="result-box">
            ⚠️ Customer is likely to churn
            </div>
            """,
            unsafe_allow_html=True
        )


        st.warning(
            "Recommendation: Consider offering retention benefits."
        )


    else:

        st.markdown(
            """
            <div class="result-box">
            ✅ Customer is likely to stay
            </div>
            """,
            unsafe_allow_html=True
        )


        st.success(
            "Customer relationship looks healthy."
        )



st.divider()


st.caption(
    "Built using Python, Scikit-learn and Streamlit 🚀"
)