import streamlit as st
import datetime

st.set_page_config(page_title="Age Calculator", page_icon="🎂")

st.title("🎂 Age Calculator")
st.write("Select your date of birth to calculate your current age.")


def calculate_age(born: datetime.date, today: datetime.date) -> tuple[int, int, int]:
    years = today.year - born.year
    months = today.month - born.month
    days = today.day - born.day

    if days < 0:
        previous_month = today.month - 1 or 12
        previous_month_year = today.year - 1 if today.month == 1 else today.year
        last_day_previous_month = (
            datetime.date(previous_month_year, previous_month % 12 + 1, 1)
            - datetime.timedelta(days=1)
        ).day
        days += last_day_previous_month
        months -= 1

    if months < 0:
        months += 12
        years -= 1

    return years, months, days


today = datetime.date.today()
dob = st.date_input(
    "Date of birth",
    value=datetime.date(2000, 1, 1),
    min_value=datetime.date(1900, 1, 1),
    max_value=today,
)

if dob > today:
    st.error("Date of birth cannot be in the future.")
else:
    years, months, days = calculate_age(dob, today)

    st.subheader("Your age")
    st.success(f"You are **{years} years, {months} months, and {days} days** old.")

    this_year_birthday = datetime.date(today.year, dob.month, dob.day)
    if this_year_birthday < today:
        next_birthday = datetime.date(today.year + 1, dob.month, dob.day)
    else:
        next_birthday = this_year_birthday

    days_to_birthday = (next_birthday - today).days

    if days_to_birthday == 0:
        st.balloons()
        st.info("Happy Birthday! 🎉")
    else:
        st.info(f"Your next birthday is in **{days_to_birthday} day(s)**.")