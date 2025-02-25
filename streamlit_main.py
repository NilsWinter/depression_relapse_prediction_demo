import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.header("Depression Relapse Risk Calculator")
st.sidebar.title("Patient Information Panel")
st.sidebar.markdown("Please enter patient details")

# Input features based on known depression relapse risk factors
Age = st.sidebar.slider("Age", 18, 80)
Gender = st.sidebar.selectbox("Gender", ("Male", "Female"))
PreviousEpisodes = st.sidebar.selectbox("Previous depressive episodes", ("No", "Yes"))
FamilyHistory = st.sidebar.selectbox("Family history of depression", ("No", "Yes"))
ChildhoodTrauma = st.sidebar.selectbox("Childhood trauma", ("No", "Yes"))
ComorbidAnxiety = st.sidebar.selectbox("Comorbid anxiety disorder", ("No", "Yes"))
SleepDisturbances = st.sidebar.selectbox("Sleep disturbances", ("No", "Yes"))
MedicationAdherence = st.sidebar.selectbox("Medication adherence", ("Good", "Poor"))
SocialSupport = st.sidebar.selectbox("Social support", ("Strong", "Weak"))
LifeStressors = st.sidebar.selectbox("Recent life stressors", ("No", "Yes"))

if st.button("Calculate Risk"):
    # Load model (dummy loading, replace with actual model in deployment)
    # rf_clf = jl.load("depression_relapse_model.pkl")

    # Simulated prediction (replace with real model output)
    x = pd.DataFrame([[Gender, PreviousEpisodes, FamilyHistory, ChildhoodTrauma, ComorbidAnxiety,
                       SleepDisturbances, MedicationAdherence, SocialSupport, LifeStressors, Age]],
                     columns=["Gender", "PreviousEpisodes", "FamilyHistory", "ChildhoodTrauma",
                              "ComorbidAnxiety", "SleepDisturbances", "MedicationAdherence",
                              "SocialSupport", "LifeStressors", "Age"])

    x = x.replace(["Male", "Female"], [1, 2])
    x = x.replace(["No", "Yes"], [0, 1])
    x = x.replace(["Good", "Poor"], [0, 1])
    x = x.replace(["Strong", "Weak"], [0, 1])

    # Simulating a probability output for relapse risk (replace with real model)
    predicted_risk = round(0.1 + 0.7 * (x.iloc[0].sum() / 10), 2)  # Dummy probability between 10%-80%

    # Output result
    st.success(f"Estimated risk of depression relapse within 2 years: {predicted_risk:.2%}")

    # Pie chart visualization
    fig, ax = plt.subplots()
    labels = ['Relapse Risk', 'No Relapse Risk']
    sizes = [predicted_risk * 100, 100 - (predicted_risk * 100)]
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'green'])
    ax.axis('equal')
    st.pyplot(fig)

st.subheader('About This Tool')
st.markdown(
    'This risk calculator is designed to estimate the likelihood of depression relapse within two years. It is based on known risk factors but should not replace clinical judgment. The model considers multiple personal and clinical factors to provide an approximate risk assessment.')
