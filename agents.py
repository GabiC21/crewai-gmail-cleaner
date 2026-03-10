"""CrewAI agents for the Gmail Cleaner: reader, classifier, and cleanup."""

from langchain.tools import Tool

from crewai import Agent

from gmail_tools import fetch_unread, delete_email


# --- Gmail tools for CrewAI (LangChain Tool wrappers) ---

def _fetch_unread_tool() -> str:
    """Fetch unread emails from Gmail. Returns a list of message dicts with 'id' and 'threadId'."""
    messages = fetch_unread()
    if not messages:
        return "No unread messages."
    return str(messages)


def _delete_email_tool(message_id: str) -> str:
    """Move an email to Gmail trash by its message ID. Call this only after deciding the email should be deleted."""
    return delete_email(message_id)


fetch_unread_emails = Tool.from_function(
    func=_fetch_unread_tool,
    name="fetch_unread_emails",
    description="Fetches the list of unread emails from Gmail. Returns message objects with 'id' and 'threadId'. Use this to see what emails need to be reviewed.",
)

delete_email_tool = Tool.from_function(
    func=_delete_email_tool,
    name="delete_email",
    description="Moves an email to trash by its message ID. Only use after the email has been identified as Plain or Linear. Input must be the message id string.",
)


# --- Agents (ChatGPT steps) ---

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
