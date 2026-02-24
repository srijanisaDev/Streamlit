import streamlit as st

st.title("Chai Flavour Poll")


if "masala_votes" not in st.session_state:
    st.session_state.masala_votes = 0

if "adrak_votes" not in st.session_state:
    st.session_state.adrak_votes = 0


col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://i.pinimg.com/1200x/51/ac/c4/51acc41a62b1480d203ee25b5abc25a8.jpg", width=100)
    
    if st.button("Vote Masala Chai"):
        st.session_state.masala_votes += 1
        st.success("Thanks for voting Masala Chai")

    st.write(f"Votes: {st.session_state.masala_votes}")


with col2:
    st.header("Adrak Chai")
    st.image("https://i.pinimg.com/736x/15/75/29/15752944ed190b179f3c79815cb39252.jpg", width=165)
    
    if st.button("Vote Adrak Chai"):
        st.session_state.adrak_votes += 1
        st.success("Thanks for voting Adrak Chai")

    st.write(f"Votes: {st.session_state.adrak_votes}")



name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose your chai", ["Masala", "Adrak", "Kesar"])

st.write(f"Welcome {name}, your {tea} chai is getting ready ☕")


with st.expander("Show Chai making instructions"):
    st.write("""
    1. Boil water with tea leaves.
    2. Add Milk and spices.
    3. Serve hot.
    """)