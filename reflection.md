# PawPal+ Project Reflection

## 1. System Design

**Core Actions:**
1. Add a new pet to the owner's profile.
2. Schedule a recurring or one-time task (like feeding or a walk) for a specific pet.
3. View the daily schedule of all tasks across all pets, sorted by time.

**a. Initial design**
I designed the system using four primary classes to separate concerns effectively:
* **Task:** Acts as a data container holding the description, time, frequency, and completion status of a specific activity.
* **Pet:** Represents an individual animal, storing its name, species, and a dedicated list of its own `Task` objects.
* **Owner:** Acts as the main user profile, holding a name and managing a list of `Pet` objects.
* **Scheduler:** The "brain" of the operation. It takes in an `Owner` object and handles the complex logic of aggregating all tasks from all pets, sorting them by time, and checking for scheduling conflicts.

classDiagram
    class Task {
        +String description
        +String time
        +String frequency
        +Boolean is_complete
        +mark_complete()
        +update_time()
    }

    class Pet {
        +String name
        +String species
        +List~Task~ tasks
        +add_task(task)
        +get_pending_tasks()
        +get_all_tasks()
    }

    class Owner {
        +String name
        +List~Pet~ pets
        +add_pet(pet)
        +get_pet(name)
        +get_all_tasks()
    }

    class Scheduler {
        +Owner owner
        +get_daily_schedule()
        +sort_by_time()
        +check_conflicts()
        +filter_tasks(status, pet_name)
    }

    Owner "1" *-- "*" Pet : owns
    Pet "1" *-- "*" Task : has
    Scheduler --> "1" Owner : manages

**b. Design changes**
Based on AI feedback during the scaffolding phase, I decided to implement `Task` and `Pet` using Python's `@dataclass` decorator. Since these classes primarily exist to hold state (data) rather than execute complex independent logic, using dataclasses significantly reduces boilerplate `__init__` code and makes the architecture cleaner and more readable.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
