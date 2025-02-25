import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.header("DEMO: Depression Relapse Risk Calculator")
st.sidebar.title("Patient Information Panel")
st.sidebar.markdown("Please enter patient details")

# Input features based on known depression relapse risk factors
Age = st.sidebar.slider("Age", 18, 80)
Age = (Age - 18) / 80
Gender = st.sidebar.selectbox("Gender", ("Male", "Female"))
PreviousEpisodes = st.sidebar.selectbox("Previous depressive episodes", ("No", "Yes"))
FamilyHistory = st.sidebar.selectbox("Family history of depression", ("No", "Yes"))
ChildhoodTrauma = st.sidebar.selectbox("Childhood trauma", ("No", "Yes"))
ComorbidAnxiety = st.sidebar.selectbox("Comorbid anxiety disorder", ("No", "Yes"))
SleepDisturbances = st.sidebar.selectbox("Sleep disturbances", ("No", "Yes"))
MedicationAdherence = st.sidebar.selectbox("Medication adherence", ("Good", "Poor"))
SocialSupport = st.sidebar.selectbox("Social support", ("Strong", "Weak"))
LifeStressors = st.sidebar.selectbox("Recent life stressors", ("No", "Yes"))

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
predicted_risk = max(0, min(round(0.1 + 0.7 * (x.iloc[0].sum() / len(x.columns)), 2), 1))  # Normalize by number of features
predicted_risk_percentage = predicted_risk * 100  # Ensure risk is between 0% and 100%

# Output result
st.success(f"Estimated risk of depression relapse within 2 years: {predicted_risk_percentage:.1f}%")

# Pie chart visualization
fig, ax = plt.subplots()
labels = ['Relapse Risk', 'No Relapse Risk']
sizes = [predicted_risk_percentage, max(0, 100 - predicted_risk_percentage)]  # Ensure non-negative values
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#bd1b06', '#32a873'])
ax.axis('equal')
st.pyplot(fig)

st.subheader('About This Tool')
st.markdown('This risk calculator is designed to estimate the likelihood of depression relapse within two years. It is based on known risk factors but should not replace clinical judgment. The model considers multiple personal and clinical factors to provide an approximate risk assessment.')
