from pawpal_system import Task, Pet

def test_task_completion():
    """Verify that calling mark_complete() changes the task's status."""
    task = Task("Test Walk", "10:00", "Daily")
    assert task.is_complete == False
    
    task.mark_complete()
    assert task.is_complete == True

def test_add_task_to_pet():
    """Verify that adding a task to a Pet increases that pet's task count."""
    pet = Pet("Buddy", "Dog")
    task = Task("Feeding", "08:00", "Daily")
    
    assert len(pet.tasks) == 0
    pet.add_task(task)
    
    assert len(pet.tasks) == 1
    assert pet.tasks[0].description == "Feeding"