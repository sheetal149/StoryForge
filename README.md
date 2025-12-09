# StoryForge Agent 🌐

StoryForge Agent is an AI-powered tool designed to streamline the process of researching topics and creating engaging video scripts for short-form content (YouTube Shorts, Instagram Reels, TikTok).

It leverages **Tavily Search API** for real-time information retrieval and **Google Gemini** for intelligent summarization and creative scriptwriting.


## 🚀 Features

-   **Real-time Topic Research**: Fetches the latest information on any given topic using Tavily.
-   **AI Summarization**: Generates concise, human-readable summaries of the gathered information.
-   **Video Script Generation**: Automatically converts the summary into an engaging video script tailored for short-form video platforms.
-   **Modern UI**: A sleek, dark-themed interface built with Streamlit.
-   **MCP Server Support**: Includes a Model Context Protocol (MCP) server implementation for integration with other AI agents.

## 🛠️ Tech Stack

-   **Python**: Core programming language.
-   **Streamlit**: Web application framework.
-   **Google Gemini API**: Generative AI for text and script generation.
-   **Tavily API**: Real-time web search and context retrieval.
-   **FastMCP**: Framework for building the MCP server.

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd StoryForge-agent-mcp
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\activate

    # Mac/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```


## 🔑 Configuration

You can configure the API keys in two ways:

### 1. via App Interface (Recommended for simple usage)
When you run the Streamlit app, you can simply enter your **Gemini API Key** and **Tavily API Key** directly in the sidebar.

### 2. via `.env` file (Required for MCP Server)
Create a `.env` file in the root directory and add your keys:

```env
GEMINI_API_KEY=your_google_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## 🖥️ Usage

### Running the Streamlit App

To use the interactive web interface:

```bash
streamlit run app.py
```

1.  **Enter your API keys in the sidebar.** (This is required before searching).
2.  Enter a topic in the search bar.
3.  Read the AI-generated summary.
4.  Choose "Yes" to generate a video script.
5.  Download the script if needed.

### Running the MCP Server

To run the MCP server for agentic integration:

```bash
python mcp_server.py
```

The server exposes two tools:
-   `get_latest_info_mcp(query)`: Fetches real-time info.
-   `generate_video_script_mcp(query)`: Generates a video script directly.

## 🚀 Deployment

### 🐳 Docker (Local)

Build and run the container locally:

```bash
docker build -t storyforge .
docker run -p 8080:8080 storyforge
```

### ☁️ Google Cloud Run

Deploy directly to Google Cloud Run (requires [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)):

```bash
gcloud run deploy storyforge --source . --port 8080 --allow-unauthenticated
```

<img width="957" height="533" alt="Screenshot 2025-12-06 020952" src="https://github.com/user-attachments/assets/165e1842-d283-4e53-9164-cf18de86049a" />

<img width="1918" height="1065" alt="Screenshot 2025-12-06 021312" src="https://github.com/user-attachments/assets/5c57a310-a592-4146-8d17-73da74723a67" />

<img width="1917" height="1071" alt="Screenshot 2025-12-06 021332" src="https://github.com/user-attachments/assets/ff97e20f-fc77-4d64-8136-22c7f1a34905" />




