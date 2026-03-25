French Oral Exam Tutor (Gemini 2.5 Native Audio)
A high-performance Streamlit application designed for French language students. This tutor utilizes Google’s Gemini 1.5/2.5 multimodal models to provide real-time feedback on French grammar and phonetics by analyzing textbook screenshots and voice recordings.

The Problem it Solves
Standard language applications often lack the specific context of a user's curriculum. This application enables users to synchronize local study materials, providing the AI with the exact vocabulary and grammar rules being studied. It specifically targets French Phonetics, assisting users in mastering complex phonetic rules such as Liaison.

Features
Native Audio Processing: Utilizes gemini-2.5-flash-native-audio-latest (with stable fallbacks) for high-fidelity pronunciation analysis.

Visual Context Synchronization: Supports uploading up to 30 textbook pages (JPG/PNG) to ground the tutor in specific curriculum data.

Smart Quota Management: Includes exception handling for 429 RESOURCE_EXHAUSTED errors to manage Google Cloud Free Tier rate limits.

Hybrid Feedback: Delivers both text-based grammatical corrections and phonetic guidance.

Technical Implementation
This project was developed to resolve specific API versioning conflicts between the v1 and v1beta endpoints of the Google GenAI SDK.

Key Technical Specifications
Frontend: Streamlit

AI Core: Google GenAI SDK (google-genai)

Model Alias: gemini-flash-latest (Optimized for Free Tier stability)

Protocol: Forced v1beta handshake to ensure model availability across different project environments.

Installation and Setup
1. Clone the Repository
git clone https://github.com/Arup/image-audio-tutor.git
cd image-audio-tutor

2. Install Dependencies
pip install streamlit google-genai Pillow

3. Configure Secrets
Create a .streamlit/secrets.toml file and add your API Key:
GEMINI_API_KEY = "your_google_ai_studio_key"

4. Run the Application
streamlit run app.py

Recommended Usage
Synchronization Limit: For optimal performance on the Free Tier, it is recommended to sync 15–30 images per session.

Interaction: Record a reading of a specific paragraph from the synchronized images. Prompt the tutor: "Check my liaison and noun-adjective agreement in this recording."

Step-by-Step Execution
Step 1: Environment Setup
Use a virtual environment to manage dependencies:
python3 -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

Step 2: Install Requirements
pip install streamlit google-genai Pillow

Step 3: Launch the Interface
treamlit run app.py

Step 4: UI Operations
Directory Path: Enter the local path to the French images in the sidebar.

Sync: Select "Sync Now" to load up to 30 images into the model's context window.

Practice: Use the Microphone to record audio or the Chat Input for specific queries, such as "Explain the agreement of the past participle on page 4."
