"""Gmail API helpers: build service, fetch unread messages, delete/trash emails."""

import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build


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
        maxResults=10
    ).execute()
    return results.get("messages", [])


def delete_email(message_id):
    service = get_service()
    service.users().messages().trash(
        userId="me",
        id=message_id
    ).execute()
    return f"Deleted {message_id}"
