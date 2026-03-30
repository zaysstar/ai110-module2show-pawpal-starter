from pawpal_system import Task, Pet, Owner, Scheduler

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

def test_sort_by_time():
    """Verify that the Scheduler correctly sorts tasks chronologically."""
    owner = Owner("Test Owner")
    scheduler = Scheduler(owner)
    
    # Create tasks out of order
    task1 = Task("Late Task", "18:00", "Daily")
    task2 = Task("Early Task", "08:00", "Daily")
    task3 = Task("Mid Task", "12:00", "Daily")
    
    unsorted_tasks = [task1, task2, task3]
    sorted_tasks = scheduler.sort_by_time(unsorted_tasks)
    
    # Check that they are in the correct order (08:00, 12:00, 18:00)
    assert sorted_tasks[0].time == "08:00"
    assert sorted_tasks[1].time == "12:00"
    assert sorted_tasks[2].time == "18:00"

def test_check_conflicts():
    """Verify that the Scheduler flags tasks scheduled at the exact same time."""
    owner = Owner("Test Owner")
    scheduler = Scheduler(owner)
    
    # Create two tasks at the exact same time
    task1 = Task("Walk", "10:00", "Daily")
    task2 = Task("Vet", "10:00", "Once")
    task3 = Task("Feed", "18:00", "Daily")
    
    tasks = [task1, task2, task3]
    warnings = scheduler.check_conflicts(tasks)
    
    # There should be exactly one warning for the 10:00 conflict
    assert len(warnings) == 1
    assert "10:00" in warnings[0]