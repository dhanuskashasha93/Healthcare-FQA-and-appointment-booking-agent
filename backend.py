from database import save_appointment


def get_response(query):
    query = query.lower().strip()

    # Hospital timings
    if "timing" in query or "hospital time" in query:
        return "The hospital is open from 9:00 AM to 5:00 PM."

    # Hospital services
    elif "service" in query or "services" in query:
        return (
            "The hospital provides General Medicine, Pediatrics, "
            "Dental and Cardiology services."
        )

    # Appointment
    elif "appointment" in query or "book" in query:
        return "Sure! Please use the appointment booking section."

    # Emergency
    elif "emergency" in query:
        return (
            "For emergencies, please contact the nearest emergency "
            "department or local emergency service."
        )

    # Doctor
    elif "doctor" in query:
        return "We have General Physician, Pediatrician and Cardiologist."

    # Default response
    else:
        return (
            "Sorry, I could not understand your question. "
            "I can help with general healthcare FAQs and appointment booking."
        )


def book_appointment(doctor, date, time):
    try:
        save_appointment(doctor, date, time)

        return (
            "✅ Appointment Confirmed!\n\n"
            f"Doctor: {doctor}\n"
            f"Date: {date}\n"
            f"Time: {time}"
        )

    except Exception as e:
        return f"❌ Booking failed: {e}"