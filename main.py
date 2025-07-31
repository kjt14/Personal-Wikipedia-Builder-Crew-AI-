import os

# Set your OpenAI API key here
os.environ["OPENAI_API_KEY"] = "Your API KEY here"


import gradio as gr
from agents import data_extractor, summarizer, formatter
from crewai import Agent, Crew, Task


# Main Wiki Builder Function
def run_wiki_builder(topic):
    task1 = Task(
        description=f"Find detailed information on the topic: {topic}",
        agent=data_extractor,
        expected_output="Raw information about the topic"
    )

    task2 = Task(
        description="Summarize the extracted data into concise bullet points.",
        agent=summarizer,
        expected_output="A short and clear summary"
    )

    task3 = Task(
        description="Format the summary into a Wikipedia-style article with headings.",
        agent=formatter,
        expected_output="Well-formatted Wikipedia-style article"
    )

    crew = Crew(
        agents=[data_extractor, summarizer, formatter],
        tasks=[task1, task2, task3],
        verbose=True
    )

    result = crew.kickoff()
    return result


# Gradio UI
iface = gr.Interface(
    fn=run_wiki_builder,
    inputs=gr.Textbox(label="Enter Topic", placeholder="e.g., Quantum Computing"),
    outputs=gr.Textbox(label="Wikipedia-Style Article"),
    title="Personal Wikipedia Builder"
)

# Launch UI
if __name__ == "__main__":
    iface.launch()
