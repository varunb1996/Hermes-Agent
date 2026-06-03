from datetime import datetime


def log_event(event):

    with open(
        "logs/agent_logs.txt",
        "a",
        encoding="utf-8"
    ) as f:

        timestamp = datetime.now()

        f.write(
            f"[{timestamp}] {event}\n"
        )