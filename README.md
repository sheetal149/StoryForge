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

1.  Create a `.env` file in the root directory.
2.  Add your API keys:

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

1.  Enter a topic in the search bar.
2.  Read the AI-generated summary.
3.  Choose "Yes" to generate a video script.
4.  Download the script if needed.

### Running the MCP Server

To run the MCP server for agentic integration:

```bash
python mcp_server.py
```

The server exposes two tools:
-   `get_latest_info_mcp(query)`: Fetches real-time info.
-   `generate_video_script_mcp(query)`: Generates a video script directly.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
