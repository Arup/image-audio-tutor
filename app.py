import streamlit as st
from google import genai
from google.genai import types
import os
from PIL import Image

# 1. THE "BACK TO BETA" CONFIG
try:
    client = genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"],
        http_options=types.HttpOptions(api_version='v1beta')
    )
    # Using Index 14 confirmed name
    active_model = 'gemini-flash-latest' 
    st.sidebar.success(f"✅ Protocol: v1beta | Model: {active_model}")
except Exception as e:
    st.sidebar.error(f"Setup Error: {e}")

st.set_page_config(page_title="French Oral Tutor", page_icon="🇫🇷")
st.title("🇫🇷 French Oral Exam Tutor")

# 2. SYNC (Capped at 30 images to balance context vs. quota)
if "context" not in st.session_state:
    st.session_state.context = []

with st.sidebar:
    folder_path = st.text_input("Folder Path:", "/Users/etudiantes/fra")
    if st.button("Sync Now"):
        st.session_state.context = []
        if os.path.exists(folder_path):
            # Filtering for images
            files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            # THE 30-IMAGE LIMIT: Prevents "Token Limit" crashes
            for f in files[:30]: 
                st.session_state.context.append(Image.open(os.path.join(folder_path, f)))
            st.success(f"Loaded {len(st.session_state.context)} images")
        else:
            st.error("Directory not found. Please check the path.")

# 3. INTERACTION
audio_input = st.audio_input("Record French")
text_input = st.chat_input("Type 'Bonjour'...")

if audio_input or text_input:
    # Instructions for the Tutor
    parts = ["Role: French Oral Tutor. Task: Correct grammar and Liaison using the textbook images as context."]
    parts.extend(st.session_state.context)

    if audio_input:
        parts.append(types.Part.from_bytes(data=audio_input.getvalue(), mime_type="audio/wav"))
    if text_input:
        parts.append(text_input)

    with st.chat_message("assistant"):
        try:
            response = client.models.generate_content(
                model=active_model,
                contents=parts
            )
            st.markdown(response.text)
        except Exception as e:
            # THE RATE LIMIT EXCEPTION: Specific fix for "429 RESOURCE_EXHAUSTED"
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                st.error("⚠️ **Rate Limit Hit:** You've sent too much data at once for the Free Tier.")
                st.info("Wait **60 seconds** for the quota to reset. Also, try using fewer images if this keeps happening.")
            else:
                st.error(f"Tutor Error: {e}")
