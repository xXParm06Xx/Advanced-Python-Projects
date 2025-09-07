import streamlit as st
import smtplib
import random, time
import configparser

# Loading Config file
config = configparser.ConfigParser()

# Config file Error Handling
try:
    config.read("Config.ini")
    if "EMAIL" not in config:
        st.error("\U0000274C Error, [EMAIL] section is missing in Config.ini")
        st.stop()

    SERVER_SMTP = config["EMAIL"]["smtp_server"]
    PORT_SMTP = int(config["EMAIL"]["smtp_port"])

    PASS = config["EMAIL"]["sender_pass"].strip()
    if PASS == "":
        st.error("Please Enter Password in Config.ini !!")
        st.stop()

    SUBJECT = config["EMAIL"]["subject"]
    MESSAGE_BODY = config["EMAIL"]["message"]

except Exception as e:
    st.error(f"\U0000274C Config Error: {e}")
    st.stop()
 
# Sidebar
st.sidebar.title("Menu")
name = st.sidebar.text_input("Enter Your Name")
EMAIL = st.sidebar.text_input("Enter Your Email")
st.sidebar.write("-- Made with \u2764\uFE0F By Parm")

# Function to send email OTP
def send_email(receiver_email, otp):
    body = MESSAGE_BODY.replace("{otp}", str(otp))
    message = f"Subject: {SUBJECT}\n\n{body}"
    try:
        server = smtplib.SMTP(SERVER_SMTP, PORT_SMTP)
        server.starttls()
        server.login(EMAIL, PASS)
        server.sendmail(EMAIL, receiver_email, message)
        server.quit()
        return True
    
    except Exception as e:
        st.error(f"\U0000274C ERROR: OTP failed to send. {e}")
        st.info("Check Details inside Config file !!")
        st.stop()
        return False

# --- Streamlit UI ---
st.title("\U0001F510 OTP Generator & Verifier")

if name and EMAIL and PASS:
    st.write(f"Welcome, {name} !")
    st.subheader(f"Sender: {EMAIL}")

    # Step 1: Enter email
    receiver_email = st.text_input("Enter Receiver's Email")

    # Step 2: Send OTP
    if st.button("\U0001f4e9 Send OTP", help="To send OTP on Receiver's Email"):
           if receiver_email:
                otp = random.randint(100000, 999999)
                st.session_state.otp = str(otp)
                st.session_state.otp_time = time.time()
                st.session_state.attempts = 0

                if send_email(receiver_email, otp):
                    st.balloons()
                    st.success("\u2705 OTP Sent Successfully! Check your inbox.")
           else:
                st.warning(f"\U0000274C ERROR, Please enter a valid email.")

    # Step 3: Verify OTP (only if OTP was sent)
    if "otp" in st.session_state:
        user_input = st.text_input("Enter OTP:",type="password")
       
        if st.button("Verify OTP",help="To verify entered OTP"):
            current_time = time.time()
            st.session_state.attempts += 1 # now attempts = 1

            if current_time - st.session_state.otp_time > 300:
                st.error("\U000023F3 OTP Expired, Please request a new one.")

            elif user_input == st.session_state.otp:
                st.success("\U0001F389 Verified Successfully!")

            else:
                if st.session_state.attempts < 3:
                    st.error(f"\U0000274C Incorrect OTP. Attempts left: {3 - st.session_state.attempts}")
                else:
                    st.error("\U0000274C Too many unsuccessful tries. Please request a new OTP.")
else:
    st.warning("\U0001F4F1 Please enter details in Menu !!")

with st.expander(" \U0001F4DC Guidelines !!" ):
    st.write("""
1. This is a OTP Sender and Verifier.
2. This uses Python's smtplib for sending OTPs on respective Email and Streamlit for UI
3. OTP message can be configured through Config file
4. Read README.md for more Instructions
5. More Features and Updates Coming Soon.....
""")