import streamlit as st
import datetime
import time

st.set_page_config(page_title="Vice City Countdown", layout="centered")

# ----------------------
# STYLE CSS (Background removed)
# ----------------------
st.markdown(
    """
    <style>


    .overlay {
        /* Removed background overlay */
        padding: 2rem;
        min-height: 100vh;
    }

    .title {
        text-align: center;
        font-size: 4rem; /* Increased size */
        color: #ff00e6; /* Neon pink */
        text-shadow: 0 0 10px #ff00e6, 0 0 20px #ff00e6;
        margin-bottom: 1rem;
    }

    .countdown {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #00ffc3; /* Neon cyan */
        text-shadow: 0 0 10px #00ffc3, 0 0 20px #00ffc3;
        margin-top: 2rem;
    }

    .message {
        font-size: 2.5rem;
        text-align: center;
        color: #ffffff;
        text-shadow: 0 0 20px #ffffff, 0 0 40px #ffffff;
        margin-top: 3rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------
# CONTENT
# ----------------------
st.markdown("<div class='overlay'>", unsafe_allow_html=True)

# Use HTML headers to adjust the size directly
st.markdown("<h1 class='title'>🌴❤️ CountDown to see my Wife Hfesa ❤️🌴</a>", unsafe_allow_html=True)

# Define the target date/time
target_datetime = datetime.datetime(2025, 4, 25, 0, 0, 0)

# Space for the countdown display
countdown_placeholder = st.empty()

# ----------------------
# COUNTDOWN LOOP
# ----------------------
while True:
    now = datetime.datetime.now()
    time_left = target_datetime - now

    if time_left.total_seconds() <= 0:
        countdown_placeholder.markdown(
            "<div class='message'>The moment has arrived! Enjoy the day, Hfesa ❤️</div>",
            unsafe_allow_html=True,
        )
        break

    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    countdown_text = f"{days}d {hours:02}h {minutes:02}m {seconds:02}s"
    countdown_placeholder.markdown(
        f"<div class='countdown'>{countdown_text}</div>",
        unsafe_allow_html=True,
    )
    time.sleep(1)
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
