import streamlit as st


st.title("Hello from bot235!")
st.subheader("Brewed with Streamlit")
st.text("Welcome to the first Interactive app")
st.write("Choose your fav variety of songs ")

songs = st.selectbox("your fav songs:" ,["Andaaz a karam" , "High on you" , "in the pool" , "pal pal"])

st.write(f"{songs} playing now !!")