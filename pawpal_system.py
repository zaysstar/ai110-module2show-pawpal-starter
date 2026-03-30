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
        """Retrieves all tasks for the day."""
        # For Phase 2, we just return all tasks. We will add sorting in Phase 4!
        return self.owner.get_all_tasks()
        
    # We will build out sort_by_time, check_conflicts, and filter_tasks in Phase 4