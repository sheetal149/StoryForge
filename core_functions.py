import os 
from dotenv import load_dotenv
import google.generativeai as genai
from tavily import TavilyClient 


load_dotenv()

#configure APIs
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

#Select the model 
MODEL_INFO = "gemini-2.0-flash"
MODEL_SCRIPT = "gemini-2.0-flash"



# --- Main function for real-time info fetching ---
def get_realtime_info(query, tavily_api_key=None, gemini_api_key=None):
    """
    Fetches up-to-date information about any topic using Tavily Search API
    and summarizes it using Gemini.
    """
    # Use provided keys or fallback to env vars
    t_key = tavily_api_key or os.getenv("TAVILY_API_KEY")
    g_key = gemini_api_key or os.getenv("GEMINI_API_KEY")

    if not t_key:
        return "⚠️ Tavily API Key is missing."
    if not g_key:
        return "⚠️ Gemini API Key is missing."

    try:
        tavily_client = TavilyClient(api_key=t_key)
        resp = tavily_client.search(
            query=query,
            max_results=3, 
            topic="general"
            )
        if resp and resp.get("results"):
            summaries = []
            for r in resp["results"]:
                title = r.get("title", "")
                snippet = r.get("snippet", "")
                url = r.get("url", "")
                summaries.append(f"**{title}**\n{snippet}\n\n Read more: {url}\n")
            source_info = "\n\n---\n\n".join(summaries)
        else:
            source_info = f"No recent updates found on '{query}'."
        
    except Exception as e:
        print(f"Error fetching data from Tavily: {e}")
        return f"Error fetching data from Tavily: {e}"
    
    # Refine & summarize the content via Gemini
    prompt = f"""
You are a professional researcher and content creator with expertise in multiple fields.
Using the following real-time information, write an accurate, engaging, and human-like summary
for the topic: '{query}'.

Requirements:
- Keep it factual, insightful, and concise (around 200 words).
- Maintain a smooth, natural tone.
- Highlight key takeaways or trends.
- Avoid greetings or self-references.

Source information:
{source_info}

Output only the refined, human-readable content.
"""
    try:
        genai.configure(api_key=g_key)
        model = genai.GenerativeModel(MODEL_INFO)
        response = model.generate_content(prompt)
        return response.text.strip() if response and response.text else source_info
    except Exception as e:
        print(f"Error generating summary: {e}")
        return source_info
    
# --- Generate video transcription ---
def generate_video_transcription(info_text, gemini_api_key=None):
    g_key = gemini_api_key or os.getenv("GEMINI_API_KEY")
    
    if not g_key:
        return "⚠️ Gemini API Key is missing."

    prompt = f"""
You are a creative scriptwriter.
Turn this real-time information into an engaging short video script (for YouTube Shorts or Instagram Reels).
Use a conversational tone with a strong hook and a clear call to action at the end.
Keep it around 100–120 words.

{info_text}
"""
    try:
        genai.configure(api_key=g_key)
        model = genai.GenerativeModel(MODEL_SCRIPT)
        response = model.generate_content(prompt)
        return response.text.strip() if response and response.text else "⚠️ Could not generate video script."
    except Exception as e:
        print(f"❌ Error generating video script: {e}")
        return None