from crewai import Agent
from tools import data_extractor_func, summarizer_func, formatter_func

data_extractor = Agent(
    role="Data Extractor",
    goal="Find raw information about a topic",
    backstory="Expert at gathering detailed info from the internet.",
    function=data_extractor_func,
    verbose=True
)

summarizer = Agent(
    role="Summarizer",
    goal="Condense raw data into summaries",
    backstory="Skilled at summarizing large content.",
    function=summarizer_func,
    verbose=True
)

formatter = Agent(
    role="Formatter",
    goal="Turn summaries into Wikipedia-style articles",
    backstory="Specialist in formatting content cleanly.",
    function=formatter_func,
    verbose=True
)
