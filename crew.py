from crewai import Crew

from agents import reader_agent, classifier_agent, cleanup_agent
from tasks import read_task, classify_task, cleanup_task

crew = Crew(
    agents=[reader_agent, classifier_agent, cleanup_agent],
    tasks=[read_task, classify_task, cleanup_task],
    verbose=True
)
