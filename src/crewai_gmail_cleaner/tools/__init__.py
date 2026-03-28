"""Tools for the Gmail Cleaner crew."""

from .gmail_tool import (
    delete_email,
    delete_email_tool,
    fetch_unread,
    fetch_unread_emails,
    get_service,
)

__all__ = [
    "delete_email",
    "delete_email_tool",
    "fetch_unread",
    "fetch_unread_emails",
    "get_service",
]
