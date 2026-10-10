import streamlit as st
from gtts import gTTS

st.set_page_config(page_title="KiddoDaily", page_icon="👶")
st.image("logo.png", width=250)
st.title("KiddoDaily-AI-Companion 👶")
st.write("Main aap ka pyara dost hun! Mujh se kuch bhi baat karo ❤️")

user_input = st.text_input("Aap kya bolna chahte ho? (kuch bhi likho)")

def speak(text):
    try:
        tts = gTTS(text=text, lang='ur')
        tts.save("awaz.mp3")
        st.audio("awaz.mp3", format='audio/mp3')
    except:
        st.audio("awaz.mp3")

# --- YEHI JAADU HAI ---
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
    elif "udaas" in text or "sad" in text or "gussa" in text:
        return f"Arey mera pyara bacha udaas hai? Aap ne kaha '{text}'. Koi baat nahi, mai aap ke sath hun, sab theek ho jayega!"
    else:
        # YE HAR BAAT KA JAWAB DEGA
        return f"Wah beta, aap ne kaha '{text}'. Bohat achi baat hai, mai sun raha hun, aur batao kya karna hai?"

if user_input:
    reply = get_smart_reply(user_input)
    st.success(f"👶 {reply}")
    speak(reply)

st.markdown("---")
st.write("Made with ❤️ for MOTHERS & KIDS by NIDA")
