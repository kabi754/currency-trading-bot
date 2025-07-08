import streamlit as st

st.title("Currency Trading Signal Bot 💹")

price = 1.2430
moving_average = 1.2450

if price > moving_average:
    st.success("BUY 🔼")
else:
    st.error("SELL 🔽")
