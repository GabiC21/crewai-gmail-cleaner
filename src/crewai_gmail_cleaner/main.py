"""Entry point for CrewAI AMP: run() is required for crew deployments."""

import os
import traceback

from crewai_gmail_cleaner.crew import get_crew


def run():
    """Run the Gmail Cleaner crew."""
    print("GMAIL_CLIENT_ID set:", bool(os.environ.get("GMAIL_CLIENT_ID")))
    print("GMAIL_CLIENT_SECRET set:", bool(os.environ.get("GMAIL_CLIENT_SECRET")))
    print("GMAIL_REFRESH_TOKEN set:", bool(os.environ.get("GMAIL_REFRESH_TOKEN")))
    print("OPENAI_API_KEY set:", bool(os.environ.get("OPENAI_API_KEY")))

    try:
        crew = get_crew()
        return crew.kickoff()
    except Exception:
        print("ERROR during crew execution:")
        traceback.print_exc()
        raise


if __name__ == "__main__":
    run()
