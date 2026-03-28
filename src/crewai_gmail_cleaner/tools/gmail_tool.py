"""Gmail API helpers and CrewAI Tool wrappers."""

import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from crewai.tools import tool as crewai_tool


def get_service():
    creds = Credentials(
        token=None,
        refresh_token=os.environ["GMAIL_REFRESH_TOKEN"],
        client_id=os.environ["GMAIL_CLIENT_ID"],
        client_secret=os.environ["GMAIL_CLIENT_SECRET"],
        token_uri="https://oauth2.googleapis.com/token",
    )
    if not creds.valid:
        creds.refresh(Request())
    return build("gmail", "v1", credentials=creds)


def fetch_unread():
    service = get_service()
    results = service.users().messages().list(
        userId="me",
        q="is:unread",
        maxResults=10,
    ).execute()
    return results.get("messages", [])


def delete_email(message_id):
    service = get_service()
    service.users().messages().trash(
        userId="me",
        id=message_id,
    ).execute()
    return f"Deleted {message_id}"


@crewai_tool
def fetch_unread_emails() -> str:
    """Fetches unread emails from Gmail. Returns message objects with id and threadId."""
    messages = fetch_unread()
    if not messages:
        return "No unread messages."
    return str(messages)


@crewai_tool
def delete_email_tool(message_id: str) -> str:
    """Moves an email to trash by message ID. Input must be the message id string."""
    return delete_email(message_id)
