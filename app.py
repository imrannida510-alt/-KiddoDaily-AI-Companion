import streamlit as st

st.set_page_config(page_title="KiddoDaily", page_icon="👶")

st.image("image.png", width=250)
st.title("KiddoDaily-AI-Companion 👶🤖")
st.write("Main aap ka pyara dost hun! Mujh se baat karo")

bacha_bola = st.text_input("Aap kya karna chahte ho? (school / homework / khana / sona)")

if bacha_bola:
    if "school" in bacha_bola.lower():
        st.success("☀️ Subah ho gayi beta, school ka time ho gaya hai! Jaldi tayyar ho jao")
        st.audio("https://www.soundjay.com/human/sounds/man-hello-01.mp3")
    elif "homework" in bacha_bola.lower():
        st.success("📚 Shabash! Chalo homework kar lete hain, aap to bohat zaheen ho")
    elif "khana" in bacha_bola.lower():
        st.success("🍎 Khana kha lo beta, sehatmand bano")
    elif "sona" in bacha_bola.lower():
        st.success("🌙 Chalo ab story sun kar so jate hain, Good Night!")
    else:
        st.info("Main sun raha hun pyare bache, bolo kya chahiye?")

st.markdown("---")
st.write("Made with ❤️ for MOTHERS & KIDS by NIDA")
