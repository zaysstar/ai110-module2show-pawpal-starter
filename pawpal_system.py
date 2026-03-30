from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    description: str
    time: str  # Format: "HH:MM"
    frequency: str
    is_complete: bool = False

    def mark_complete(self):
        """Marks the task as complete and handles recurrence."""
        pass

    def update_time(self, new_time: str):
        """Updates the scheduled time of the task."""
        pass

@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Adds a new task to the pet's list."""
        pass

    def get_pending_tasks(self) -> List[Task]:
        """Returns a list of tasks that are not yet complete."""
        pass

    def get_all_tasks(self) -> List[Task]:
        """Returns all tasks for this pet."""
        pass

class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        """Adds a new pet to the owner's profile."""
        pass

    def get_pet(self, name: str) -> Pet:
        """Retrieves a pet by its name."""
        pass

    def get_all_tasks(self) -> List[Task]:
        """Aggregates and returns every task from all of the owner's pets."""
        pass

class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_daily_schedule(self) -> List[Task]:
        """Retrieves all tasks for the day."""
        pass

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Sorts a list of tasks chronologically by their time attribute."""
        pass

    def check_conflicts(self):
        """Checks for overlapping tasks and returns warnings."""
        pass

    def filter_tasks(self, status: bool = None, pet_name: str = None) -> List[Task]:
        """Filters tasks based on completion status or a specific pet."""
        pass