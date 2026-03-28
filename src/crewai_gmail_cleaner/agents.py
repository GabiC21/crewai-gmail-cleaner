"""Gmail Cleaner agents/tools mix-in (@agent / @tool from crewai.project, not crewai root)."""

from crewai import Agent
from crewai.project import agent, tool

from crewai_gmail_cleaner.tools import gmail_tool


class GmailAgentComponents:
    """Mix into a @CrewBase class; provides tool factories and agent factories."""

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
