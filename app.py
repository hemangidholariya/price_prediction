import streamlit as st
import pandas as pd

#st.title("CodeX Beverage: Price Prediction")
st.set_page_config(page_title="CodeX Beverage: Price Prediction", layout="wide")
st.markdown(
    """
    <h1 style='text-align: center; color: white; font-family: "Trebuchet MS", sans-serif;'>
         CodeX Beverage: Price Prediction
    </h1>
    """,
    unsafe_allow_html=True
)




with st.form("Prediction_form"):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        age = st.number_input('Age',min_value=10,max_value=70, step=1)
        income = st.selectbox("Income Level (In L)", ["<10L", "10L-15L","16L-25L","26L-35L",">35L"])
        awareness = st.selectbox("Awareness of other brands", ["0 to 1", "2 to 4", "above 4"])
        packaging = st.selectbox("Packaging Preference", ["Simple", "Premium", "Eco-Friendly"])

    with col2:
        gender = st.selectbox("Gender", ["M", "F", "Other"])
        frequency = st.selectbox("Consume Frequency (weekly)", ["0-2 times", "3-4 times", "5-7 times"])
        reason = st.selectbox("Reason for choosing Brands", ["Price", "Quality", "Availability", "Brand Reputation"])
        health = st.selectbox("Health Concerns", ["Low(Not very concerned)", "Medium(moderately health conscious)", "High(Very health conscious)"])

    with col3:
        zone = st.selectbox("Zone", ["Metro", "Rural", "Urban", "Semi-Urban"])
        current_brand = st.selectbox("Current Brand", ["Established", "Newcomer"])
        preference = st.selectbox("Flavour Preference", ["Traditional", "Exotic"])
        situation = st.selectbox("Typical Consumption Situations", ["Active (eg. Sports, gym)", "Social (eg. Parties)", "Casual (eg. At home)"])

    with col4:
        occupation = st.selectbox("Occupation", ["Working Profession", "Entrepreneur", "Student", "Retired"])
        size = st.selectbox("Preferable Consumption Size", ["Small(250ml)", "Medium(500ml)", "Large(1L)"])
        channel = st.selectbox("Purchase Channel", ["Online", "Retail Store"])

    submit_btn = st.form_submit_button("Calculate Price Range")

if submit_btn:
    base_price = 100

    if income == "10L - 15L":
        base_price += 30
    elif income == "16L-25L":
        base_price += 70
    elif income == "26L-35L":
        base_price += 120
    elif income == ">35L":
        base_price += 170



    if occupation == "Entrepreneur":
        base_price += 40
    elif occupation == "Student":
        base_price -= 20

    if preference == "Exotic":
        base_price += 20
    elif preference == "Traditional":
        base_price += 10

    if packaging == "premium":
        base_price += 50
    elif packaging == "Eco-Friendly":
        base_price += 25


    if current_brand == "Established":
        base_price += 80
    elif current_brand == "Newcomer":
        base_price += 40

    if frequency == "5-7 times":
        base_price += 30

    if health == "High(Very health conscious)":
        base_price += 20


    if size == "Large(1L)":
        base_price += 40
    elif size == "Small(250ml)":
        base_price -= 20

    low = base_price - 20
    high = base_price + 20


    st.success(f"Predicted Price Range: **{low}- {high} INR**")

    st.write(pd.DataFrame({
        "Feature": ["Age", "Gender", "Income", "Occupation", "Preference", "Reason", "Frequency"],
        "Value": [age, gender, income, occupation, preference, reason, frequency]
    }))