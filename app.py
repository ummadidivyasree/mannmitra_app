import streamlit as st
import openai
from textblob import TextBlob

st.set_page_config(page_title="MannMitra - Mental Wellness Companion", page_icon="💙")

st.title("💙 MannMitra - Your Mental Wellness Companion")
st.write("A safe, friendly space to share your thoughts and find positivity.")

# API key input
api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Chat input
user_input = st.text_area("How are you feeling today?")

if st.button("Send") and api_key and user_input:
    openai.api_key = api_key
    
    # Mood detection
    mood = TextBlob(user_input).sentiment.polarity
    if mood > 0.1:
        mood_status = "😊 Positive"
    elif mood < -0.1:
        mood_status = "😰 Stressed"
    else:
        mood_status = "😐 Neutral"
    
    st.write("**Mood Detected:**", mood_status)
    
    # AI Response
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are MannMitra, a kind and empathetic mental wellness companion. Reply in short, caring, and supportive ways."},
                {"role": "user", "content": user_input}
            ]
        )
        st.write("🤖 MannMitra:", response["choices"][0]["message"]["content"])
    except Exception as e:
        st.error(f"Error: {e}")

st.subheader("✨ Quick Wellness Tools")
col1, col2 = st.columns(2)

with col1:
    if st.button("🌬️ Breathing Exercise"):
        st.info("Try this: Inhale for 4 sec 🫁, hold for 4 sec ⏸️, exhale for 6 sec 🌬️. Repeat 3 times.")
    if st.button("📖 Journal Prompt"):
        st.info("Write about one small thing that made you smile today.")

with col2:
    if st.button("💡 Motivation Quote"):
        st.info("“Believe you can and you're halfway there.” – Theodore Roosevelt")
    if st.button("🕒 1-Minute Meditation"):
        st.info("Close your eyes, focus on your breath, and let go of today’s worries for 60 seconds.")

st.caption("⚠️ Disclaimer: MannMitra is not a replacement for professional help. For severe distress, please seek professional support.")