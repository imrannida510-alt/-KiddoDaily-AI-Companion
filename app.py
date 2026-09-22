# KiddoDaily-AI-Companion - Daily Routine Assistant for Kids
import datetime

def kiddo_assistant():
    print("Assalam-o-Alaikum! Main KiddoDaily hun 😊")
    name = input("Bache ka naam kya hai? ")
    
    print(f"\n{ name } ke liye Aaj ka Routine:")
    print("---------------------------------")
    
    hour = datetime.datetime.now().hour
    
    if hour < 12:
        print("☀️ Good Morning! School ka time ho gaya, jaldi tayyar ho jao!")
    elif hour < 17:
        print("📚 Homework Time! Chalo homework kar lete hain.")
        print("💧 Pani peena mat bhoolo!")
    else:
        print("🌙 Story Time! Ab sone ka time ho gaya hai.")
    
    print("\nYaad-dihani: Mobile kam dekho, achi aadatein apnao!")

if __name__ == "__main__":
    kiddo_assistant()
