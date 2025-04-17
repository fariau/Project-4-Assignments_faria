import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="😊", layout="centered")

st.title("BMI Calculator")
st.markdown("""
## apna body mass index bmi calculate kry nichy apna wight or hight enter kren""")

col1, col2 = st.columns(2)
with col1: 
    weight = st.number_input("weight (kg):", min_value=1.0,format="%.2f")
with col2:
    hight = st.number_input("weight (m):", min_value=1.0,format="%.2f")
    
if hight > 0 and weight > 0:
    bmi = weight / (hight ** 2) ##bmi formula
    st.subheader("apka bmi h:")
    st.markdown(f"{bmi:.2f}", unsafe_allow_html=True)
    
    if bmi < 18.5:
        st.error("underweight")
    elif 18.5 <= bmi < 24.0:
        st.success("normalweight")
    elif 25 <= bmi < 29.5:
        st.warning("overweight")
    else:
        st.error("obsisty ")
        
else:
    st.info("please enter a valid weight and hight")