"""Entry point for CrewAI AMP: run() is required for crew deployments."""

from crewai_gmail_cleaner.crew import get_crew


def run():
    """Run the Gmail Cleaner crew."""
    crew = get_crew()
    return crew.kickoff()


if __name__ == "__main__":
    run()
