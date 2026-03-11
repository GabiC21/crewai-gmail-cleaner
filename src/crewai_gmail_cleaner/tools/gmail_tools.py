"""Gmail API helpers for the crew."""

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


def get_service():
    creds = Credentials.from_authorized_user_file("token.json")
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
    service.users().messages().trash(userId="me", id=message_id).execute()
    return f"Deleted {message_id}"
