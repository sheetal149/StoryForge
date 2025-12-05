import streamlit as st
import os 
from dotenv import load_dotenv
import google.generativeai as genai
from tavily import TavilyClient 
from  core_functions import get_realtime_info, generate_video_transcription

# Streamlit page setup
st.set_page_config(
    page_title="StoryForge Agent",
    page_icon="🌐",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Custom modern CSS theme with MAXIMUM visibility ---
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: #f5f5f5;
        }
        h1, h2, h3 {
            text-align: center;
            color: #F9FAFB !important;
        }
        
        /* FORCE ALL TEXT TO BE VISIBLE */
        * {
            color: #F9FAFB !important;
        }
        
        /* Text input styling */
        .stTextInput > label > div > p,
        .stTextInput > label,
        .stTextInput label {
            color: #FFFFFF !important;
            font-weight: 600 !important;
        }
        .stTextInput>div>div>input {
            border: 1px solid #6EE7B7 !important;
            border-radius: 10px;
            padding: 12px;
            background-color: #111827;
            color: white !important;
        }
        
        /* Button styling */
        div.stButton > button,
        div.stButton > button > div,
        div.stButton > button > div > p {
            background: linear-gradient(90deg, #06b6d4, #3b82f6) !important;
            color: #FFFFFF !important;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            font-weight: 600 !important;
            border: none;
            transition: 0.3s ease-in-out;
        }
        div.stButton > button:hover {
            transform: scale(1.05);
            background: linear-gradient(90deg, #2563eb, #06b6d4) !important;
        }
        
        /* Download button - FORCE BLACK TEXT for visibility */
        div.stDownloadButton > button,
        div.stDownloadButton > button *,
        div.stDownloadButton button p,
        div.stDownloadButton button span,
        div.stDownloadButton button div {
            color: #000000 !important;
            font-weight: 600 !important;
            background: linear-gradient(90deg, #06b6d4, #3b82f6) !important;
        }
        
        /* Radio button - FORCE WHITE TEXT */
        .stRadio > label,
        .stRadio > label > div,
        .stRadio > label > div > p,
        .stRadio label,
        .stRadio p,
        .stRadio span,
        .stRadio div {
            color: #FFFFFF !important;
            font-weight: 500 !important;
        }
        .stRadio > div {
            justify-content: center;
        }
        
        /* SIDEBAR - Light background with dark text for visibility */
        section[data-testid="stSidebar"] {
            background-color: #1f2937 !important;
        }
        section[data-testid="stSidebar"],
        section[data-testid="stSidebar"] *,
        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] div,
        section[data-testid="stSidebar"] span {
            color: #FFFFFF !important;
        }
        section[data-testid="stSidebar"] a {
            color: #6EE7B7 !important;
        }
        
        .card {
            background-color: rgba(255, 255, 255, 0.05);
            padding: 20px;
            border-radius: 16px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            margin-top: 20px;
        }
        
        footer, .stCaption {
            text-align: center;
            color: #9CA3AF !important;
        }
    </style>
""", unsafe_allow_html=True)
    

# --- Streamlit UI ---
def main():
    st.markdown("<h1>🌐StoryForge Agent</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#D1D5DB;'>Search any topic — from world news to research trends — and get AI-powered insights & video scripts instantly 🚀</p>", unsafe_allow_html=True)

    # Sidebar for API Keys
    with st.sidebar:
        st.markdown("<h2 style='color: #FFFFFF !important;'>🔑 API Configuration</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: #FFFFFF !important;'>Enter your API keys below to use the app.</p>", unsafe_allow_html=True)
        
        gemini_key = st.text_input("Gemini API Key", type="password", help="Get it from Google AI Studio")
        tavily_key = st.text_input("Tavily API Key", type="password", help="Get it from Tavily")
        
        st.markdown("---")
        st.markdown("<p style='color: #FFFFFF !important;'><a href='https://aistudio.google.com/app/apikey' style='color: #6EE7B7 !important;'>Get Gemini Key</a></p>", unsafe_allow_html=True)
        st.markdown("<p style='color: #FFFFFF !important;'><a href='https://tavily.com/' style='color: #6EE7B7 !important;'>Get Tavily Key</a></p>", unsafe_allow_html=True)

    query = st.text_input("🔎 Enter your topic or question:", key="query_input")


    if query:
        if not gemini_key or not tavily_key:
            st.error("⚠️ Please enter both API keys in the sidebar to proceed.")
        else:
            with st.spinner('🌍 Gathering latest information...'):
                info_result = get_realtime_info(query, tavily_api_key=tavily_key, gemini_api_key=gemini_key)

            if info_result:
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.subheader("📚 AI-Generated Summary")
                st.write(info_result)
                st.markdown("</div>", unsafe_allow_html=True)

                st.markdown("<p style='color: #FFFFFF !important; font-weight: 600; text-align: center;'>🎬 Generate a short video script?</p>", unsafe_allow_html=True)
                generate_script = st.radio(
                    "",
                    ("No", "Yes"),
                    index=0,
                    horizontal=True,
                    label_visibility="collapsed"
                )

                if generate_script == "Yes":
                    with st.spinner('🎥 Crafting your video script...'):
                        script = generate_video_transcription(info_result, gemini_api_key=gemini_key)

                    if script:
                        st.markdown("<div class='card'>", unsafe_allow_html=True)
                        st.subheader("🎥 Video Script")
                        st.write(script)
                        st.download_button(
                            label="📥 Download Script",
                            data=script,
                            file_name="video_script.txt",
                            mime="text/plain"
                        )
                        st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        st.warning("⚠️ Could not generate transcription.")
            else:
                st.warning("⚠️ No valid information found. Please try another query.")


    st.markdown("<hr>", unsafe_allow_html=True)
    st.caption("Made with 💖")

if __name__ == "__main__":
    main()