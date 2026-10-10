import streamlit as st
from gtts import gTTS
import os

st.set_page_config(page_title="KiddoDaily AI", page_icon="👶")

# Logo - agar image.png mile to dikhao, warna skip
if os.path.exists("image.png"):
    st.image("image.png", width=200)
elif os.path.exists("logo.png"):
    st.image("logo.png", width=200)

st.title("KiddoDaily-AI-Companion 👶")
st.write("Main aap ka pyara dost hun! Mujh se kuch bhi baat karo ❤️")
st.write("Jaise: school / homework / tuition / khana / sona / udaas")

user_input = st.text_input("Yahan likho...")

def speak(text):
    try:
        tts = gTTS(text=text, lang='ur')
        tts.save("awaz.mp3")
        st.audio("awaz.mp3", format='audio/mp3')
    except Exception as e:
        st.warning("Awaz chalane me masla hai, lekin jawab neeche hai")

def get_smart_reply(text):
    text = text.lower()
    if "school" in text:
        return "Subah ho gayi mere pyare bache, school ka time ho gaya, jaldi tayyar ho jao beta!"
    elif "tuition" in text or "tution" in text:
        return "Haan beta, tuition ka time ho gaya hai, apna bag check kar lo, Allah kamyab kare!"
    elif "homework" in text or "kaam" in text:
        return "Shabash beta, chalo homework kar lete hain, mai aap ki madad karunga!"
    elif "khana" in text or "bhook" in text:
        return "Aao beta khana kha lo, khana thanda ho raha hai, hath dho kar aao!"
    elif "sona" in text or "neend" in text:
        return "Raat ho gayi hai mere bache, mobile rakh do aur so jao, subha jaldi uthna hai!"
    elif "udaas" in text or "sad" in text:
        return f"Mera pyara bacha udaas hai? Aap ne kaha '{text}'. Koi baat nahi, mai aap ke sath hun!"
    elif text.strip() == "":
        return ""
    else:
        # AB KUCH BHI BOLOGE TO JAWAB DEGA
        return f"Wah beta, aap ne kaha '{text}'. Bohat achi baat hai! Aur batao, mai sun raha hun."

if user_input:
    reply = get_smart_reply(user_input)
    if reply:
        st.success(f"👶 {reply}")
        speak(reply)

st.markdown("---")
st.write("Made with ❤️ for MOTHERS & KIDS by NIDA")
