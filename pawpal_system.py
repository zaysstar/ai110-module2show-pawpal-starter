from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    description: str
    time: str  # Format: "HH:MM"
    frequency: str
    is_complete: bool = False

    def mark_complete(self):
        """Marks the task as complete."""
        self.is_complete = True

    def update_time(self, new_time: str):
        """Updates the scheduled time of the task."""
        self.time = new_time

@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Adds a new task to the pet's list."""
        self.tasks.append(task)

    def get_pending_tasks(self) -> List[Task]:
        """Returns a list of tasks that are not yet complete."""
        return [task for task in self.tasks if not task.is_complete]

    def get_all_tasks(self) -> List[Task]:
        """Returns all tasks for this pet."""
        return self.tasks

class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        """Adds a new pet to the owner's profile."""
        self.pets.append(pet)

    def get_pet(self, name: str) -> Pet:
        """Retrieves a pet by its name."""
        for pet in self.pets:
            if pet.name.lower() == name.lower():
                return pet
        return None

    def get_all_tasks(self) -> List[Task]:
        """Aggregates and returns every task from all of the owner's pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_all_tasks())
        return all_tasks

class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_daily_schedule(self) -> List[Task]:
        """Retrieves and sorts all tasks for the day."""
        all_tasks = self.owner.get_all_tasks()
        return self.sort_by_time(all_tasks)

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Sorts a list of tasks chronologically by their time attribute."""
        # Uses a lambda function as a key to sort the "HH:MM" strings
        return sorted(tasks, key=lambda task: task.time)

    def check_conflicts(self, tasks: List[Task]) -> List[str]:
        """Checks for overlapping tasks and returns a list of warning messages."""
        seen_times = set()
        warnings = []
        for task in tasks:
            if task.time in seen_times:
                warnings.append(f"⚠️ Conflict Detected: Multiple tasks scheduled at {task.time}!")
            seen_times.add(task.time)
        return warnings

    def filter_tasks(self, tasks: List[Task], status: bool = None) -> List[Task]:
        """Filters tasks based on completion status."""
        if status is None:
            return tasks
        return [task for task in tasks if task.is_complete == status]