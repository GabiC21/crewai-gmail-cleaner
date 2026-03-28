"""Gmail Cleaner crew: YAML config; @tool/@agent from crewai.project; Tool objects from crewai.tools."""

from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task, tool

from crewai_gmail_cleaner.tools import gmail_tool


@CrewBase
class CrewaiGmailCleaner:
    """Gmail Cleaner Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @tool
    def fetch_unread_emails(self):
        return gmail_tool.fetch_unread_emails

    @tool
    def delete_email_tool(self):
        return gmail_tool.delete_email_tool

    @agent
    def reader_agent(self) -> Agent:
        return Agent(config=self.agents_config["reader_agent"])

    @agent
    def classifier_agent(self) -> Agent:
        return Agent(config=self.agents_config["classifier_agent"])

    @agent
    def cleanup_agent(self) -> Agent:
        return Agent(config=self.agents_config["cleanup_agent"])

    @task
    def read_task(self) -> Task:
        return Task(config=self.tasks_config["read_task"])

    @task
    def classify_task(self) -> Task:
        return Task(config=self.tasks_config["classify_task"])

    @task
    def cleanup_task(self) -> Task:
        return Task(config=self.tasks_config["cleanup_task"])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )


def get_crew() -> Crew:
    return CrewaiGmailCleaner().crew()
