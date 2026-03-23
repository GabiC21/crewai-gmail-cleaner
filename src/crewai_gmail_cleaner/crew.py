"""Crew definition for Gmail Cleaner."""

from crewai import Agent, Crew, Task
from crewai.tools import tool
from crewai_gmail_cleaner.tools.gmail_tools import delete_email, fetch_unread


@tool("fetch_unread_emails")
def fetch_unread_emails() -> str:
    """Fetches unread emails from Gmail. Returns message objects with 'id' and 'threadId'."""
    messages = fetch_unread()
    if not messages:
        return "No unread messages."
    return str(messages)


@tool("delete_email")
def delete_email_tool(message_id: str) -> str:
    """Moves an email to trash by message ID. Input must be the message id string."""
    return delete_email(message_id)


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
    expected_output="List of unread email IDs and thread IDs",
    agent=reader_agent,
)

classify_task = Task(
    description="Identify emails from plain.com or linear.app",
    expected_output="List of email IDs that are from Plain or Linear",
    agent=classifier_agent,
)

cleanup_task = Task(
    description="Delete emails identified as notifications",
    expected_output="Confirmation of deleted email IDs",
    agent=cleanup_agent,
)


def get_crew() -> Crew:
    return Crew(
        agents=[reader_agent, classifier_agent, cleanup_agent],
        tasks=[read_task, classify_task, cleanup_task],
        verbose=True,
    )