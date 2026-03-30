from pawpal_system import Task, Pet, Owner, Scheduler

def main():
    # 1. Create the Owner
    owner = Owner("Izayah") 

    # 2. Create Pets
    dog = Pet("Apollo", "Dog")
    cat = Pet("Luna", "Cat")
    owner.add_pet(dog)
    owner.add_pet(cat)

    # 3. Add Tasks
    dog.add_task(Task("Morning Walk", "08:00", "Daily"))
    dog.add_task(Task("Evening Feeding", "18:00", "Daily"))
    cat.add_task(Task("Litter Box Cleaning", "09:00", "Weekly"))

    # 4. Initialize Scheduler and Print Schedule
    scheduler = Scheduler(owner)
    todays_tasks = scheduler.get_daily_schedule()

    # 5. Formatted Output for Terminal
    print(f"\n🐾 Today's Schedule for {owner.name}'s Pets 🐾")
    print("-" * 45)
    for pet in owner.pets:
        for task in pet.get_all_tasks():
            status = "✅" if task.is_complete else "❌"
            print(f"[{task.time}] {pet.name}: {task.description} ({task.frequency}) - {status}")
    print("-" * 45 + "\n")

if __name__ == "__main__":
    main()