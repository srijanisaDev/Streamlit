import streamlit as st
import datetime

st.title("Chai maker app")

add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("Masala added to your chai")

tea_type = st.radio("Pick your chai base: " ,["Milk" , "water" ])    
st.write(f"Selected base {tea_type}")    

flavour = st.selectbox("choose Flavour : " , ["Adrak" , "kesar","Tulsi"])
st.write(f"Selected falvour {flavour}")

sugar = st.slider("Teaspoons" ,0,4,1)
if sugar > 2:
    st.warning("This can be harmful for your health!!")

cups = st.number_input("How many cups" , min_value=1 , max_value = 10 , step = 1)
st.write(f"selected cups {cups}") 

if st.button("Make chai"):
    st.success("Your chai is being brewed")

name = st.text_input("Enter your name ")
if name :
    st.write(f"Welcome, {name} ! Your chai is on the way")   



dob = st.date_input(
    "Select your date of Birth",
    min_value=datetime.date(1950, 1, 1),   
    max_value=datetime.date.today()
)

st.write(f"Your date of Birth is {dob}")

   


