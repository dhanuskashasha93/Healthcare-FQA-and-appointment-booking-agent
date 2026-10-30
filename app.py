import streamlit as st
from backend import get_response, book_appointment

st.set_page_config(
    page_title="Healthcare Agent",
    page_icon="🏥"
)

st.title("🏥 Healthcare FAQ & Appointment Booking Agent")
st.write("Ask a healthcare question or book an appointment.")

st.subheader("💬 Healthcare Assistant")

user_query = st.chat_input("Type your question...")

if user_query:
    st.chat_message("user").write(user_query)

    response = get_response(user_query)

    st.chat_message("assistant").write(response)

st.divider()

st.subheader("📅 Book an Appointment")

doctor = st.selectbox(
    "Select Doctor",
    ["Dr. Arun - General Physician",
     "Dr. Priya - Pediatrician",
     "Dr. Kumar - Cardiologist"]
)

date = st.date_input("Select Date")
time = st.time_input("Select Time")

if st.button("Book Appointment"):
    result = book_appointment(doctor, str(date), str(time))
    st.success(result)