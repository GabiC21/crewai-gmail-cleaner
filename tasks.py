from crewai import Task

from agents import reader_agent, classifier_agent, cleanup_agent

read_task = Task(
    description="Read unread emails from Gmail inbox",
    agent=reader_agent
)

classify_task = Task(
    description="Identify emails from plain.com or linear.app",
    agent=classifier_agent
)

cleanup_task = Task(
    description="Delete emails identified as notifications",
    agent=cleanup_agent
)
