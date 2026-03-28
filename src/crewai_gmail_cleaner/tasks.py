"""Gmail Cleaner tasks (CrewAI @task)."""

from crewai import Task
from crewai.project import task


class GmailTaskComponents:
    """Mix into a @CrewBase class; provides task factories from YAML."""

    @task
    def read_task(self) -> Task:
        return Task(config=self.tasks_config["read_task"])

    @task
    def classify_task(self) -> Task:
        return Task(config=self.tasks_config["classify_task"])

    @task
    def cleanup_task(self) -> Task:
        return Task(config=self.tasks_config["cleanup_task"])
