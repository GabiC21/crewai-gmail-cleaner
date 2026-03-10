# CrewAI Gmail Cleaner

A CrewAI-based assistant that helps analyze and clean your Gmail inbox.

## Setup

1. Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Configure Gmail API credentials (see [Google Cloud Console](https://console.cloud.google.com/) and enable Gmail API).

3. Copy `.env.example` to `.env` and fill in your values (if you add one).

## Run

```bash
python main.py
```

## Project structure

- `agents.py` – CrewAI agents (e.g. email analyst, cleanup agent)
- `tasks.py` – Tasks (analyze inbox, suggest deletions)
- `crew.py` – Crew definition and workflow
- `gmail_tools.py` – Gmail API tools (list, delete, etc.)
- `main.py` – Entry point
