 Personal Wikipedia Builder Crew — AI Wiki Article Generator

This project is an AI-powered system that generates personalized Wikipedia-style articles from user-provided topics or keywords. It combines advanced natural language generation with real-time semantic search to create accurate, well-structured content.

The frontend uses **Gradio** to deliver a responsive, interactive web interface where users input queries and receive detailed wiki-like articles instantly.

 How It Works

 **User Input:** Enter a topic or keyword via the Gradio UI.
 **Data Retrieval:** `duckducksearch` fetches relevant contextual information to ground the article in real-world data.
 **Content Generation:**

  The `openai` API generates coherent, human-like text.
  `crewai` enhances AI collaboration and advanced text synthesis.
   `langchain` orchestrates the workflow, chaining search results and generation for well-structured outputs.
 **Output:** Cleanly formatted Wikipedia-style articles rendered in the UI.

## Features

 Combines semantic search with AI text generation for improved accuracy.
 Modular architecture using LangChain for flexible pipeline management.
 Collaborative model orchestration with CrewAI for high-quality text synthesis.
 User-friendly Gradio interface for fast prototyping and deployment.
 Easily extensible for additional data sources or AI models.

 Requirements

 Python 3.8+
 `openai`
 `crewai`
 `duckducksearch`
 `langchain`
 `gradio`

 Installation
 
pip install openai crewai duckducksearch langchain gradio

 Usage

Run the Gradio app locally or deploy on the cloud. Input a topic and get a detailed Wikipedia-style article generated instantly.

