"""Crew definition for Gmail Cleaner (Plain/Linear notifications)."""

from langchain.tools import Tool

from crewai import Agent, Crew, Task

from crewai_gmail_cleaner.tools.gmail_tools import delete_email, fetch_unread


def _fetch_unread_tool() -> str:
    messages = fetch_unread()
    if not messages:
        return "No unread messages."
    return str(messages)


def _delete_email_tool(message_id: str) -> str:
    return delete_email(message_id)


fetch_unread_emails = Tool.from_function(
    func=_fetch_unread_tool,
    name="fetch_unread_emails",
    description="Fetches unread emails from Gmail. Returns message objects with 'id' and 'threadId'.",
)

delete_email_tool = Tool.from_function(
    func=_delete_email_tool,
    name="delete_email",
    description="Moves an email to trash by message ID. Input must be the message id string.",
)

reader_agent = Agent(
    role="Inbox Reader",
    goal="Fetch unread Gmail emails",
    backstory="Expert inbox automation assistant",
    tools=[fetch_unread_emails],
    verbose=True,
)

classifier_agent = Agent(
    role="Notification Classifier",
    goal="Identify emails from Plain or Linear",
    backstory="Specialist in SaaS notifications",
    verbose=True,
)

cleanup_agent = Agent(
    role="Inbox Cleaner",
    goal="Delete Plain and Linear emails",
    backstory="Maintains inbox hygiene",
    tools=[delete_email_tool],
    verbose=True,
)

read_task = Task(
    description="Read unread emails from Gmail inbox",
    agent=reader_agent,
)

classify_task = Task(
    description="Identify emails from plain.com or linear.app",
    agent=classifier_agent,
)

cleanup_task = Task(
    description="Delete emails identified as notifications",
    agent=cleanup_agent,
)


def get_crew() -> Crew:
    return Crew(
        agents=[reader_agent, classifier_agent, cleanup_agent],
        tasks=[read_task, classify_task, cleanup_task],
        verbose=True,
    )
